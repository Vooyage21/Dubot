# Ported By @disinikazu & @Riizzvbss
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from . import (
     StartTime,
     kazu_cmd,
     DEVLIST,
     eor,
     humanbytes,
     devs_cmd,
     )
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@kazu_cmd(pattern=r"^pink$", incoming=True, from_users=DEVLIST)
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cpink$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await eor(ping, "**🖕**")
    await ping.edit("**🫰**")
    await ping.edit("**⚡**")
    await ping.edit("**🖖**")
    await ping.edit("**🖕**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.edit("⚡")
    sleep(3)
    await ping.edit(
        f"**Dante UBot**\n\n"
        f"**Ping!! :** `%sms`\n"
        f"**UpTime :** `{uptime}` \n"
        f"**Owner :** {user.first_name} (tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="ping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await eor(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**PONG!! 🍭**\n**Ping** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="lping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await eor(ping, "**PING**")
    await lping.edit("**PING**")
    await lping.edit("**PING**")
    await lping.edit("**PING**")
    await lping.edit("**PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"**Ping !!** "
        f"`%sms` \n"
        f"**Uptime -** "
        f"`{uptime}` \n"
        f"**Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="Dping$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await eor(pong, "**P**")
    await kopong.edit("**WOI**")
    await kopong.edit("**⚡**")
    await kopong.edit("**🫰**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**NIH** "
        f"\nDante UBot `%sms` \n"
        f"**Yoo!!** "
        f"\nSalken! Saya {user.first_name} (tg://user?id={user.id})』 \n" % (duration)
    )


# .keping & kping Coded by Koala


@kazu_cmd(pattern=r"Dan$")
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Kaz$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await eor(pong, "✊")
    await kping.edit("🤚")
    await kping.edit("✌️")
    await kping.edit("🖖")   
    await kping.edit("🤟")
    await kping.edit("🖕")
    await kping.edit("**NIH BUAT KAMU**")
    await kping.edit("**SEMUANYA MINGGIR DANTE MAU KASIH KEJUTAN.....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit("🫰")
    sleep(3)
    await kping.edit(
        f"**ᴜʙᴏᴛ ᴅᴀɴᴛᴇ!! 🫰**\n**Ping!!** : %sms\n**Uptime** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await eor(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@kazu_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await eor(pong, "`Assalamualaikum Tuan`")
    await xx.edit("Waalaikumsalam.....")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("Tunggu...")
    sleep(3)
    await xx.edit("**𝙿𝙸𝙽𝙶!**\n`%sms`" % (duration))
