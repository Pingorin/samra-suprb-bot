import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


PLANS_IMG = "https://graph.org/file/de9b8d53bd8a786f37029.jpg"




PLANS_TEXT = """
ᴛʜᴇsᴇ ᴀʀᴇ ᴀʟʟ ᴛʜᴇ ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ !
ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴏɴᴇ.
"""

    
   

@Client.on_message(filters.command(["plans","Plans"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
    await message.reply_photo((PLANS_IMG),
        caption=(START_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("sɪʟᴠᴇʀ - 39ʀs|1 ᴍᴏɴᴛʜ", url=f"https://t.me/")
        ],
        [
            InlineKeyboardButton("ᴘʟᴀᴛɪɴᴜᴍ - 99ʀs|3 ᴍᴏɴᴛʜs", url="https://t.me/"),            
        ],
        [
            InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", url="https://t.me/Priyanka_samrottbot"),
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴘᴀʏ ᴍᴏɴᴇʏ", callback_data="help_pay"),            
  
    ]
  ),
)
