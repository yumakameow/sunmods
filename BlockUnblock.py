# (C) Copyright 2023 - SunModules
# License - GNU APGL V3

# meta developer: @sunmodules

from telethon import functions

from .. import loader, utils


@loader.tds
class BlockUnblockMod(loader.Module):
    """
    Helps you for to add user in blacklist
    """

    strings = {
        "name": "BlockUnblock",
        "blocked": "⛔ <b>{} was blacklisted.</b>",
        "unblocked": "✅ <b>{} removed from the blacklist.</b>",
        "who_to_block": "😾 <b>Indicate, who to block.</b>",
        "who_to_unblock": "⛔ <b>Indicate, who to unblock.</b>",
    }

    def __init__(self):
        self.me = None

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        self.me = await client.get_me(True)

    async def reportcmd(self, message):
        """User report for spam."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if args:
                user = await message.client.get_entity(
                    args if not args.isnumeric() else int(args)
                )
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                return await message.edit("<b>Who I must report?</b>")

        await message.client(functions.messages.ReportSpamRequest(peer=user.id))
        await message.edit("<b>You get report for spam!</b>")

    async def blockcmd(self, message):
        """Use: .block to block this user."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_block"])
                return
        await message.client(functions.contacts.BlockRequest(user))
        await utils.answer(message, self.strings["blocked"].format(user.first_name))

    async def unblockcmd(self, message):
        """Use: .unblock to unblock this user."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_unblock"])
                return
        await message.client(functions.contacts.UnblockRequest(user))
        await utils.answer(message, self.strings["unblocked"].format(user.first_name))
