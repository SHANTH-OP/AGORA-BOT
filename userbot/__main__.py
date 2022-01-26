from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, AGORAversion
from pathlib import Path
import asyncio
import glob
import telethon.utils
l2= Config.SUDO_COMMAND_HAND_LER
AGORA_PIC = Config.ALIVE_PIC or "https://te.legra.ph/file/78a7494a15602979a9241.mp4"
l1 = Config.COMMAND_HAND_LER


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"AGORA_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()
print("Loading Modules / Plugins")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
"""
async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

        extra_repo = "https://github.com/SHANTH-OP/AGORA-BOT"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "AGORA-BOT/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[AGORA-USERBOT] - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[AGORA-USERBOT] - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
"""
bot.loop.run_until_complete(module())

print(f"""『☘️ AGORA-USERBOT ☘️』➙𖤍࿐ IS ON!!! AGORA VERSION :- {AGORAversion}
TYPE :- " .gpromote @AGORASWAMY_PROFESSOR " OR .agora OR .ping CHECK IF I'M ON!
╔════❰AGORABOT❱═❍⊱❁۪۪
║┣⪼ OWNER - PROFESSOR AGORA
║┣⪼{AGORA_PIC}
║┣⪼ CREATOR -@AGORASWAMY_PROFESSOR
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『☘️ AGORA-USERBOT ☘️』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



async def python_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                PYTHON_PIC.
                caption=f"#START \n\nDeployed AGORA-USERBOT Successfully\n\n**AGORA-USERBOT- {AGORAversion}**\n\nType `{l1}agora` or `{l1}alive` to check! \n\nJoin [AgoraBot Channel](t.me/Agorabot_info) for Updates & [AgoraBot Chat](t.me/Agora_Userbot) for any query regarding AgoraBot",
            )
    except Exception as e:
        print(str(e))

# Join AgoraBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Agorabot_info"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@agora_userbot"))
    except BaseException:
         pass


bot.loop.create_task(agora_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
