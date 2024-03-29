
import re

from . import (
    Button,
    danteConfig,
    callback,
    get_back_button,
    get_languages,
    get_string,
    udB,
)


@callback("lang", owner=True)
async def setlang(event):
    languages = get_languages()
    tayd = [
        Button.inline(
            f"{languages[ay]['natively']} [{ay.lower()}]",
            data=f"set_{ay}",
        )
        for ay in languages
    ]
    buttons = list(zip(tayd[::2], tayd[1::2]))
    if len(tayd) % 2 == 1:
        buttons.append((tayd[-1],))
    buttons.append([Button.inline("« Back", data="mainmenu")])
    await event.edit(get_string("ast_4"), buttons=buttons)


@callback(re.compile(b"set_(.*)"), owner=True)
async def settt(event):
    lang = event.data_match.group(1).decode("UTF-8")
    languages = get_languages()
    danteConfig.lang = lang
    udB.del_key("language") if lang == "id" else udB.set_key("language", lang)
    await event.edit(
        f"Bahasa Anda telah disetel ke {languages[lang]['natively']} [{lang}].",
        buttons=get_back_button("lang"),
    )
