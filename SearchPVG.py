# (C) Copyright 2023 - @sunmods
# meta developer: @sunmods
# scope: hikka_only

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import Message

from .. import loader, utils


class SearchPVGMod(loader.Module):
    """Search videos, pics, games via inline bots"""

    strings = {"name": "SearchPVG", "res": "<b>Result</b>"}
    string_ru = {"res": "<b>Результат</b>"}

    async def piccmd(self, event):
        "<pic name> - search pic"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("pic", args)
        await result[0].click(event.to_id)
        await event.edit(self.strings("res"))

    async def vidcmd(self, event):
        "<video name> - search video"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("vid", args)
        await result[0].click(event.to_id)
        await event.edit(self.strings("res"))

    async def gamecmd(self, event):
        "<game name> - search game"
        args = utils.get_args_raw(event)
        result = await event.client.inline_query("gamee", args)
        await result[0].click(event.to_id)
        await event.edit(self.strings("res"))
