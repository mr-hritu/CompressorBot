#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in <https://github.com/1Danish-00/CompressorBot/blob/main/License> .


from helper._get import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserBannedInChannel, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant



LOGS.info("Starting...")


######## Connect ########


try:
    cbot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()



app = Client(
        "pdf",
        bot_token=BOT_TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )


@app.on_message(filters.text & filters.private & filters.incoming)
async def fore(c, m):
      try:
        chat = await c.get_chat_member(-1001785446911, m.from_user.id)
        if chat.status=="kicked":
           await c.send_message(chat_id=m.chat.id, text="You are Banned ☹️\n\n📝 If u think this is an ERROR message in @Prime_Hritu", reply_to_message_id=m.id)
           m.stop_propagation()
      except UserBannedInChannel:
         return await c.send_message(chat_id=m.chat.id, text="Hai you made a mistake so you are banned from channel so you are banned from me too 😜")
      except UserNotParticipant:
          button = [[InlineKeyboardButton('🇮🇳 Updates Channel', url=f'https://t.me/Private_Bots')]]
          markup = InlineKeyboardMarkup(button)
          return await c.send_message(chat_id=m.chat.id, text="""Hai bro,\n\nYou must join my channel for using me.\n\nPress this button to join now\n\nReport Error at @Prime_Hritu 👇""", reply_markup=markup)
      m.continue_propagation()





####### GENERAL CMDS ########


@cbot.on(events.NewMessage(pattern="/start"))
async def _(e):
    await start(e)


@cbot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    await up(e)


@cbot.on(events.NewMessage(pattern="/help"))
async def _(e):
    await help(e)


######## Callbacks #########


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sshot(.*)")))
async def _(e):
    await screenshot(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gsmpl(.*)")))
async def _(e):
    await sample(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"encc(.*)")))
async def _(e):
    await encc(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sencc(.*)")))
async def _(e):
    await sencc(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ccom(.*)")))
async def _(e):
    await ccom(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back(.*)")))
async def _(e):
    await back(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## Direct ###########


@cbot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)


@cbot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


########## AUTO ###########


@cbot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


########### Start ############

LOGS.info("Bot has started.")
cbot.run_until_disconnected()
