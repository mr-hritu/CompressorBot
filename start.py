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
from telethon import Button,  TelegramClient, events, functions, errors
import requests, json

LOGS.info("Starting...")

######## Connect ########


try:
    cbot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()

####### GENERAL CMDS ########

async def check_user(user):
    ok = True
    try:
        await cbot(
            functions.channels.GetParticipantRequest(
                channel="Private_Bots", participant=user
            )
        )
        ok = True
    except errors.rpcerrorlist.UserNotParticipantError:
        ok = False
    return ok

async def broadcast(user_list, message, client):
    for i in user_list:
        user_id = i['user_id']
        try:
            await client.forward_messages(user_id, message)
        except errors.FloodWaitError as e:
            print(f'Sleeping for {e.seconds} seconds.')
            time.sleep(e.seconds)
        except Exception as e:
            print(f'Error: {e}')

@cbot.on(events.NewMessage(pattern="/start"))
async def _(e):
    user = await e.get_sender()
    if not await check_user(user.id):
        await force(e)
        return
    else:
        await start(e)

@cbot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    await up(e)


@cbot.on(events.NewMessage(pattern="/help"))
async def _(e):
    await help(e)

@cbot.on(events.NewMessage(pattern="/users"))
async def _(e):
    await statss(e)

@cbot.on(events.NewMessage(pattern="/insert"))
async def insert(e):
    users_list = get_served_users()
    ok = requests.get("https://pastebin.com/raw/tDDGEH48").text
    ok = ok.replace('None',str("483097119")).replace("'","")
    ok = json.loads(ok)
    for i in ok:
        add_served_user(i)
        
@cbot.on(events.NewMessage(pattern='/broad'))
async def handler(event):
    if event.chat_id != 6629411642:
        return
    msg_to_br = await event.get_reply_message()
    users_list = get_served_users()  # You need to define this function
    await broadcast(users_list, msg_to_br, cbot)
    await cbot.send_message(6629411642, "Done")

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
