from AIMXMUSIC.core.bot import DAXX
from AIMXMUSIC.core.dir import dirr
from AIMXMUSIC.core.git import git
from AIMXMUSIC.core.userbot import Userbot
from AIMXMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DAXX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
