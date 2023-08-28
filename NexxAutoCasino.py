# (C) Copyright 2023 - @sunmods
# scope: hikka_only
# meta developer: @sunmods

from telethon import types 
from .. import loader, utils 
from typing import * 
import asyncio 
 
@loader.tds 
class NexxCasinoMod(loader.Module): 
    'Автоматическая игра в @NexxRevengeBot' 
 
    strings = { 
        'name':'NexxCasino' 
    } 
     
    start: int = 0 
    last: int = 0 
    loses: int = 0 
    is_started: bool = False 
    bot: str = '@NexxRevengeBot' 
    bot_id: int = 5837228831
     
    async def gstartcmd(self, m: types.Message): 
        '<сумма> - начать с суммой ставки' 
        args: str = utils.get_args_raw(m) 
        if self.is_started: 
            return await utils.answer(m, '🙃 Уже запущён! Для остановки введи <code>.gstop</code>') 
        try: 
            self.last = int(args) 
            self.start = int(args) 
            self.loses = 0 
        except: 
            return await utils.answer(m, 'Введи корректное число') 
        self.is_started = True 
        await m.client.send_message(self.bot, "казино {} ".format(self.start)) 
        await utils.answer(m, '✅ <b>Автоигра успешно запущено! Начальная ставка:</b> <code>{}</code>'.format(self.start)) 
 
    async def gstopcmd(self, m: types.Message): 
        '.gstop - остановить казино' 
        if not self.is_started: 
            return await utils.answer(m, '❌ <b>Не запущено! Используй:</b> <code>.gstart <сумма></code>') 
        self.is_started = False 
        await utils.answer(m, '⛔ <b>Остановлено успешно!</b>') 
     
    async def watcher(self, m: types.Message): 
        if not isinstance(m, types.Message): 
            return 
        if not hasattr(m.peer_id, 'user_id'): 
            return 
        chat = m.peer_id.user_id 
        if chat == self.bot_id and not m.out and self.is_started: 
            if 'вы поставили' in m.raw_text: 
                await asyncio.sleep(4) 
                self.loses = 0 
                self.last = self.start 
                await m.client.send_message(self.bot, "казино {} ".format(self.last)) 
            elif 'остаются' in m.raw_text: 
                await asyncio.sleep(4) 
                self.loses = 0 
                await m.client.send_message(self.bot, "казино {} ".format(self.last)) 
            elif 'вы проиграли' in m.raw_text or 'проиграли' in m.raw_text: 
                await asyncio.sleep(4) 
                if self.loses >= 15: 
                    self.loses = 0 
                    self.last = self.start 
                else: 
                    self.last *= 3
                    self.loses += 1 
                await m.client.send_message(self.bot, "казино {} ".format(self.last)) 
            elif 'Путин, у вас не достаточно денег!' in m.raw_text: 
                await asyncio.sleep(4) 
                self.last = self.start 
                self.loses = 0 
                await m.client.send_message(self.bot, "казино {} ".format(self.last))
