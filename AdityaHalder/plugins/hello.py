 import asyncio
from pyrogram import *
from pyrogram.types import *
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.command import commandpro
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only

 
@Client.on_message(commandpro(["cute"]) & filters.private & filters.group & filters.edited)
@errors
@sudo_users_only
async def hello_world(client: Client, message: Message):
    mg = await message.edit("😀")
    await asyncio.sleep(0.2)
    await mg.edit("😄")
    await asyncio.sleep(0.2)
    await mg.edit("🙂")
    await asyncio.sleep(0.2) 
    await mg.edit("😉")
    await asyncio.sleep(0.2) 
    await mg.edit("😇")
    await asyncio.sleep(0.2) 
    await mg.edit("🥰") 
    await asyncio.sleep(0.2) 
    await mg.edit("😍") 
    await asyncio.sleep(0.2) 
    await mg.edit("🤩")
    await asyncio.sleep(0.2) 
    await mg.edit("😋")
    await asyncio.sleep(0.2) 
    await mg.edit("😘")
    await asyncio.sleep(0.2) 
    await mg.edit("😜")
    await asyncio.sleep(0.2) 
    await mg.edit("🤪")
    await asyncio.sleep(0.2) 
    await mg.edit("😂")
    await asyncio.sleep(0.2) 
    await mg.edit("🤗")
    await asyncio.sleep(0.2) 
    await mg.edit("🤭")
    await asyncio.sleep(0.2) 
    await mg.edit("🥳")
    await asyncio.sleep(0.2) 
    await mg.edit("😝")
    await asyncio.sleep(0.2) 
    await mg.edit("😎")
    


__MODULE__ = "ʜᴇʟʟᴏ"
__HELP__ = f"""**🇮🇳 Cᴏᴍᴍᴀɴᴅ :**

`hello` - ** Emoji Fun**
"""
