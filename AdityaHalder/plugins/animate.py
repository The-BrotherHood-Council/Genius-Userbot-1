import asyncio
from pyrogram import *
from pyrogram.types import *
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.command import commandpro
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only

 
@Client.on_message(commandpro(["hello"]))
async def hello(client: Client, message: Message):
    mg = await message.edit("😀")
    await asyncio.sleep(1)
    await mg.edit("😄")
    await asyncio.sleep(1)
    await mg.edit("🙂")
    await asyncio.sleep(1) 
    await mg.edit("😉")
    await asyncio.sleep(1) 
    await mg.edit("😇")
    await asyncio.sleep(1) 
    await mg.edit("🥰") 
    await asyncio.sleep(1) 
    await mg.edit("😍") 
    await asyncio.sleep(1) 
    await mg.edit("🤩")
    await asyncio.sleep(1) 
    await mg.edit("😋")
    await asyncio.sleep(1) 
    await mg.edit("😘")
    await asyncio.sleep(1) 
    await mg.edit("😜")
    await asyncio.sleep(1) 
    await mg.edit("🤪")
    await asyncio.sleep(1) 
    await mg.edit("😂")
    await asyncio.sleep(1) 
    await mg.edit("🤗")
    await asyncio.sleep(1) 
    await mg.edit("🤭")
    await asyncio.sleep(1) 
    await mg.edit("🥳")
    await asyncio.sleep(1) 
    await mg.edit("😝")
    await asyncio.sleep(1) 
    await mg.edit("😎")
    

__MODULE__ = "Aɴɪᴍᴀᴛᴇ"
__HELP__ = f"""**🇮🇳 Bᴇsᴛ Aɴɪᴍᴀᴛɪᴏɴs :**

`hello` - **Cʜᴀɴɢɪɴɢ Eᴍᴏᴊɪ Fᴜɴ**
"""
