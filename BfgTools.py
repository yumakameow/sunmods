from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import time

def register(cb):
    cb(checker())


class BfgTools(loader.Module):
    """Помощь в bfg"""
    strings = {'name': 'BfgTools'}

    async def profilecmd(self, message):
        """Показывает профиль"""
        chat = "@bforgame_bot"
        text = "профиль"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<code>Секунду...</code>")
        async with message.client.conversation(chat) as conv:

            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<code> {response.text} </code> ")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()

    async def sadcmd(self, message):
        """Показывает сад"""
        chat = "@bforgame_bot"
        text = "мой сад"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<code>Секунду...</code>")
        async with message.client.conversation(chat) as conv:

            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<code> {response.text} </code> ")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()

    async def biznescmd(self, message):
        """Показывает бизнес"""
        chat = "@bforgame_bot"
        text = "мой бизнес"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<code>Секунду...</code>")
        async with message.client.conversation(chat) as conv:

            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<code> {response.text} </code> ")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()

    async def fermacmd(self, message):
        """Показывает ферму"""
        chat = "@bforgame_bot"
        text = "моя ферма"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<code>Секунду...</code>")
        async with message.client.conversation(chat) as conv:

            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<code> {response.text} </code> ")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()

    async def balancecmd(self, message):
        """Показывает баланс"""
        chat = "@bforgame_bot"
        text = "б"
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Нет текста или реплая!</b>")
            return
        await message.edit("<code>Секунду...</code>")
        async with message.client.conversation(chat) as conv:

            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1721358063))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("😾 <b>Разблокируй @bforgame_bot</b>")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<code> {response.text} </code> ")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()
      
