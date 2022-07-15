import os
import sys
import math
import urllib3
import asyncio
import random
import requests
import shutil

from datetime import datetime
from time import strftime, time

from git import Repo
from os import system, execle, environ
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram.types import Message
from pyrogram import filters, Client
from AdityaHalder.config import LOG_GROUP_ID, UPSTREAM_REPO, UPSTREAM_BRANCH, OWNER_ID
from AdityaHalder.modules.helpers.filters import command

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


__MODULE__ = "ᴜᴘᴅᴀᴛᴇ"
__HELP__ = f"""

**Note:**
**Tʜɪs Pʟᴜɢɪɴ Fᴏʀ Uᴘᴅᴀᴛᴇ**


/update
- Update Your Bot.
"""


@Client.on_message(command("update") & filters.user(OWNER_ID))
async def update_(client, message):
    response = await message.reply_text("Checking for available updates...")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit("Invalid Git Repository")
    to_exc = f"git fetch origin {UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("Bot is up-to-date!")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[
            (format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4
        ],
    )
    for info in repo.iter_commits(f"HEAD..origin/{UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Commited on:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        link = await paste_queue(updates)
        url = link + "/index.txt"
        nrs = await response.edit(
            f"<b>A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n**<u>Updates:</u>**\n\n[Click Here to checkout Updates]({url})"
        )
    else:
        nrs = await response.edit(
            _final_updates_, disable_web_page_preview=True
        )
    os.system("git stash &> /dev/null && git pull")
    await response.edit(
            f"{nrs.text}\n\nBot was updated successfully! Now, wait for 1 - 2 mins until the bot reboots!"
        )
        os.system("pip3 install -r Installer")
        os.system(f"kill -9 {os.getpid()} && python3 -m AdityaHalder")
        exit()
    return
