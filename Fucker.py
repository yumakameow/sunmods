# (C) Copyright 2023 - @sunmods
# scope: hikka_only
# meta developer: @sunmods
# edited for @Mersai

from .. import loader, utils

import random
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto


srach = [
    "ТЫ ПОНИМАЕШЬ ЧТО Я ПИЗДАК В ТЕОЙ МАТРЕИ НА СВОЙ ХУЙ КАК МАКАРОНИНУ НАМОТАЛ БЛЯДЬ И НАЧАЛ РАСКРУЧИВАТЬ ЕЁ, ПОСЛЕ ЧЕГО ВЫКИНУЛ В КОСМОС, ЧТОБ ЕЁ ТАМ ИНОПЛАНЕТЯНЫ ХУЯМИ РВАЛИ?)",
    "Пососи мой хуй бездарь.",
    "И что ты мне можешь сделать? рассказать мамке что ты соснул у меня?",
    "Твоя мамка тоже сосала у меня и кстати я твой отчим)",
    "Ты знаешь что я твою маму ебал и ты родился и еще ебал и родился тебе братик)",
    "Соси хуй мой бездарь , чурка ебанная чтобы твою мать ебали 1000-7 негров которых их мам тоже ебали 1000-7 негров.",
    "Нормально общайся с батей",
    "Общайся адекватно с отцом а то я твою маму выебу и тебя с ремьнём)",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ТВОЮ МАТЬ ОТПРАВИЛ СО СВОЕГО ХУЯ В НЕБО, ЧТОБ ОНА СВОИМ ПИЗДАКОМ ПРИНИМАЛА МИТЕОРИТНУЮ АТАКУ?)",
    "ЕСЛИ ТЫ СЕЙЧАС ТАК И БУДЕШЬ ПРОДОЛЖАТЬ ПРОТИВОРЕЧИТЬ МОЕМУ ХУЮ, КАК ИМ КАК БЛЯДЬ НА НЛО ЗАХВОЧУ ТВОЁ ОЧКО И НАЧНУ ОПЫТЫ ПРОВОДИТЬ",
    "ТЫ ПОНИМАЕШЬ ЧТО ТВОЯ МАТЬ МОЙ ХУЙ ЗАВЕРНУЛА В ПАКЕТИК ПОТОМУ ЧТО У ЭТОЙ БОМЖИХИ НЕБЫЛО ДЕНЕГ НА ПРЕЗИКИ, И ПОКЕТИК ПОРВАЛСЯ, И РОДИЛОСЬ ТАКОЕ ХУЙЛО КАК ТЫ",
    "TЫ ПОНИМАЕШЬ ЧТО Я ТВОЮ МАТЬ СЛУЧАЙНО СВОИМ ХУЁМ СМЁЛ НАХУЙ СО СВОЕГО ПУТИ, И ОНА УЛЕТЕЛА НА РАДИУС ОБСТРЕЛА МОЕЙ ЗАЛУПЫ",
    "АМЕБА ЕБАНАЯ СУКА) МАМАШКУ ТВОЮ ДЫРЯВИЛ ЧЕТ ) НАХУЙ ТВОЯ МАМАША КРИЧИТ КОГДА Я НАЧИНАЮ ЕБАТЬ ЕЕ)",
    "АМЕБА ИЛИ ТЫ ОЛЕНЬ?) СЛЫШЬ ЕСЛИ ТЫ ПРОЛЬЕШЬ НА МОЙ ХУЙ СЛЕЗЫ , ТО ТЫ НЕ РАССЧИТЫВАЙ НА ТО , ЧТО ПОТОМ К ТЕБЕ ПРИДЕТ ФЕЯ И ПООБЕЩАЕТ ТЕБЕ ДОЛГУЮ И СЧАСТЛИВУЮ ЖИЗНЬ)",
    "ОЛЕНЬ ТЫ ЕБАНЫЙ) МАТЬ ТВОЮ ЕБУ ЧЕТ ) ДАВАЙ ТЫ ЩАС ВОЗЬМЕШЬ МОЙ ХУЙ КАК ПЕРО И СЛОВНО КАК ПИСАТЕЛЬ СЕРЕБРЯНОГО ВЕКА НАПИШЕШЬ КАКОЙ НИБУДЬ РОМАН КОТОРЫЙ БУДЕТ ПО РАЗМЕРУ ПРИМЕРНО КАК МАСТЕР И МАРГАРИТА )",
    "твоя мамка блядоебская кобыла и лезби",
    "у тебя мать сраная шлюха",
    "Я ТОВЮ МАМАШУ СВОИМ ХУЁМ РАСПЛЮЩИЛ, И ТЕПЕРЬ ОНА КАК ХОЯЧАЮ ПРУЖИТНКА БЛЯДЬ, ОТ СЕБЯ ВСЕ ХУИ ОТТАЛКИВАЕТ КРОМЕ МОЕГО, ДЛЯ МОЕГО ХУЯ ВСЕГДА ОТКРЫТ ДОСТУП В ЕЁ ПИЗДАК",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ТВОЮ МАТЬ БЛЯДЬ НАТЯНУЛ ПИЗДАКОМ НА ВЫСОКОВОЛЬТНУЮ ЭЛЕКТРО ВЫШКУ, И ОНА В СЕБЯ НАХУЙ ВЕСЬ ТОК ВТЯНУЛА, ТЕПЕРЬ ОНА БЛЯДЬ КАК ЭЛЕКТРО",
    "Я КОГДА ВЫЕБАЛ ТВОЮ МАТЬ Я СВОЙ ХУЙ ПОСТАВИЛ К ЕЁ УХУ, ЧТОБ ОНА СЛЫШАЛА ПРИБОЯ СПЕРМЫ, А ПОТОМ ОНА ШИРОКО РАСКРЫЛА РОТ  МЫ В ЕЁ ЕБЛЯТНИКЕ УСТРОИЛИ ОКЕАН",
    "ТЫ ПОНИМАЕШЬ ЧТО Я В ПИЗДАК ТВОЕЙ МАТРЕИ СВОЙ ХУЙ ЗАСУНУ КАК БЛЯДЬ ШТТЕККЕР И ЕЁ ЗАРЯД ПОВЫСИЛСЯ КАК ОТ ЭНЕРГЕТИКА)",
    "ТЫ ПОНИМАЕШЬ ЧТО ТВОЯ МАТЬ НА МОЁМ ХУЮ УСТРОИЛА БЛЯДЬ ТАНЦПОЛ, И НАЧАЛА СВОИМ ПОДРУГАМ ПРОДАВАТЬ НА НЕГО БИЛЕТЫ",
    " ЕСЛИ ТЫ СЕЙЧАС НЕ НАЧНЁШЬ МНЕ ОТВЕЧАТЬ, Я ТЕБЕ НАХУЙ ХЁМ ПАЛЬЦЫ ПЕРЕЛОМАЮ, ОБРАЗИНА ТЫ ЕБАНАЯ)",
    "ТЫ ПОНИМАЕШЬ ЧТО ВТОЯ МАМАШКА КАШЁЛКА ЕБАНАЯ, НА МОЙ ХУЙ ВЕШАЕТСЯ СВОИМ ПИЗДАКОМ КАК МАГНИТИК НА ХОЛОДИЛЬНИК, ПИДОПР ТЫ БЛЯДЬ ЕБАНЫЙ",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ТВОЕЙ МАТЕРИ ГОЛОВУ ХУЁМ КАК КОПЬЁМ ПРОБИЛ БЛЯДЬ И ЕЁ КУРИНЫЙ МОЗГ УМЕР НАХУЙ)) ИЗ-ЗА ЭТОГО ОНА ТЕБЯ ДАЖЕ И НЕ ВСПОМИНАЕТ)",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ВЫСТАВИЛ СВОЙ ХУЙ НА АВИТО, А ТВОЯ МАТЬ ПРОШЛА БЛЯДЬ БЕЗ ОЧЕРЕДИ И ККУПИЛА ЕГО, ОТДАВ СВОЮ ГНИЛУЮ ПОЧКУ?)",
    "ТЫ ПОНИМАЕШЬ ЧТО ТВОЯ МАТЬ МОЙ ХУЙ НА НОЧЬ СЕБЕ В ПИЗДАК СУЁТ КАК ОБОГРЕВАТЕЛЬ НАХУЙ?)",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ПОКА ЧТО ЕБАЛ ТВОЮ МАМАШУ В СРАКУ, У НЕЁ ТАМ ЗАСОР СПЕРМЫ БЛЯДЬ ОБРАЗОВАЛСЯ И ЗАСОХ, ТЕПЕРЬ ОНА СРАТЬ НОРМАЛЬНО НЕ МОЖЕТ, ИДИ НАХУЙ СПАСАЙ ЭТУ ШЛЮХУ",
    "ТЫ ПОНИМАЕШЬ ЧТО КОГДА Я ЕБУ ТВОЮ МАТЬ ЧТОБЫ ОНА НЕ ОРАЛА Я ЕЙ КЛЯП В РОТ СУЮ, НО ОДИН РАЗ СЛУЧИЛОСЬ ТАКОЕ, ЧТО КОГДА Я СВОИМ ХУЁМ ДАЛ ЕЙ ПО ПИЗДЕ ОНА ЭТОТ КЛЯП ПРОГЛАТИЛА, И НАЧАЛА ЗАДЫХАТЬСЯ, СПАСИ СВОЮ ШЛЮХА МАМКУ)",
    "ТЫ ПОНИМАЕШЬ ЧТО МОЙ ХУЙ ВЗЛАМЫВАЕТ ОЧКО ТВОЕЙ МАТЕРИ КАК СЕЙФ НАХУЙ, И ОТ ТУДА НАЧИНАЮТ ВАЛИТЬСЯ САМОРОДКИ СПЕРМЫ?)",
    "ТЫ ПОНИМАЕШЬ ЧТО Я В ПИЗДАКЕ ТВОЕЙ МАТЕРИ УСТРОИЛ ИЗВЕРЖЕНИЕ СВОЕГО ХУЯ НАХУЙ?",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ХУЁМ НАЧАЛ МОТАТЬ ПЕРЕД ТВОИМ ЕБАЛОИ И ТЕБЯ СЛУЧАЙНО НАХУЙ ЗАГИПНОТЕЗИРОВАЛ, И ТЫ ОБ ХУИ СТАЛ ГОЛОВОЙ БИТЬСЯ?)",
    "ТЫ ПОНИМАЕШЬ ЧТО КОГДА Я ТВОЮ МАТЬ ОНА КАК ШЛЮХА ЛОЖИТСЯ НА СПИНКУ И НАЧИНАЕТ ПОСАСЫВАТЬ МОИ ЯЙЦА",
    "ТЫ ПОНИМАЕШЬ ЧТО Я В ПИЗДАКЕ ТВОЕЙ МАТЕРИ ИЗ ЕЁ КЛИТОРНЫЙ СТЕН ВЫРЕЗАЮ РАКЕТНИЦУ СВОИМ ХУЁМ?",
    "Я СЕЙЧАС СВОЕЙ СПЕРМОЙ ОБОЛЬЮ ТВОЙ ПИЗДАК КАК КЕРАСИНОМ, И ПУЩУ НА НЕГО ИСКРУ, ДОБЫТАЯ КОТОРАЯ БУДЕТ О ТВОИ ГНИЛЫЕ ЗУБКИ, И ТЫ СГОРИШЬ НАХУЙ)",
    "ТЫ ПОНИМАЕШЬ ЧТО ТЫ ОТ МОЕЙ ЗАЛУПЫ ПРЯЧШЬСЯ В ПИЗДАКЕ СВОЕЙ МАТЕРИ КАК НАХУЙ В БУНКЕРЕ, А Я СВОИМ ХУЁМ ЕГО НА СКВОЗЬ ПРОШИЛ И ТЕБЕ В ЕБАЛО ПОПАЛ)) ",
    "ТЫ ПОНИМАЕШЬ ЧТО Я ХУЁМ СТАЛ КАТАЛИЗИРОВАТЬ ПИЗДАК ТВОЕЙ МАТЕРИ НА РАЗДВИЖЕНИЕ ЕЁ ЖИРНЫХ НОГ?)",
    "пошел нахуй",
    "всоси хуяку",
    "хуяру зажуй",
    "мать те ебал",
    "твою мамашу поебем",
    "закрой рыло своё сын шлюхи",
    "хуяру зажуй тебе сказали ты чё тупого из себя строишь",
    "я твою маму ебал сынка шлюхи кривоёблого",
    "ты здесь мою залупу отсосёшь",
    "я твоё ебало щас разложу здесь и каждый будет проходить и об тебя ноги вытирать сынка проститутки такого",
    "я твою маму ебал криворукого сынка проститутки бля ахаха",
    "че замолк идиот ебаный мать те ебём",
    "тебе рот отьёб",
    "сынка шлюхи тебя выебут",
    "поймай член ебалом чунга чанга ты ебаная",
    "ебало в залупу втопи",
    "твоя мать шлюха соберись давай с силами идиот ебаный и придумай хоть какие то слова сын шлюхи зашуганный",
    "иди нахуй отсюда говорю сынок проститутки пока я и тебе ебало нахуй не снес своей залупой ахаха",
    "отсосешь",
    "слитый сын шлюхи соси",
    "в соло всей конфе хуи до блеска соси блядина слабая",
    "ку сосёшь слабак криворукий",
    "член мой на вкус попробуй сын шлюхи тебе он на всю жизнь запомнится тут придурок ебаный блять ахахаха",
    "грязный хуй соси",
    "член выжуй огромный",
    "поебут твою свиноматерь",
    "пососешь мне шалава черномазая",
    "блядина черная соси тут",
    "сынок шлюхи черный соси",
    "ускоглазый сынок шлюхи соси тут",
    "дырявый сын шлюхи соси давай",
    "в очко прими долбоёб ебучий",
    "усама бен ладен ты ебаный отсоси тебе сказали",
    "отсоси мне тут улитка ебучая",
    "твою мамашу поебём слоупок ты ебаный",
    "бери хуище в рот",
    "истеричка ебаная отсоси чё",
    "блядина истеричная соси",
    "доброе утро хуй на",
    "здарова чё сосёшь мне",
    "слитый сын шлюхи соси",
    "чё молчишь мать ебём те",
    "поебут мамашу те",
    "на член вафлер ебучий",
    "ну че соси",
    "чё сосёшь тут молча шлюха ебучая",
    "ку твою мать ебал спящий ты сынок проститутки",
    "хуяру высоси сынок блядины",
    "сынка шлюхи порванного тебя ебём",
    "шлюха дрочи мне сиськами своими",
    "грызи хуище",
    "твой рот отъеб",
    "пососи блядина жирноеблая",
    "твою мамашу поебем Чингиз ебаный ты",
    "подрочи хуй своими сиськами шлюха ты черная",
    "пожуй член",
    "ебальник закрой и соси тут сын шлюхи",
    "пососи шалава криворукая",
    "пососи блядье",
    "твою рожу еб",
    "твою маму ёб",
    "маму те ёб",
    "рыло те ебём",
    "всем хуй пососи",
    "те рот выебли шлюхе",
    "твою мать на хую выношу вместо носилок",
    "ты пидорас",
    "всем селом тебя негры ебали",
    "ниже отпиши если твоя мать шлюха",
    "сосу хуй в теле твоей мамаши, в хуй спиздани ниже",
    "при помощи души твоего отца, я убил твою мать мелким хуем твоего отца, и после чего расчленил на маленькие кусочки",
    "докажи что твоя матуха шлюха любым сообщением ниже",
    "пересоси",
    "чососи",
    "при помощи души твоего отца я убил твою мамашу шлюху и после чего я отдал ее мертвое тело хачам за пачку сигарет",
    "убейся об мой хуй ниже",
    "давай ты всей конфе докажешь что ты мой фанат, просто отпиши ниже любое сообщение",
    "ты же ебаный фанатик моего хуя)) просто признай, что всосал мне анскильный ты хуесос я тя ебу словами как и твою матуху ниже кстати убейся об залупу",
    "ты тупоголовый сельский житель, переставай уже провацировать мой хуй на еблю твоей мамаши",
    "ты знаешь какие отличия между твоей мамашей и хуем хача? Они незаменимы",
    "добей свою матуху сообщением ниже, а то она уже не может сосать мне хуй",
    "всоси ниже текстом",
    "я тя парой слов ебу, пока ты потеешь мне в залупу",
    "воздух = мой член, дыши глубже",
    "чопапе в залупу спизданул?",
    "с какими словами я убил твою матуху, отпиши ниже",
    "ты потный хряк, соси ниже словами",
    "ХАХАХАХАХ бездарный хуесос я же тя парочкой слов выебу пока ты текста будешь сочинять тупоголовый деревенский житель продолжай фанатеть от моей залупы",
    "ты обрыганый сын московского бомжа",
    "с какими словами твоя мамаша сосала?",
    "взял хуй в рот, он сказал:",
    "я украл твою душу, дабы незаметно убить твою мать шлюху когда она будет ебаться с хачами в соседней комнате кстати в хуй че спизданешь?",
    "ублюдощный хуесос, твои текста сразу идут мне в залупу старайся лучше",
    "Мой хуй для твоей мамы как спайдерман,по ночам по крышам лазит до нее,а твой отец думает что за шумы <у моей жены в комнате> а там я ее ебу)",
    "с этой провокацией на тебя кончал твой брат а ты что зеркалу орал?",
    "с этой провокацией твоя мать ебала тебя страпаном в анал ,а ты что ей орал когда хуй отца досасывал?",
    "с этой провокацией тебя добили хачи, а ты слизывал у них с залупы кончу и что отцу орал?",
    "с этой провокацией ты вылизал клитор сестре, а та обоссала твое ебло и что тебе ответила после члена моего?",
    "с этой провокацией твой отец кончал  на твою сестру а ты слизывал кончу и что зеркалу орал?",
    "с этой провокацией твоя мать заглатывала мой член как питон, а ты что отцу орал когда хуй бомжа  всасывал?",
    "с этой провокацией ты откусил клитор своей матери ,а та обоссала тебя и  что тебе крикнула?",
    "с этой провокацией твой отец прищимил твой хуй дверью, а ты укусил его за залупу и что ему крикнул?",
    "с этими словами я твою мать в подвале ебал, а ты сосал член моему псу и что отцу своему орал?)",
    "с этими словами ты ебал собак, а твоя мать облизывала мне яйца и что тебе орала?)",
    "Лол, меня пригласили в конфу просто пообщаться, а уже через минуту я ебу какую то шлюху... ты понимаешь что я своим хуем накрыл клиторе твоей матери как волной цунами ?",
    "блять как не зайдешь в магазин там твоя мать тупая сидит на коленях и у прохожих сосёт за деньги, вот блять откуда у вас в доме хлеб, оказалось твоя мать зарабатывает тяжелым трудом",
]


@loader.tds
class MamkoebMod(loader.Module):
    strings = {
        "name": "🤡 Унижатор"
    }
    
    async def client_ready(self, client, db):
        self.db = db
        self.users = self.db.get("fucker", "users", [])
        self.phrases = self.db.get("fucker", "phrases", [])
    
    def add_phrase(self, phrase: str):
        self.phrases.append(phrase)
        self.db.set("fucker", "phrases", self.phrases)
    
    def add_user(self, user_id: int):
        self.users.append(user_id)
        self.db.set("fucker", "users", self.users)
    
    def remove_user(self, user_id: int):
        self.users.remove(user_id)
        self.db.set("fucker", "users", self.users)
    
    async def fuckclearcmd(self, message):
        """Очистить всех от срачей"""
        
        self.users = []
        self.db.set("fucker", "users", self.users)
        
        await utils.answer(
            message=message,
            response="🤡 <code>Больше я никого не унижаю</code>"
        )
    
    async def fuckaddcmd(self, message):
        """Добавить фразу | .fuckadd <фраза>"""
        
        args = utils.get_args_raw(message)
        
        if not args:
            return await utils.answer(
                message=message,
                response="<b>🚫 Не указан аргумент</b>"
            )
        
        self.add_phrase(args)
        
        await utils.answer(
            message=message,
            response="<b>Фраза добавлена</b>"
        )
    
    async def fuckrandcmd(self, message):
        """Вкинуть рандомное оскорбление"""
        
        await utils.answer(
            message=message,
            response=random.choice(srach + self.phrases)
        )
    
    async def fuckoncmd(self, message):
        """Выебать человека. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            if reply.from_id is not None:
                await utils.answer(
                    message=message,
                    response="<b>🤡 Давай начнём срач сын бездаря.</b>"
                )

                self.add_user(reply.from_id)
            
            else:
                await utils.answer(
                    message=message,
                    response="<code>🚫 Модуль не работает на анонимных администраторах или каналах</code>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🚫 Нужен реплай</b>"
            )
    
    async def fuckoffcmd(self, message):
        """Не выебать человека. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            await utils.answer(
                message=message,
                response="<b>идешь нахуй слитая немощь</b>"
            )
            
            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<code>🤡 Я и так не унижаю этого человека</code>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🚫 Нужен реплай</b>"
            )
    
    async def watcher(self, message):
        if getattr(message, "from_id", None) in self.users:
            await message.reply(random.choice(srach + self.phrases))
