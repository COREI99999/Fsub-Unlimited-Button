# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# recoded by https://t.me/ur_core_i9 [ dont forget to leave credit for this English version :)

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users 
 ├ /start - Start Bot
 ├ /about - About this Bot
 ├ /help - Bot Command Help
 ├ /ping - About bot ping
 └ /uptime - Bot uptime
 
 ❏ Command For Admin BOT
 ├ /logs - get bot logs
 ├ /setvar - To set var with the dibot command
 ├ /delvar - To delete var with the dibot command 
 ├ /getvar - To see one of the vars with the dibot command
 ├ /users -To view bot user statistics 
 ├ /batch - To batch files
 ├ /speedtest - bot server speed test
 └ /broadcast - broadcast message to users

👨‍💻 Develoved by </b><a href='https://t.me/ur_core_i9'>@ur_core_i9</a>
"""

    close = [
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("HELP & COMMANDS", callback_data="help"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ABOUT BOT", callback_data="about"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:
 
@{} is a Telegram bot for saving posts or files that can be accessed via a special link.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://t.me/ur_core_i9'>ASK-POLIETLY v4</a>

👨‍💻 Develoved by </b><a href='https://t.me/ur_core_i9'>@ur_core_i9</a>
"""
