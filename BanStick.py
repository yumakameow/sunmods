# (C) Copyright 2023 - SunModules
# License - GNU APGL V3

from .. import loader, utils


class BanStickMod(loader.Module):
    """Блокирует стикеры/гифы в чате."""

    strings = {"name": "BanStick"}

    async def client_ready(self, client, db):
        self.db = db

    async def banstickcmd(self, message):
        """Используй: .banstick чтобы заблокировать стикер или гифку в чате; аргументы clear или clearall (по желанию)"""
        banned = self.db.get("BanMedia", "banned", {})
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        chat = str(message.chat_id)
        try:
            if args == "clear":
                banned.pop(chat)
                self.db.set("BanMedia", "banned", banned)
                return await message.edit(
                    "<b>Теперь все стикеры или гиф разрешены в этом чате.</b>"
                )
        except:
            return await message.edit("<b>Что то пошло по пизде :/</b>")
        try:
            if args == "clearall":
                self.db.set("BanMedia", "banned", {})
                return await message.edit(
                    "<b>Теперь все стикеры или гиф разрешены во всех чатах.</b>"
                )
        except:
            return await message.edit("<b>Что то пошло не так :/</b>")
        if not reply:
            return await message.edit("<b>Нету реплая.</b>")
        elif not reply.media:
            return await message.edit("<b>Это не файл.</b>")
        try:
            if reply.media:
                docid = (reply.document).id
                if chat not in banned:
                    banned.setdefault(chat, [])
                if str(docid) not in banned[chat]:
                    banned[chat].append(str(docid))
                    self.db.set("BanMedia", "banned", banned)
                    await message.edit(
                        "<b>Теперь этот гиф или стикер запрещён в этом чате!</b>"
                    )
                else:
                    banned[chat].remove(str(docid))
                    if len(banned[chat]) == 0:
                        banned.pop(chat)
                    self.db.set("BanMedia", "banned", banned)
                    await message.edit(
                        "<b>Теперь этот гиф или стикер разрешён в этом чате.</b>"
                    )
        except:
            return await message.edit("<b>Что то пошло по не так :/</b>")

    async def watcher(self, message):
        try:
            banned = self.db.get("BanMedia", "banned", {})
            chat = str(message.chat_id)
            me = await message.client.get_me()
            if chat not in str(banned):
                return
            r = banned[chat]
            for i in r:
                docid = (message.document).id
                if docid == int(i):
                    if message.sender_id == me.id:
                        return
                    else:
                        await message.client.delete_messages(
                            message.chat_id, message.id
                        )
        except:
            pass
