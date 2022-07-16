import asyncio
from pyrogram import *
from pyrogram.types import *
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only

 
@Client.on_message(command(["emoji"]))
async def hello_world(client: Client, message: Message):
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

`.emoji` - **Cʜᴀɴɢɪɴɢ Eᴍᴏᴊɪ Fᴜɴ**
"""
