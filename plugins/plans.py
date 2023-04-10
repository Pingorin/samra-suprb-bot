import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageNotModified
from info import PREMIUM_IDS as sudo


PLANS_IMG = "https://graph.org/file/de9b8d53bd8a786f37029.jpg"

 
PLANS_TEXT = """<u>
ᴛʜᴇsᴇ ᴀʀᴇ ᴀʟʟ ᴛʜᴇ ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ !
ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴏɴᴇ.</u>
[ᴄʟɪᴄᴋ](https://t.me/Priyanka_samrottbot)
"""

HOW_TO_PAY = """
<u>ʜᴏᴡ ᴛᴏ ᴘᴀʏ ᴍᴏɴᴇʏ</u>

<code>» sᴛᴇᴘ 𝟷 : sᴄᴀɴ ʙᴀʀ ᴄᴏᴅᴇ ᴏʀ ᴘᴀʏ ᴏɴ ᴛʜɪs ᴜᴘɪ</code> : <code> 8194994597@paytm </code>

<code>» sᴛᴇᴘ 𝟸 : ᴄʟɪᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ʙᴜᴛᴛᴏɴ ᴀɴᴅ sᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴsʜᴏᴛ.</code>

<code>» sᴛᴇᴘ 𝟹 : ɪ ᴡɪʟʟ ᴀᴅᴅ ʏᴏᴜʀ ᴘʟᴀɴ ɪɴsᴛᴀɴᴛ.</code>
"""

   


@Client.on_message(filters.command(["checkmyplan","Checkmyplan"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
  sender = message.from_user 
  if message.from_user.id in sudo: 
    await message.reply("ʜᴇʏ, ʏᴏᴜʀ ᴘʟᴀɴ ɢᴏᴛ ᴇxᴘɪʀᴇᴅ ! ᴋɪɴᴅʟʏ ᴛᴀᴋᴇ ᴀ ɴᴇᴡ ᴘʟᴀɴ ʙʏ ᴄᴏɴᴛᴀᴄᴛɪɴɢ ᴍʏ ᴀᴅᴍɪɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs, ᴜsᴇ /plans ᴄᴏᴍᴍᴀɴᴅ.")

  if message.from_user.id not in sudo:
    await mesaage.reply(("ʏᴏᴜʀ ᴘʟᴀɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ. ʏᴏᴜ ᴀʀᴇ 🤭 [ᴘʀᴇᴍɪᴜᴍ](tg://user?id={}) ᴘᴇʀsᴏɴ.").format(sender.id))



@Client.on_message(filters.command(["plans","Plans"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
    await message.reply_photo((PLANS_IMG),
        caption=(PLANS_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("sɪʟᴠᴇʀ - 39ʀs|1 ᴍᴏɴᴛʜ", callback_data=f"alert_msg")
        ],
        [
            InlineKeyboardButton("ᴘʟᴀᴛɪɴᴜᴍ - 99ʀs|3 ᴍᴏɴᴛʜs", callback_data="alert_msg"),            
        ],
        [
            InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", url="https://t.me/Priyanka_samrottbot"),
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴘᴀʏ ᴍᴏɴᴇʏ", callback_data="help_pay"),            
  
        ],
    ]
  ),
)


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="home":
        buttons = [
        [
            InlineKeyboardButton("sɪʟᴠᴇʀ - 39ʀs|1 ᴍᴏɴᴛʜ", callback_data=f"alert_msg")
        ],
        [
            InlineKeyboardButton("ᴘʟᴀᴛɪɴᴜᴍ - 99ʀs|3 ᴍᴏɴᴛʜs", callback_data="alert_msg"),            
        ],
        [
            InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", url="https://t.me/Priyanka_samrottbot"),
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴘᴀʏ ᴍᴏɴᴇʏ", callback_data="help_pay"),            
  
        ],
    ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                PLANS_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="help_pay":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
                [
                    InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ", url="https://t.me/Priyanka_samrottbot"),
                    InlineKeyboardButton("ǫʀ ᴄᴏᴅᴇ sᴄᴀɴ", url="https://graph.org/file/3acbbee2c3f2030ea4f6e.jpg"),
                ],   
                [   
                    InlineKeyboardButton(" ᴄʟᴏsᴇ ", callback_data="close_data") ,
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
                ]
           ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOW_TO_PAY,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

    elif query.data=="alert_msg":
            await app.answer_callback_query("ᴛʜᴇsᴇ ᴀʀᴇ ᴀʟʟ ᴛʜᴇ ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ !\nᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴏɴᴇ.@Priyanka_samrottbot", show_alert=True)

