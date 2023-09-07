# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @sunmodules

from .. import loader, utils
from asyncio import sleep 

class VideoDownloaderMod(loader.Module):
    """Install videos for tiktok or instagram with link"""
    
    strings = {
        "name": "VideoDownloader",
        "yumaka_pls_wait": "🕒 <code>Wait...</code>",
        "yumaka_pls_enter_a_link": "😾 <b>Please provide a link for the video</b>",
        "yumaka_done": "✅ <b>Done!</b>",
        }
    
    strings_ru = {
        "yumaka_pls_wait": "🕒 <code>Пожалуйста подождите...</code>",
        "yumaka_pls_enter_a_link": "😾 <b>Пожалуйста, укажите ссылку на видео</b>",
        "yumaka_done": "✅ <b>Готовo!",
        }
  
    async def videocmd(self, message):
        """> [Link] just enter the link (TikTok, Instagram)"""
        reply = await message.get_reply_message() 
        await utils.answer(message, self.strings("yumaka_pls_wait", message))
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("yumaka_pls_enter_a_link", message))
            return
        r = await message.client.inline_query('saveasbot', args)
        await message.client.send_file(message.to_id, r[1].result.content.url, caption=f"{self.strings('yumaka_done')} | <code>{args}</code>", reply_to=reply.id if reply else None)
        
