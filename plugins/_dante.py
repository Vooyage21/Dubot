
from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, kazu_cmd, eor, get_string

REPOMSG = """
**ᴅᴀɴᴛᴇ ᴜʙᴏᴛ** \n
Owner - [Click Here](https://t.me/Usern4meDoesNotExist404)
Channels - [Click Here](https://t.me/SpotifyStreamMusic)
Support - @SpotifyStream_Id
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://t.me/SpotifyStream_Id"),
        Button.url("Channels", "https://t.me/SpotifyStreamMusic"),
    ],
    [Button.url("Support Group", "t.me/SpotifyStream_Id")],
]

KAZUSTRING = """🎇 **Thanks for Deploying ᴅᴀɴᴛᴇ ᴜʙᴏᴛ!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@kazu_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@kazu_cmd(pattern="kazu$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        KAZUSTRING,
        file="https://mallucampaign.in/images/img_1708341080.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
