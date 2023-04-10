import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageNotModified
#from info PREMIUM_IDS as sudo

sudo = [5709622852]

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


PLAN_EXP = """
Hey, Your plan got expired !

Kindly take a new plan by contacting my admin !
To check all available plans, Use /plans command.
"""


PLAN_ALIVE ="""
You plan is not expired 
Enjoy your plan and get more movies add free 
"""   

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
            InlineKeyboardButton("ᴘʟᴀᴛɪɴᴜᴍ - 99ʀs|3 ᴍᴏɴᴛʜs", callback_data="alert_msg2"),            
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
            InlineKeyboardButton("ᴘʟᴀᴛɪɴᴜᴍ - 99ʀs|3 ᴍᴏɴᴛʜs", callback_data="alert_msg2"),            
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
            await query.answer("ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴀɴʏ ᴘᴀɴɴᴇʟ !", show_alert=True)

    elif query.data=="alert_msg2":
            await query.answer("ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴀɴʏ ᴘᴀɴɴᴇʟ !", show_alert=True)

@Client.on_message(filters.command(["checkmyplan","checkmyplans"], prefixes=["/", "!"]))
async def check_(client: Client, message: Message):
  sender = message.from_user 
  if message.from_user.id in sudo:
     await message.reply(PLAN_ALIVE)

  if message.from_user.id not in sudo:
     await message.reply((PLAN_EXP).format(sender.id))



