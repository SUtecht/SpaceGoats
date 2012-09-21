# -*- encoding: utf-8 -*-

from django.conf import settings


# Generate thumbnails when saving objects.
# Default: True
THUMBS_GENERATE_THUMBNAILS = getattr(settings, "THUMBS_GENERATE_THUMBNAILS", True)

# Generate thumbnail when its url is accessed and the the file doesn't exist.
# Set this option when you are replacing ImageField with ImageWithThumbsField on a populated database where the thumbnails doesn't exist.
# Default: True
THUMBS_GENERATE_MISSING_THUMBNAILS = getattr(settings, "THUMBS_GENERATE_MISSING_THUMBNAILS", True)

# Generate the thumbnail even if it's not in the configured `sizes` argument.
# Default: False
THUMBS_GENERATE_ANY_SIZE = getattr(settings, "THUMBS_GENERATE_ANY_SIZE", False)
