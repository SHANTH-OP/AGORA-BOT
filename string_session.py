
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
AGORA-USERBOT = """
"""
print(AGORA-USERBOT)
print("""String Generator. ==> AGORABot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.
╭━━━┳╮╱╱╭┳━━━━┳╮╱╭┳━━━┳━╮╱╭╮
┃╭━╮┃╰╮╭╯┃╭╮╭╮┃┃╱┃┃╭━╮┃┃╰╮┃┃
┃╰━╯┣╮╰╯╭┻╯┃┃╰┫╰━╯┃┃╱┃┃╭╮╰╯┃
┃╭━━╯╰╮╭╯╱╱┃┃╱┃╭━╮┃┃╱┃┃┃╰╮┃┃
┃┃╱╱╱╱┃┃╱╱╱┃┃╱┃┃╱┃┃╰━╯┃┃╱┃┃┃
╰╯╱╱╱╱╰╯╱╱╱╰╯╱╰╯╱╰┻━━━┻╯╱╰━╯
╭━━╮╭━━━┳━━━━╮
┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━╮┃┃╱┃┃╱┃┃
┃╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━━╯╱╰╯""")
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as PYTHONBOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(AGORA-USERBOT.session.save())
    print("")
    print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
    omk =AGORA-USERBOT.send_message("me", f"`{AGORA-USERBOT.session.save()}`")
    omk.reply("The above is the `AGORA_STRING` #POWERFUL [AGORA-USERBOT](https://t.me/AGORA_SPAM_OFFICIAL)"
		)
