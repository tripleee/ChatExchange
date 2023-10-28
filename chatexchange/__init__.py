from . import browser

from . import users
from . import messages
from . import rooms
from . import events
from . import client
from .version import __version__


Browser = browser.Browser

Client = client.Client

__all__ = [
    'browser', 'users', 'messages', 'rooms', 'events', 'client',
    'Browser', 'Client']
