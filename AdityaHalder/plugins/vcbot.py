# 𝐊𝐚𝐚𝐥 𝐌𝐮𝐬𝐢𝐜 // @𝐢𝐚𝐦𝐤𝐚𝐚𝐥

import os
import aiofiles
import aiohttp
import ffmpeg
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from AdityaHalder.modules.cache.admins import set
from AdityaHalder.modules.clientbot import clientbot, queues
from AdityaHalder.modules.clientbot.clientbot import client as USER
from AdityaHalder.modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from AdityaHalder.modules import converter
from AdityaHalder.modules.downloaders import youtube
from AdityaHalder.config import que
from AdityaHalder.modules.cache.admins import admins as a
from AdityaHalder.modules.helpers.command import commandpro
from AdityaHalder.modules.helpers.filters import command, other_filters
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only
from AdityaHalder.modules.helpers.errors import DurationLimitError
from AdityaHalder.modules.helpers.gets import get_url, get_file_name
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

# plus
chat_id = None
useer = "NaN"


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



@Client.on_message(
    commandpro(["play", ".play", "!play", "/play", "ply"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
#errors
@sudo_users_only
async def play(_, message: Message):
    global que
    global useer
    await message.delete()
    lel = await message.reply("**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id


    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/ed6920a2f0ab5af3fd55d.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"


        requested_by = message.from_user.first_name
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            
        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/ed6920a2f0ab5af3fd55d.png"
            duration = "NaN"
            views = "NaN"

        requested_by = message.from_user.first_name
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
           return await lel.edit(
                "**🤖 𝐖𝐡𝐚𝐭 🙃 𝐘𝐨𝐮 💿 𝐖𝐚𝐧𝐭 😍\n💞 𝐓𝐨 🔊 𝐏𝐥𝐚𝐲❓**"
            ) and await lel.delete()

        await lel.edit("**🔎 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("**✅ 𝐅𝐢𝐧𝐚𝐥𝐢𝐳𝐢𝐧𝐠 ...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🔊 𝐌𝐮𝐬𝐢𝐜 😕 𝐍𝐨𝐭 📵 𝐅𝐨𝐮𝐧𝐝❗️\n💞 𝐓𝐫𝐲 ♨️ 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 🌷...**"
            ) and await lel.delete()
            print(str(e))
            return


        requested_by = message.from_user.first_name
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await lel.edit("**💥 𝐊𝐚𝐚𝐥🤞𝐀𝐝𝐝𝐞𝐝 💿 𝐒𝐨𝐧𝐠❗️\n🔊 𝐀𝐭 💞 𝐏𝐨𝐬𝐢𝐭𝐢𝐨𝐧 » `{}` 🌷 ...**".format(position),
    )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await lel.edit("**💥 𝐊𝐚𝐚𝐥🤞𝐌𝐮𝐬𝐢𝐜 🎸 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(),
        )

    return await lel.delete()
    
    
    
@Client.on_message(commandpro(["pause", ".pause", "!pause", "/pause", "pse"]) & other_filters)
#errors
@sudo_users_only
async def pause(_, message: Message):
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        noac = await message.reply_text("**💥 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 🔇 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 🌷 ...**")
        await noac.delete()
    else:
        await clientbot.pytgcalls.pause_stream(message.chat.id)
        pase = await message.reply_text("**▶️ 𝐏𝐚𝐮𝐬𝐞𝐝 🌷 ...**")
        await pase.delete()

@Client.on_message(commandpro(["resume", ".resume", "!resume", "/resume", "rsm"]) & other_filters)
#errors
@sudo_users_only
async def resume(_, message: Message):
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        noac = await message.reply_text("**💥 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 🔇 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 🌷 ...**")
        await noac.delete()
    else:
        await clientbot.pytgcalls.resume_stream(message.chat.id)
        rsum = await message.reply_text("**⏸ 𝐑𝐞𝐬𝐮𝐦𝐞𝐝 🌷 ...**")
        await rsum.delete()


@Client.on_message(commandpro(["skip", ".skip", "!skip", "/skip", "skp"]) & other_filters)
#errors
@sudo_users_only
async def skip(_, message: Message):
    global que
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
       novc = await message.reply_text("**💥 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 🔇 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 🌷 ...**")
       await novc.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            empt = await message.reply_text("**🥀 𝐄𝐦𝐩𝐭𝐲 𝐐𝐮𝐞𝐮𝐞, 𝐋𝐞𝐚𝐯𝐢𝐧𝐠 𝐕𝐂 ✨ ...**")
            await empt.delete()
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            next = await message.reply_text("**⏩ 𝐒𝐤𝐢𝐩𝐩𝐞𝐝 🌷 ...**")
            await next.delete()
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )
             


@Client.on_message(commandpro(["stop", "end", ".stop", ".end", "!stop", "!end", "/stop", "/end", "stp"]) & other_filters)
#errors
@sudo_users_only
async def stop(_, message: Message):
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        noac = await message.reply_text("**💥 𝐍𝐨𝐭𝐡𝐢𝐧𝐠 🔇 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 🌷 ...**")
        await noac.delete()
        return
    else:
        try:
            clientbot.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    leav = await message.reply_text("**❌ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝 🌷 ...**")
    await leav.delete()


@Client.on_message(commandpro(["reload", "admincache", ".reload", ".admincache", "!reload", "!admincache", "/reload", "/admincache" "rld", "ach"]))
#errors
@sudo_users_only
async def update_admin(client, message):
    global a
    await message.delete()
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    a[message.chat.id] = new_admins
    cach = await message.reply_text("**🔥 𝐑𝐞𝐥𝐨𝐚𝐝𝐞𝐝 🌷 ...**")
    await cach.delete()


__MODULE__ = "ᴠᴄʙᴏᴛ"
__HELP__ = f""" Yᴏᴜ Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Oɴ VC

`.play` - Pʟᴀʏ Mᴜsɪᴄ Oɴ Vᴄ
`.pause` - Pᴀᴜsᴇ Yᴏᴜʀ Mᴜsɪᴄ
`.resume` - Rᴇsᴜᴍᴇ Yᴏᴜʀ Mᴜsɪᴄ
`.skip` - Sᴋɪᴘ Tᴏ Tʜᴇ Nᴇxᴛ Sᴏɴɢ
`.stop` - Sᴛᴏᴘ Pʟᴀʏɪɴɢ Aɴᴅ Lᴇᴀᴠᴇ
`.reload` - Rᴇʟᴏᴀᴅ Yᴏᴜʀ VC Cʟɪᴇɴᴛ
`.song` - Dᴏᴡɴʟᴏᴀᴅ Sᴏɴɢ Yᴏᴜ Wᴀɴᴛ

**ɴᴏᴛᴇ:**
-Aʟsᴏ Sᴜᴅᴏ Usᴇʀs Cᴀɴ Cᴏɴᴛʀᴏʟ Tʜɪs Pʟᴜɢɪɴ
"""
