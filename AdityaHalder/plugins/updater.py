import sys
from git import Repo
from os import system, execle, environ
from git.exc import InvalidGitRepositoryError
from pyrogram.types import Message
from pyrogram import filters, Client
from AdityaHalder.config import UPSTREAM_REPO, UPSTREAM_BRANCH OWNER_ID
from AdityaHalder.modules.helpers.filters import command


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("UPSTREAM_BRANCH", origin.refs.UPSTREAM_BRANCH)
        repo.heads.UPSTREAM_BRANCH.set_tracking_branch(origin.refs.UPSTREAM_BRANCH)
        repo.heads.UPSTREAM_BRANCH.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@Client.on_message(command(["update"]) & filters.user(OWNER_ID) & ~filters.edited)
async def update_bot(_, message: Message):
    chat_id = message.chat.id
    msg = await message.reply("» ᴄʜᴇᴄᴋɪɴɢ ᴜᴘᴅᴀᴛᴇs...")
    update_avail = updater()
    if update_avail:
        await msg.edit("»__ ᴜᴘᴅᴀᴛᴇ ғɪɴɪsʜᴇᴅ __\n» __ʙᴏᴛ ʀᴇsᴛᴀʀᴛɪɴɢ, ʙᴀᴄᴋ ᴀᴄᴛɪᴠᴇ ᴀɢᴀɪɴ ɪɴ 2ᴍɪɴ __.")
        system("git pull -f && pip3 install -U -r Installer")
        execle(sys.executable, sys.executable, "-m modules", environ)
        return
    await msg.edit(f"__» ᴀʟʀᴇᴀᴅʏ ᴜᴘᴅᴀᴛᴇᴅ ʙʏ ɢᴇɴɪᴜs __")

__MODULE__ = "ᴜᴘᴅᴀᴛᴇ"
__HELP__ = f"""

**Note:**
**Tʜɪs Pʟᴜɢɪɴ Fᴏʀ Uᴘᴅᴀᴛᴇ**


/update
- Update Your Bot.
"""
