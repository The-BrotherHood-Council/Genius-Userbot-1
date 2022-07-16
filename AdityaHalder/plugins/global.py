from pyrogram import filters
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
from AdityaHalder.utilities.mongo import gban_info, gban_list, gban_user, ungban_user, gmute, is_gmuted, ungmute, kaalub_info, rkaal, runkaal, loveub_info, rlove, runlove 
from AdityaHalder.utilities.data import *
from AdityaHalder.modules.helpers.filters import *
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only


async def iter_chats(client: Client):
    """Iter Your All Chats"""
    chats = []
    async for dialog in client.iter_dialogs():
        if dialog.chat.type in ["supergroup", "channel"]:
            chats.append(dialog.chat.id)
    return chats

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(command("gmute"))
@errors
@sudo_users_only
async def gmute_him(client: Client, message: Message):
    await message.delete()
    g = await message.edit_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    if not user:
        await g.edit("`Reply To User Or Mention To Gmute Him`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await g.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Just_Gmutted!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await g.edit("`Are you kidding with ne`")
        return
    if await is_gmuted(userz.id):
        await g.edit("`Re-Gmute? Seriously? :/`")
        return
    await gmute(userz.id, reason)
    gmu = f"**#Gmutted** \n**User :** `{userz.id}` \n**Reason :** `{reason}`"
    await g.edit(gmu)
    


@Client.on_message(command("ungmute"))
@errors
@sudo_users_only
async def gmute_him(client: Client, message: Message):
    await message.delete()
    ug = await message.edit_text("`Processing..`")
    text_ = get_text(message)
    user_ = get_user(message, text_)[0]
    if not user_:
        await ug.edit("`Reply To User Or Mention To Un-Gmute Him`")
        return
    try:
        userz = await client.get_users(user_)
    except:
        await ug.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await ug.edit("`Are ya kidding with me`")
        return
    if not await is_gmuted(userz.id):
        await ug.edit("`Un-Gmute A Non Gmutted User? Seriously? :/`")
        return
    await ungmute(userz.id)
    ugmu = f"**#Un-Gmutted** \n**User :** `{userz.id}`"
    await ug.edit(ugmu)
   


@Client.on_message(command("gban"))
@errors
@sudo_users_only
async def gbun_him(client: Client, message: Message):
    await message.delete()
    gbun = await message.edit_text("`Processing..`")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await gbun.edit("`Reply To User Or Mention To GBan Him`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await gbun.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return
    if not reason:
        reason = "Private Reason!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await gbun.edit("`Why bothering yourself`")
        return
    if await gban_info(userz.id):
        await gbun.edit("`Re-Gban? Seriously? :/`")
        return
    await gbun.edit("`Please, Wait Fectching Your Chats!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        gbun.edit("`You Have No Chats! So Sad`")
        return
    await gbun.edit("`Starting GBans Now!`")
    for devils in chat_dict:
        try:
            await client.kick_chat_member(devils, int(userz.id))
        except:
            failed += 1
    await gban_user(userz.id, reason)
    gbanned = f"**#GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Reason :** `{reason}` \n**Affected Chats :** `{chat_len-failed}`"
    await gbun.edit(gbanned)
    

@Client.on_message(command("ungban"))
@errors
@sudo_users_only
async def ungbun_him(client: Client, message: Message):
    await message.delete()
    ungbun= await message.edit_text("`Processing..`")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await ungbun.edit("`Reply To User Or Mention To Un-GBan Him`")
        return
    try:
        userz = await client.get_users(user)
    except:
        await ungbun.edit(f"`404 : User Doesn't Exists!`")
        return
    mee= await client.get_me()
    if userz.id == mee.id:
        await ungbun.edit("`what a joke`")
        return
    if not await gban_info(userz.id):
        await ungbun.edit("`Un-Gban A Ungbanned User? Seriously? :/`")
        return
    await ungbun.edit("`Please, Wait Fectching Your Chats!`")
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    if not chat_dict:
        ungbun.edit("`You Have No Chats! So Sad`")
        return
    await ungbun.edit("`Starting Un-GBans Now!`")
    for devils in chat_dict:
        try:
            await client.unban_chat_member(devils, int(userz.id))
        except:
            failed += 1
    await ungban_user(userz.id)
    ungbanned = f"**#Un_GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Affected Chats :** `{chat_len-failed}`"
    await ungbun.edit(ungbanned)
    


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
    if await is_gmuted(user):
        try:
            await message.delete()
        except:
            return
    if await gban_info(user):
        if message.chat.type != "supergroup":
            return
        try:
            me_ = await message.chat.get_member(int(client.me.id))
        except:
            return
        if not me_.can_restrict_members:
            return
        try:
            await client.kick_chat_member(message.chat.id, int(user))
        except:
            return
        await client.send_message(
            message.chat.id,
            f"**#GbanWatch** \n**Chat ID :** `{message.chat.id}` \n**User :** `{user}` \n**Reason :** `{await gban_info(user)}`",
        )
    


@Client.on_message(command("gbanlist"))
@errors
@sudo_users_only
async def give_glist(client: Client, message: Message):
    await message.delete()
    oof = "**#GBanList** \n\n"
    glist = await message.edit_text("`Processing..`")
    list_ = await gban_list()
    if len(list_) == 0:
        await glist.edit("`No User is Gbanned Till Now!`")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Reason :** `{lit['reason']}` \n\n"
    await edit_or_send_as_file(oof, glist, client, "GbanList", "Gban-List")


@Client.on_message(command("gcast"))
@errors
@sudo_users_only
async def gbroadcast(client: Client, message: Message):
    await message.delete()
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



__MODULE__ = "ɢʟᴏʙᴀʟ"
__HELP__ = f"""
**🥀 Gʙᴀɴ & Gᴍᴜᴛᴇ Mᴏᴅᴜʟᴇ ✨**

**ᴜsᴀɢᴇ:**
`.gmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gᴍᴜᴛᴇ.**

`.ungmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGᴍᴜᴛᴇ.**


`.gban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gʙᴀɴ.**

`.ungban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGʙᴀɴ.**

`.gbanlist` - ** Gᴇᴛ Lɪsᴛ Oғ Aʟʟ Gʙᴀɴ Usᴇʀs.**

`.gcast` - ** Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇssᴀɢᴇ Tᴏ Gʟᴏʙᴀʟʏ Bʀᴏᴀᴅᴄᴀsᴛ**
"""
