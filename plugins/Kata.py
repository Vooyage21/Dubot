
"""
◈ Perintah Tersedia

•`{i}smgt`

•`{i}ywc`

•`{i}jamet`

•`{i}pp`

•`{i}dp`

•`{i}sed`

•`{i}so`

•`{i}nb`

•`{i}met`

•`{i}war`

•`{i}wartai`

•`{i}kismin`

•`{i}ded`

•`{i}sokab`

•`{i}gembel`

•`{i}cuih`

•`{i}dih`

•`{i}gcs`

•`{i}skb`

•`{i}virtual`
    Cobain aja sendiri.
"""

import string
from time import sleep
from . import (
    eor,
    kazu_cmd,
)

@kazu_cmd(pattern="Tt$")
async def _(event):
    xx = await event.eor("Aku")
    sleep(3)
    await xx.edit("Cuma Mau Bilang")
    sleep(2)
    await xx.edit("Kalo Dante Itu...")
    sleep(1)
    await xx.edit("Setia Mhehe")


# Create by myself @localheart


@kazu_cmd(pattern="smgt$")
async def _(event):
    xx = await event.eor("Lah kok nyerah??")
    sleep(3)
    await xx.edit("jangan nyerang Dong:' kan ada aku")
    sleep(1)
    await xx.edit("yang selalu buat kamu semangat umm")


# Create by myself @localheart


@kazu_cmd(pattern=r"ywc$")
async def _(event):
    await event.client.send_message(
        event.chat_id, "Ok bawang", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@kazu_cmd(pattern="jamet$")
async def _(event):
    xx = await event.eor("WOII")
    sleep(1.5)
    await xx.edit("JAMET")
    sleep(1.5)
    await xx.edit("CUMA MAU BILANG")
    sleep(1.5)
    await xx.edit("GAUSAH SO ASIK")
    sleep(1.5)
    await xx.edit("EMANG KITA KENAL?")
    sleep(1.5)
    await xx.edit("GAUSAH REPLY JUGA")
    sleep(1.5)
    await xx.edit("KITA KAGAK KENAL")
    sleep(1.5)
    await xx.edit("GASUKA BANYAK TINGKAH")
    sleep(1.5)
    await xx.edit("BOCAH KAMPUNG")
    sleep(1.5)
    await xx.edit("BOCAH KAGAK ADA ORANG TUA")
    sleep(1.5)
    await xx.edit("CUIH.")


@kazu_cmd(pattern="pp$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA JELEK NYA MUKA LU!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="dp$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()

    
@kazu_cmd(pattern="ra$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "Dante Userbot Active!",
        reply_to=event.reply_to_msg_id,
    )
    
@kazu_cmd(pattern="Dante$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Mmuuaahh🥹**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()
    

@kazu_cmd(pattern="so$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="nb$")
    await event.client.send_message(
        event.chat_id,
        "VIRTUAL VIRTUAL TAIK ANJING, MENDING NIKAH BLOK INI KAGAK ADA KEPASTIAN MASIH AJA MAU BLOK",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="met$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "CAPER SANA SINI BUAT CARI NAMA BOCAH AMPAS",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="war$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN MANA PENGANGGURAN LAGI CUIH",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="wartai$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="kismin$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="Az$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "P ADU NASIP?",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="sokab$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "SOKAB BET LU, EMG KITA KENAL??!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="gembel$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="cuih$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="dih$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern=r"gcs$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await event.eor(
            event, "Perintah ini Dilarang digunakan di Group ini"
        )
    await event.client.send_message(
        event.chat_id,
        "GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="skb$")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@kazu_cmd(pattern="virtual$")
async def _(event):
    xx = await event.eor("CIEEE YG VIRTUAL")
    sleep(1.5)
    await xx.edit("UDAH TAU VIRTUAL")
    sleep(1.5)
    await xx.edit("MASIH AJA SETIA GOBLOKKK KAN SAKIT KAN THOLOL")
    sleep(1.5)
    await xx.edit("TERUS GALAU DIMANA MANA, SADAR GOBLOK")
    sleep(1.5)
    await xx.edit("LU CUMA JADI TEMPAT DIA KESEPIAN AJA")
    sleep(1.5)
    await xx.edit("JADI SADAR DIRI DEK DEKKK")
    sleep(1.5)
    await xx.edit("APALAGI DENGAR OMONGAN MANIS")
    sleep(1.5)
    await xx.edit("BHAHAHAHA")
    sleep(1.5)
    await xx.edit("KAN TOLOLL KALAU MASIH AJA PERCAYA VIRTUAL - VIRTUAL")
    
    
