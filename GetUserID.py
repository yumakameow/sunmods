# (C) Copyright 2023 - @sunmods
# meta developer: @sunmods
# scope: hikka_only

from .. import loader, utils


@loader.tds
class GetUserIDMod(loader.Module):
    """Get id for user"""

    strings = {
        "name": "GetUserID",
        "error": "Error!",
        "getid": "{}"
    }
    
    async def getidcmd(self, message):
        """Use: .getid <@ or reply>"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        try:
            user = await message.client.get_entity(
                (
                    args
                    if not args.isdigit()
                    else int(args)
                )
                if args
                else reply.sender_id
                if reply
                else message.sender_id
            )
        except ValueError:
            return await utils.answer(
                message, self.strings["error"])

        return await utils.answer(
            message, f"<b><a href=\"tg://user?id={user.id}\">{self.strings['getid'].format(user.id)}</a></b>")
