# (C) Copyright 2023 - @sunmods
# meta developer: @sunmods
# scope: hikka_only

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils


class ModuleSearcherMod(loader.Module):
    """search a modules via @ftg2bot"""

    strings = {"name": "ModuleSearcher", "mod": "<b>👇 Probably this module</b>"}
    string_ru = {"mod": "⚡ <b>Вот модуль под названием: {args}</b>"}

    async def modcmd(self, event):
        "<module name>"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("ftg2bot", args)
        await result[0].click(event.to_id)
        await event.edit(self.strings("mod"))
