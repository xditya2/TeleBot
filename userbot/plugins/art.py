# For TeleBot
# By @AKASH_AM1 and @xditya
# Kangers keep credits 
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.ded$")
@borg.on(admin_cmd(pattern=r"ded"))
@borg.on(sudo_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await ded.reply(n + " ==             |\n　　　　　|" "\n　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")

M = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")
P = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
K = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - -\n"
"_/﹋\_\n")
G = ("........___________________\n"
"....../ `-___________--_____|] - - - - - -\n"" - - ░ ▒▓▓█D \n"
"...../==o;;;;;;;;______.:/\n"
".....), -.(_(__) /\n"
"....// (..) ), —\n"
"...//___//\n")
D = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
H = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, my friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

@borg.on(admin_cmd(pattern=r"monster"))
@borg.on(sudo_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await monster.reply(M)
@borg.on(admin_cmd(pattern=r"pig"))
@borg.on(sudo_cmd(pattern=r"pig"))
async def bluedevipig(pig):
    await pig.reply(P)
@borg.on(admin_cmd(pattern=r"kiler"))
@borg.on(asudo_cmd(pattern=r"kiler"))
async def bluedevikiller(kiler):
    await kiler.reply(K)
@borg.on(admin_cmd(pattern=r"gun"))
@borg.on(sudo_cmd(pattern=r"gun"))
async def bluedevigun(gun):
    await gun.reply(G)
@borg.on(admin_cmd(pattern=r"dog"))
@borg.on(sudo_cmd(pattern=r"dog"))
async def bluedevidog(dog):
    await dog.reply(D)
@borg.on(admin_cmd(pattern=r"hmf"))
@borg.on(sudo_cmd(pattern=r"hmf"))
async def bluedevihmf(hmf):
    await hmf.reply(H)
