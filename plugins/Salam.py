# @riizzvbss
"""
Perintah Tersedia

• `{i}ass`
   Salam Lengkap

• `{i}as`
   Assalamu'alaikum

• `{i}ws`
   Jawab Salam
   
• `{i}ks`
   Kenalan Salam
   
• `{i}jws`
   Istighfar Salam
   
• `{i}3x`
    Bisa Kali

• `{i}kg`
    Keren lu gitu

• `{i}hm`
    Batuk
"""

from time import sleep
from . import (
    eor,
    kazu_cmd,
)

@kazu_cmd(pattern="ass$")
async def _(event):
    await event.eor("**Assalamu'alaikum Warohmatulohi Wabarokatu**")


@kazu_cmd(pattern="as$")
async def _(event):
    await event.eor("**Assalamu'alaikum**")
    
@kazu_cmd(pattern="ws$")
async def _(event):
    await event.eor("**Wa'alaikumussalam**")

    
@kazu_cmd(pattern="ks$")
async def _(event):
    xx = await event.eor("**Hy kaa 🥹**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@kazu_cmd(pattern="jws$")
async def _(event):
    xx = await event.eor(event, "**Astaghfirullah, Jawab dulu salam dong**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum**")


@kazu_cmd(pattern="3x$")
async def _(event):
    xx = await event.eor("**Bismillah, 3x**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum Bisa yug Kali**")
    
@kazu_cmd(pattern="kg$")
async def _(event):
    xx = await event.eor("**Lu kenapa Begitu ?**")
    sleep(2)
    await xx.edit("**Keren Lu Begitu ?**")

@kazu_cmd(pattern="hm$")
async def _(event):
    xx = await event.eor("**Batuk dulu g sih**")
    sleep(2)
    await xx.edit("**Biar ludah batuk nya gw ludahin ke wajah lu!**")
