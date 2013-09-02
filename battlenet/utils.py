import unicodedata
import urllib.request, urllib.parse, urllib.error


def normalize(name):
    if not isinstance(name, str):
        name = name.decode('utf8')

    return unicodedata.normalize('NFKC', name).encode('utf8')


def quote(name):
    return urllib.parse.quote(normalize(name))


def make_icon_url(region, icon, size='large'):
    if not icon:
        return ''

    if size == 'small':
        size = 18
    else:
        size = 56

    return 'http://%s.media.blizzard.com/wow/icons/%d/%s.jpg' % (region, size, icon)


def make_connection():
    if not hasattr(make_connection, 'Connection'):
        from .connection import Connection
        make_connection.Connection = Connection

    return make_connection.Connection()
