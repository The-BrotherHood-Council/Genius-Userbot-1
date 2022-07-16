from pyrogram import filters, Client
from traceback import format_exc
from typing import Tuple
import asyncio
import random
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message)
from AdityaHalder.utilities.mongo import kaalub_info, rkaal, runkaal, loveub_info, rlove, runlove 
from AdityaHalder.utilities.data import *
from AdityaHalder.config import *
from AdityaHalder.modules.helpers.filters import *
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only
from AdityaHalder.modules.databases.gmute_db import get_gmuted_users, gmute_user, ungmute_user
from AdityaHalder.modules.databases.gban_db import *
from AdityaHalder.modules.helpers.program import get_arg
from AdityaHalder.modules.helpers.admins import CheckAdmin

# Aditya Halder

@Client.on_message(filters.command("gmute", ["."]) & filters.me)
async def gmute(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I gmute?**")
            return
    get_user = await app.get_users(user)
    await gmute_user(get_user.id)
    await message.edit(f"**Successfully Taped {get_user.first_name}, This users mouth!**")


@Client.on_message(filters.command("ungmute", ["."]) & filters.me)
async def ungmute(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I ungmute?**")
            return
    get_user = await app.get_users(user)
    await ungmute_user(get_user.id)
    await message.edit(f"**Unmuted {get_user.first_name}, enjoy!**")

@Client.on_message(filters.command("gban", ["."]) & filters.me)
async def gban(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I gban?**")
            return
    get_user = await app.get_users(user)
    await gban_user(get_user.id)
    await message.edit(f"**Successfully Gbanned {get_user.first_name}!**")


@Client.on_message(filters.command("ungban", ["."]) & filters.me)
async def ungban(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I ungban?**")
            return
    get_user = await app.get_users(user)
    await ungban_user(get_user.id)
    await message.edit(f"**Ungbanned {get_user.first_name}, enjoy!**")


@Client.on_message(filters.group & filters.incoming)
async def check_and_del(app: Client, message):
    if not message:
        return
    try:
        if not message.from_user.id in (await get_gmuted_users()):
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await app.delete_messages(message.chat.id, message_id)
    except:
        pass

@Client.on_message(filters.group & filters.incoming)
async def check_and_del_(app: Client, message):
    if not message:
        return
    try:
        if not message.from_user.id in (await get_gban_users()):
            return
    except AttributeError:
        return
    try:
        await app.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    except:
        pass



@Client.on_message( ~filters.me & filters.incoming)
async def watch(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user = message.from_user.id
    kaal = random.choice(REPLY_RAID)
    love = random.choice(LOVER_RAID)
    if int(user) in VERIFIED_USERS:
        return
    elif int(user) in SUDO_USERS:
        return
    if int(message.chat.id) in GROUP:
        return
    if await kaalub_info(user):
        try:
            await message.reply_text(kaal)
        except:
            return
    if await loveub_info(user):
        try:
            await message.reply_text(love)
        except:
            return


@Client.on_message(command("gcast"))
@errors
@sudo_users_only
async def gbroadcast(client: Client, message: Message):
    msg_ = await message.edit_text("`Processing..`")
    failed = 0
    if not message.reply_to_message:
        await msg_.edit("`Reply To Message Boss!`")
        return
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    await msg_.edit("`Now Sending To All Chats Possible!`")
    if not chat_dict:
        msg_.edit("`You Have No Chats! So Sad`")
        return
    for c in chat_dict:
        try:
            msg = await message.reply_to_message.copy(c)
        except:
            failed += 1
    await msg_.edit(
        f"`Message Sucessfully Send To {chat_len-failed} Chats! Failed In {failed} Chats.`"
    )



__MODULE__ = "Gʟᴏʙᴀʟ"
__HELP__ = f"""
**🥀 Gʙᴀɴ & Gᴍᴜᴛᴇ Mᴏᴅᴜʟᴇ ✨**

**ᴜsᴀɢᴇ:**
`.gmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gᴍᴜᴛᴇ.**

`.ungmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGᴍᴜᴛᴇ.**

`.gban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gʙᴀɴ.**

`.ungban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGʙᴀɴ.**

`.gcast` - ** Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇssᴀɢᴇ Tᴏ Gʟᴏʙᴀʟʏ Bʀᴏᴀᴅᴄᴀsᴛ**
"""
