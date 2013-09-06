# -*- encoding: utf-8 -*-
"""
goatnails
based on django-thumbs (see below).
In fact, this is just django-thumbs without the dumb part replaced with
something reasonable (ie, no cropping of thumbnails)


django-thumbs on-the-fly
https://github.com/madmw/django-thumbs

A fork of django-thumbs 
[http://code.google.com/p/django-thumbs/] 
by Antonio Melé [http://django.es].

"""
import io
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from django.core.files.base import ContentFile
from django.conf import settings
from goatnails.settings import (THUMBS_GENERATE_ANY_SIZE, 
                                THUMBS_GENERATE_MISSING_THUMBNAILS, 
                                THUMBS_GENERATE_THUMBNAILS)
from PIL import Image

def generate_thumb(original, size, format='JPEG'):
    """
    Generates a thumbnail image and returns a ContentFile object with the thumbnail

    Arguments:
    original -- The image being resized as `File`.
    size     -- Desired thumbnail size as `tuple`. Example: (70, 100)
    format   -- Format of the original image ('JPEG', 'PNG', ...) 
                The thumbnail will be generated using this same format.

    """
    original.seek(0)  # see http://code.djangoproject.com/ticket/8222
    image = Image.open(original)
    if image.mode not in ('L', 'RGB', 'RGBA'):
        image = image.convert('RGB')

    thumbnail = image.copy()
    thumbnail.thumbnail(size, Image.ANTIALIAS)

    buff = io.BytesIO()
    if format.upper() == 'JPG':
        format = 'JPEG'
    thumbnail.save(buff, format)
    return ContentFile(buff.getvalue())


class ImageWithThumbsFieldFile(ImageFieldFile):
    """
    Django `ImageField` replacement with automatic generation of thumbnail images.
    See `ImageWithThumbsField` for usage example.

    """

    THUMB_SUFFIX = '%s.%sx%s.%s'

    def __init__(self, *args, **kwargs):
        super(ImageFieldFile, self).__init__(*args, **kwargs)

    def _url_for_size(self, size):
        """Return a URL pointing to the thumbnail image of the requested size.
        If `THUMBS_GENERATE_MISSING_THUMBNAILS` is True, the thumbnail will be created if it doesn't exist on disk.
            
        Arguments:
        size  -- A tuple with the desired width and height. Example: (100, 100)

        """
        if not self:
            return ''
        else:
            # generate missing thumbnail if needed
            fileBase, extension = self.name.rsplit('.', 1)
            thumb_file = self.THUMB_SUFFIX % (fileBase, size[0], size[1], extension)
            if THUMBS_GENERATE_MISSING_THUMBNAILS:
                if not self.storage.exists(thumb_file):
                    try:
                        self._generate_thumb(self.storage.open(self.name), size)
                    except:
                        if settings.DEBUG:
                            import sys
                            print("Exception generating thumbnail")
                            print(sys.exc_info())
            urlBase, extension = self.url.rsplit('.', 1)
            thumb_url = self.THUMB_SUFFIX % (urlBase, size[0], size[1], extension)
            return thumb_url

    def __getattr__(self, name):
        """Return the url for the requested size.

        Arguments:
        name -- The field `url` with size suffix formatted as _WxH. Example: instance.url_100x70

        """
        sizeStr = name.replace("url_", "")
        # fix for change in hasattr() behavior between py2 and py3.
        try:
            width, height = sizeStr.split("x")
        except:
            raise AttributeError("nope")
        requestedSize = (int(width), int(height))
        acceptedSize = None
        if THUMBS_GENERATE_ANY_SIZE:
            acceptedSize = requestedSize
        else:
            for configuredSize in self.field.sizes:
                # FIXME: fuzzy search, accept nearest size
                if requestedSize == configuredSize:
                    acceptedSize = requestedSize
        if acceptedSize is not None:
            return self._url_for_size(acceptedSize)
        raise ValueError("The requested thumbnail size %s doesn't exist" % sizeStr)

    def _generate_thumb(self, image, size):
        """Generates a thumbnail of `size`.
        
        Arguments:
        image -- An `File` object with the image in its original size.
        size  -- A tuple with the desired width and height. Example: (100, 100)

        """
        base, extension = self.name.rsplit('.', 1)
        thumb_name = self.THUMB_SUFFIX % (base, size[0], size[1], extension)
        thumbnail = generate_thumb(image, size, extension)
        saved_as = self.storage.save(thumb_name, thumbnail)
        if thumb_name != saved_as:
            raise ValueError('There is already a file named %s' % thumb_name)

    def save(self, name, content, save=True):
        super(ImageFieldFile, self).save(name, content, save)
        if THUMBS_GENERATE_THUMBNAILS:
            if self.field.sizes:
                for size in self.field.sizes:
                    try:
                        self._generate_thumb(content, size)
                    except:
                        if settings.DEBUG:
                            import sys
                            print("Exception generating thumbnail")
                            print(sys.exc_info())

    def delete(self, save=True):
        if self.name and self.field.sizes:
            for size in self.field.sizes:
                base, extension = self.name.rsplit('.', 1)
                thumb_name = self.THUMB_SUFFIX % (base, size[0], size[1], extension)
                try:
                    self.storage.delete(thumb_name)
                except:
                    if settings.DEBUG:
                        import sys
                        print("Exception deleting thumbnails")
                        print(sys.exc_info())
        super(ImageFieldFile, self).delete(save)

    def generate_thumbnails(self):
        """
        """
        if self.field.sizes:
            for size in self.field.sizes:
                try:
                    self._generate_thumb(self.storage.open(self.name), size)
                except:
                    if settings.DEBUG:
                        import sys
                        print("Exception generating thumbnail")
                        print(sys.exc_info())

    def thumbnail(self, widthOrSize, height=None):
        """
        Return the thumbnail url for an specific size. The same thing as url_[width]x[height] without the magic.

        Arguments:
        widthOrSize -- Width as integer or size as tuple.
        height      -- Height as integer. Optional, will use `widthOrSize` as height if missing.

        Usage:
        instance.thumbnail(48, 48)
        instance.thumbnail(64)
        instance.thumbnail( (100, 70) )

        """
        if type(widthOrSize) is tuple:
            size = widthOrSize
        else:
            if height is None:
                height = widthOrSize
            size = (widthOrSize, height)
        return self.__getattr__('url_%sx%s' % (size[0], size[1]))


class ImageWithThumbsField(ImageField):
    """
    Usage example:
    ==============
    photo = ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,200),)
    
    To retrieve image URL, exactly the same way as with ImageField:
        my_object.photo.url
    To retrieve thumbnails URL's just add the size to it:
        my_object.photo.url_125x125
        my_object.photo.url_300x200
    
    Note: The 'sizes' attribute is not required. If you don't provide it,
    ImageWithThumbsField will act as a normal ImageField
        
    How it works:
    =============
    For each size in the 'sizes' atribute of the field it generates a
    thumbnail with that size and stores it following this format:
    
    available_filename.[width]x[height].extension

    Where 'available_filename' is the available filename returned by the storage
    backend for saving the original file.
    
    Following the usage example above: For storing a file called "photo.jpg" it saves:
    photo.jpg          (original file)
    photo.125x125.jpg  (first thumbnail)
    photo.300x200.jpg  (second thumbnail)
    
    With the default storage backend if photo.jpg already exists it will use these filenames:
    photo_.jpg
    photo_.125x125.jpg
    photo_.300x200.jpg
    
    Note: django-thumbs assumes that if filename "any_filename.jpg" is available
    filenames with this format "any_filename.[widht]x[height].jpg" will be available, too.
    
    """
    attr_class = ImageWithThumbsFieldFile

    def __init__(self, verbose_name=None, name=None, width_field=None, height_field=None, sizes=None, **kwargs):
        self.verbose_name = verbose_name
        self.name = name
        self.width_field = width_field
        self.height_field = height_field
        self.sizes = sizes
        super(ImageField, self).__init__(**kwargs)
