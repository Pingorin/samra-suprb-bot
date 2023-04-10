import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from info import PREMIUM_IDS as sudo



@Client.on_message(filters.command(["checkmyplan","Checkmyplan"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
  sender = message.from_user 
  if message.from_user.id in sudo: 
    await message.reply("ʜᴇʏ, ʏᴏᴜʀ ᴘʟᴀɴ ɢᴏᴛ ᴇxᴘɪʀᴇᴅ ! ᴋɪɴᴅʟʏ ᴛᴀᴋᴇ ᴀ ɴᴇᴡ ᴘʟᴀɴ ʙʏ ᴄᴏɴᴛᴀᴄᴛɪɴɢ ᴍʏ ᴀᴅᴍɪɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs, ᴜsᴇ /plans ᴄᴏᴍᴍᴀɴᴅ.")

  if message.from_user.id not in sudo:
    await mesaage.reply(("ʏᴏᴜʀ ᴘʟᴀɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ. ʏᴏᴜ ᴀʀᴇ 🤭 [ᴘʀᴇᴍɪᴜᴍ](tg://user?id={}) ᴘᴇʀsᴏɴ.").format(sender.id))
