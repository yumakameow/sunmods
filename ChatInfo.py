# (C) Copyright 2023 - @sunmods
# meta developer: @sunmods

from .. import loader, utils
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime


def register(cb):
    cb(ChatInfoMod())

class ChatInfoMod(loader.Module):
    """Показывает информацию о чате."""
    strings = {'name': 'ChatInfo'}

    async def chatinfocmd(self, message):
        """Используй .chatinfo <ID; Ничего>"""
        args = utils.get_args_raw(message)

        try:
            chat = await message.client.get_entity(args if not args.isdigit() else int(args))
        except:
            if not message.is_private:
                chat = await message.client.get_entity(message.chat_id)
            else:
                return await message.edit("<emoji document_id=5843702098864116098>🚫</emoji> <code>Это не чат!</code>")

        chat = await message.client(GetFullChannelRequest(chat.id))

        await message.edit("<emoji document_id=5841359499146825803>⌨️</emoji> <code>Загрузка информации...</code>")

        caption = await get_info(chat, message)
        
        await message.client.send_message(message.chat_id, str(caption), file=await message.client.download_profile_photo(chat.full_chat.id, "chatphoto.jpg"))
        
        await message.delete()


async def get_info(chat, message):
    chat_obj_info = await message.client.get_entity(chat.full_chat.id)
    chat_title = chat_obj_info.title
    try:
        msg_info = await message.client(
            GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1),
                              add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception:
        msg_info = None

    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Удалённый аккаунт"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restrcited_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    users_online = 0
    async for i in message.client.iter_participants(message.chat_id):
        if isinstance(i.status, UserStatusOnline):
            users_online = users_online + 1
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info
    bots = 0
    slowmode = "Да" if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else "Нет"
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = "Да" if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted else "Нет"
    verified = "Да" if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else "Нет"
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None

    if admins is None:
        try:
            participants_admins = await message.client(
                GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                       offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception:
            pass
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = f"<emoji document_id=5418133868475587618>🧐</emoji> <b>Информация о чате <code>{chat_title}</code>:</b>\n\n"
    caption += f"<b>ID:</b> {chat_obj_info.id}\n"
    if chat_title is not None:
        caption += f"<b>Название группы:</b> {chat_title}\n"
    if former_title is not None:
        caption += f"<b>Предыдущее название:</b> <code>{former_title}</code>\n"
    if username is not None:
        caption += f"<b>Тип группы:</b> Публичный\n"
        caption += f"<b>Линк:</b> {username}\n"
    else:
        caption += f"<b>Тип группы:</b> Приватный\n"
    if creator_username is not None:
        caption += f"<b>Создатель:</b> <code>{creator_username}</code>\n"
    elif creator_valid:
        caption += f"<b>Создатель:</b> <code><a href=\"tg://user?id={creator_id}\">{creator_firstname}</a></code>\n"
    if created is not None:
        caption += f"<b>Создан:</b> {created.date().strftime('%b %d, %Y')} - {created.time()}\n"
    else:
        caption += f"<b>Создан:</b> {chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}\n"
    if messages_viewable is not None:
        caption += f"<b>Видимые сообщения:</b> {messages_viewable}\n"
    if messages_sent:
        caption += f"<b>Всего сообщений:</b> <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"<b>Всего сообщений:</b> <code>{messages_sent_alt}</code>\n"
    if members is not None:
        caption += f"<b>Участников:</b> <code>{members}</code>\n"
    if admins is not None:
        caption += f"<b>Админов:</b> <code>{admins}</code>\n"
    if bots_list:
        caption += f"<b>Ботов:</b> <code>{bots}</code>\n"
    if users_online:
        caption += f"<b>Сейчас онлайн:</b> <code>{users_online}</code>\n"
    if restrcited_users is not None:
        caption += f"<b>Ограниченных пользователей:</b> {restrcited_users}\n"
    if banned_users is not None:
        caption += f"<b>Забаненных пользователей:</b> {banned_users}\n"
    if group_stickers is not None:
        caption += f"<b>Стикеры группы:</b> <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a>\n"
    caption += "\n"
    caption += f"<b>Слоумод:</b> <code>{slowmode}</code>"
    if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
        caption += f", {slowmode_time} секунд\n"
    else:
        caption += "\n"
    caption += f"<b>Ограничен:</b> {restricted}\n"
    if chat_obj_info.restricted:
        caption += f"> Платформа: {chat_obj_info.restriction_reason[0].platform}\n"
        caption += f"> Причина: {chat_obj_info.restriction_reason[0].reason}\n"
        caption += f"> Текст: {chat_obj_info.restriction_reason[0].text}\n\n"
    else:
        caption += ""
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += "<b>Скам</b>: да\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"<b>Верифицирован:</b> {verified}\n\n"
    if description:
        caption += f"<b>Описание:</b> \n\n<code>{description}</code>\n"
    return caption
