# Aditya Halder // @AdityaHalder
from AdityaHalder.modules.databases import db as dbb

Rbun = dbb["RBAN"]


async def rkaal(user, reason="#MATHERCHOD"):
    await Rbun.insert_one({"user": user, "reason": reason})


async def runkaal(user):
    await Rbun.delete_one({"user": user})


async def rban_list():
    return [lo async for lo in Rbun.find({})]


async def kaalub_info(user):
    kk = await Rbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]


# Aditya Halder // @AdityaHalder

Lbun = dbb["LBAN"]


async def rlove(user, reason="#MYLOVER"):
    await Lbun.insert_one({"user": user, "reason": reason})


async def runlove(user):
    await Lbun.delete_one({"user": user})


async def lban_list():
    return [lo async for lo in Lbun.find({})]


async def loveub_info(user):
    um = await Lbun.find_one({"user": user})
    if not um:
        return False
    else:
        return um["reason"]



gbun = dbb["GBAN"]


async def gban_user(user, reason="#GBanned"):
    await gbun.insert_one({"user": user, "reason": reason})


async def ungban_user(user):
    await gbun.delete_one({"user": user})


async def gban_list():
    return [lo async for lo in gbun.find({})]


async def gban_info(user):
    kk = await gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]



gmuteh = dbb["GMUTE"]


async def is_gmuted(sender_id):
    kk = await gmuteh.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


async def gmute(sender_id, reason="#GMuted"):
    await gmuteh.insert_one({"sender_id": sender_id, "reason": reason})


async def ungmute(sender_id):
    await gmuteh.delete_one({"sender_id": sender_id})
