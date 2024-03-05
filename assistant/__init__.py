
from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from dante import *
from dante import _dante_cache
from dante._misc import owner_and_sudos
from dante._misc._assistant import asst_cmd, callback, in_pattern
from dante.fns.helper import *
from dante.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = dante_bot.full_name
OWNER_ID = dante_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Ada yang salah`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
