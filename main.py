import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from flask import Flask
import threading
import random
app = Flask(__name__)

@app.route("/")
def hello():
 owner_username = "kingerdem"

 if owner_username == "kingerdem":  
  return "Powered By King Erdem"


def run_flask_app():
    app.run("0.0.0.0",port=random.randint(1000,9999))


def start_flask_app():
    # Yeni bir thread oluştur
    t = threading.Thread(target=run_flask_app)
    # Arka planda çalıştır
    t.daemon = True
    # Thread'i başlat
    t.start()

from flask import Flask
import threading
import os
import random

import schedule
import time
from os import system
def run_job():
 system("main.py")

# işlemi her 2 saatte bir çalıştırmak için
schedule.every(1).hours.do(run_job)

while True:
  schedule.run_pending()
  time.sleep(1)
  
    



 



logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = "14993791"
api_hash = "60a2897e2d7de8eefd6cf610085b1f0a"
bot_token = ""
bot_username = "anlamsiztaggerbot"
support = "botssupport"
owner = "kgerdem"
bot_name = "Anlamsız Tagger Bot"


SUDO_USERS = "6274336801"




client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []
  
kanallar = ['No have any ads now.',]
	
	
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     
     await event.reply(f"__{random.choice(kanallar)}__\n**#anlamsiztagger ADS**")
     await event.reply(f"**Merhaba Benim Adım [{bot_name}(http://t.me/{bot_username}).**\n**Grubunuzun tüm üyelerini tag etme yetkim var.**\n\n**Daha fazla bilgi için 📚 Komutlar bölümüne gidin.**", buttons=(
                     [Button.url('➕ Beni bir Gruba ekle ➕',f'http://t.me/{botusername}?startgroup=a')],
	             [Button.inline(f"📚 Komutlar", data="help"),
	              Button.inline(f"📑 Reklamlar", data="reklam")],
	             [Button.url('Grup💬', f'https://t.me/{support}'),
                      Button.url('Sahip 👨‍💻', f'https://t.me/{owner}')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"** Gruba eklediğiniz için teşekkürler**\n**Aşağıdaki bazı butonlar size yardım edebilir.**", buttons=(
                     [Button.url('💡Bota geç',f'https://t.me/{bot_username}?start=start')],
	             [Button.url('Sahip 👨‍💻', f'https://t.me/{owner}'),
		      Button.url('Grup💬', f'https://t.me/{support}')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     
     await event.reply(f"**ÖZEL SOHBETLER İÇİN REKLAM**\n{random.choice(kanallar)}")
     await event.reply(f"**Merhaba Benim Adım [{bot_name}](http://t.me/{bot_username}).**\n**Grubunuzun tüm üyelerini tag etme yetkim var.**\n\n**Daha fazla bilgi için '📚'Komutlar' bölümüne gidin.**", buttons=(
                     [Button.url('➕ Beni bir Gruba ekle ➕',f'http://t.me/{botusername}?startgroup=a')],
	             [Button.inline(f"📚 Komutlar", data="help"),
	              Button.inline(f"📑 Reklamlar", data="reklam")],
	             [Button.url('Grup💬', f'https://t.me/{support}'),
                      Button.url('Sahip 👨‍💻', f'https://t.me/{owner}')],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
    await event.edit(f"""**  [{bot_name}](http://t.me/{bot_username})-un Yardım '📚 komutları' Bunlardır.⤵**
    
    
    •━━━━━━━━•••━━━━━━━━•
    **➪ /tag <sebep> - 5-li Tag Atışları.**
    **➪ /etag <sebep> - Emoji ile etiketler.**
    **➪ /btag- <sebep> - bayraklar ile etiketler.**
    **➪ /mafia- <sebep> - Mafya oyunun rolleri ile etiketler.**
    **➪ /adtag- <sebep> - İlginç adlar ile etiket atar.**
    **➪ /erdem <sebep> - ilginç sözler ile tag eder **
    **➪ /tektag <sebep> - üyeleri tek-tek etiketler.**
    **➪ /admins <sebep> - Yöneticiler Tek-Tek etiketler.**
    **➪ /cancel - Etiketlemeyi Durdur.**
    •━━━━━━━━•••━━━━━━━━•**""", buttons=(
	             [Button.url('Grup💬', f'https://t.me/{support}'),
                      Button.url('Sahip 👨‍💻', f'https://t.me/{owner}')],
	             [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):	
    await event.edit(f"**📌 {bot_name} ile Reklamlar için sahibiyle iletişime geçebilirsiniz...**", buttons=(
		     [Button.url('🎉 Botlar', f'https://t.me/{owner}')],
	             [Button.url('Grup💬', f'https://t.me/{support}'),
                      Button.url('Sahip 👨‍💻', f'https://t.me/{owner}')],
	             [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)
	
    
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu yalnızca yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları etiketleyemem! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Etiketi başlatmak için bir neden girin...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Etiket işlemi başarıyla sonlandırıldı!**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**İşlem Başarıyla Durduruldu! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Etiket işlemi başarıyla sonlandırıldı! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**↯ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

stag = (
"Kaş önünüzde yere gidiyor",
"Bana ne yaptığımı söyle",
"Kalbim çarpıyor",
"Günahım yok inan bana",
"Varsa - söyle, kurban olayım!",
"Böyle olmasına dayanamıyorum",
"Neredeyse ölüyorum",

"Bana bak, flört etme.",
"Kaşlarını bile önüne atmayın",
"Gel beni dağ yapma",

"Kim ne dedi, söyle bakayım.",
"Seni yoldan mı çıkardı?",
"Sana kim ne söyledi?",
"Beni erkek mi yaptı?",
"O adamın mezarı nerede?",
"Cezasını çeksin!..",

"Dağlardaki sis çok güzel."
"Kaşların - yay güzel",
"Sözlerinin karşılığı yok",
"Gözlerin güzel",
"Aklımı uçurdu"
"Bu gözü geçemezsin"
"Seni çok seviyorum",
"Kalpten",
"aşık olma canım",
"Söğütler başını eğdiğinde",
"Sana yarım dediğimde",
"Sanırım dünya benim"
"Gözlerime baktığında",
"Aklımı uçurdu",
"Bu gözü geçemezsin",
"Seni sevdiğim kadar seviyorum",
"Seni kalbimin derinliklerinden seviyorum.",
"Gel ve bana sadık ol canım",
"Aşık olma canım",
"O morarmış göz olmasaydı,",
"Yeminlerimiz doğru olmasaydı",
"sana aldırış etmezdim.",
"Ya sözlerimiz söz olmasaydı?",

"gidiyorum bu akşam, gidiyorum gay",
"bensiz gül yüzün solacak biliyorum",
"вєη gι∂ιуσяυм, gєℓмєzѕєη ѕєνgιмιz уαηıρ çöρ σℓα¢αк",
"вєηѕιz gözℓєяιη ∂σℓα¢αк мı? hïç §åñmïɏðrïm",
"𝙮𝙖𝙡𝙖𝙣𝙙𝙖𝙣 𝙗𝙞𝙧 𝙨𝙚𝙫ş 𝙙𝙖 𝙮𝙖𝙨𝙖𝙩𝙞𝙧 𝙗𝙚𝙣𝙞",
"𝙗𝙚𝙣 𝙜𝙞𝙙𝙞𝙮𝙤𝙧𝙪𝙢 𝙜𝙚𝙡𝙢𝙚𝙮𝙚𝙘𝙚𝙠𝙨𝙚𝙣 𝙨𝙞𝙠𝙩𝙞𝙧 𝙜𝙞𝙩",
"𝙆𝙍𝘼𝙇𝙇",
"𝙩𝙤𝙥𝙧𝙖𝙠 𝙙𝙞𝙡𝙚 𝙜𝙚𝙡𝙞𝙧, 𝙖𝙮 𝙖𝙢𝙖𝙣",
"𝙫𝙖𝙩𝙖𝙣 𝙜𝙤𝙯𝙪 𝙮𝙖𝙨𝙡𝙞 𝙠𝙖𝙡𝙨𝙖 𝙤 𝙯𝙖𝙢𝙖𝙣",
"𝘴𝘦𝘷𝘨𝘪𝘭𝘪𝘮 𝘬𝘢𝘭𝘢𝘤𝘢𝘬 𝘣𝘦𝘯𝘴𝘪𝘻!",
"🄰🄺🅃🄰🅁🄸🄿 🅃🄰🄿🄳🄸🄼 🅂🄴🄽🄸",
"𝔰𝔢𝔫𝔡𝔢𝔪𝔦 𝔰𝔢𝔳𝔡𝔦𝔫 𝔶𝔞𝔯𝔯𝔞𝔨 𝔟𝔯𝔫𝔦? ",
"𝐬𝐞𝐧𝐢𝐧 𝐩𝐢*𝐥𝐢ğ𝐢𝐧 𝐲𝐮𝐳𝐮𝐧𝐝𝐞𝐧 𝐠𝐨𝐭𝐮𝐦 𝐠𝐨𝐫𝐦𝐮𝐨𝐫 𝐝𝐮𝐧𝐢𝐚𝐢",
"🆆🅷🅰🆃 🅸🆂 🆈🅾🆄🆁 🅿🆁🅾🅱🅻🅴🅼?????",
"🅶🅴🅻 🅴🅻🅴🅺🆃🆁🅸🅶🅸🅼 🅶🅴🅻",
"🅷🅴🅻🅰🅻 🅾🅻🆂🆄🅽",
"🆂🅴🅽 🅽🅴 🅺🅴🅻🅴🅱🅴🅺🆂🅸🅽 🆂🅴🆈🆃🅰🅽!",
"🅰🆂🅺🅸 🅾🅶🆁🅴🆃🆃🅸🅽 🅰🅼🅰 🆂🅸🅺🆃🅸🆁🅸🅿 🅶🅸🆃🆃🅸🅽",
"ｉｎａｎ ｄｅｒｔｌｅｒｉｍｄüｎｙａｙａｓığｍａｄı",


)	

@client.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag Başarıyla Durduruldu! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag Başarıyla Durduruldu! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎Yönetici Listesi♕︎"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ↯ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@client.on(events.NewMessage(pattern="^/erdem ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
usta = ('𝙆𝙊𝙈𝙐𝙏 𝙔𝘼𝙎𝘼𝙆𝙇𝘼𝙈𝘼𝙎İ👀😁😍','𝘾𝙊𝙈𝙈𝘼𝙉𝘿 𝘽𝘼𝙉𝙉𝙀𝘿🤒',) 

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu yalnızca yöneticiler kullanabilir!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Etiketi başlatmak için bir neden girin...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Etiket işlemi başarıyla sonlandırıldı!**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

bayrag = ['🏳️‍🌈','🏳️‍⚧️','🇦🇫','🇦🇽','🇦🇱','🇩🇿','🇦🇸','🇦🇩','🇦🇴','🇦🇮','🇦🇶','🇦🇬','🇦🇷','🇦🇲','🇦🇼','🇦🇺','🇦🇹','🇦🇿','🇧🇸','🇧🇭','🇧🇩','🇧🇧','🇧🇾','🇧🇪','🇧🇿','🇧🇯','🇧🇲','🇧🇹','🇧🇴','🇧🇦','🇧🇼','🇧🇷','🇻🇬','🇧🇳','🇧🇬','🇧🇫','🇧🇮','🇰🇭','🇨🇲','🇨🇦','🇮🇨','🇨🇻','🇧🇶','🇰🇾','🇨🇫','🇹🇩','🇮🇴','🇨🇱','🇨🇳','🇨🇽','🇨🇨','🇨🇴','🇰🇲','🇨🇬','🇨🇩','🇨🇰','🇨🇷','🇨🇮','🇭🇷','🇨🇺','🇨🇼','🇨🇾','🇨🇿','🇩🇰','🇩🇯','🇩🇲','🇩🇴','🇪🇨','🇪🇬','🇸🇻','🇬🇶','🇪🇷','🇪🇪','🇪🇹','🇸🇿','🇪🇺','🇫🇰','🇫🇴','🇫🇯','🇫🇮','🇫🇷','🇬🇫','🇵🇫','🇹🇫','🇬🇦','🇬🇲','🇬🇪','🇩🇪','🇬🇭','🇬🇮','🇬🇷','🇬🇱','🇬🇩','🇬🇵','🇬🇺','🇬🇹','🇬🇬','🇬🇳','🇬🇼','🇬🇾','🇭🇹','🇭🇳','🇭🇰','🇭🇺','🇮🇸','🇮🇳','🇮🇩','🇮🇷','🇮🇶','🇮🇪','🇮🇲','🇮🇱','🇮🇹','🇯🇲','🇯🇵','🎌','','🇯🇪','🇯🇴','🇰🇿','🇰🇪','🇰🇮','🇽🇰','🇰🇼','🇰🇬','🇱🇦','🇱🇻','🇱🇧','🇱🇸','🇱🇷','🇱🇾','🇱🇮','🇱🇹','🇱🇺','🇲🇴','🇲🇬','🇲🇼','🇲🇾','🇲🇻','🇲🇱','🇲🇹','🇲🇭','🇲🇶','🇲🇷','🇲🇺','🇾🇹','🇲🇽','🇫🇲','🇲🇩','🇲🇨','🇲🇳','🇲🇪','🇲🇸','🇲🇦','🇲🇿','🇲🇲','🇳🇦','🇳🇷','🇳🇵','🇳🇱','🇳🇨','🇳🇿','🇳🇮','🇳🇪','🇳🇬','🇳🇺','🇳🇫','🇰🇵','🇲🇰','🇲🇵','🇳🇴','🇴🇲','🇵🇰','🇵🇼','🇵🇸','🇵🇦','🇵🇬','🇵🇾','🇵🇪','🇵🇭','🇵🇳','🇵🇱','🇵🇹','🇵🇷','🇶🇦','🇷🇪','🇷🇴','🇷🇺','🇷🇼','🇼🇸','🇸🇲','🇸🇹','🇸🇦','🇸🇳','🇷🇸','🇸🇨','🇸🇱','🇸🇬','🇸🇽','🇸🇰','🇸🇮','🇬🇸','🇸🇧','🇸🇴','🇿🇦','🇰🇷','🇸🇸','🇪🇸','🇱🇰','🇧🇱','🇸🇭','🇰🇳','🇱🇨','🇵🇲','🇻🇨','🇸🇩','🇸🇪','🇸🇷','🇨🇭','🇸🇾','🇹🇼','🇹🇯','🇹🇿','🇹🇭','🇹🇱','🇹🇬','🇹🇰','🇹🇴','🇹🇹','🇹🇳','🇹🇷 Şanslı kişi','🇹🇲','🇹🇨','🇹🇻','🇺🇬','🇺🇦','🇦🇪','🇬🇧','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🏴󠁧󠁢󠁷󠁬󠁳󠁿','🇺🇸','🇺🇾','🇻🇮','🇺🇿','🇻🇺','🇻🇦','🇻🇪','🇻🇳','🇼🇫','🇪🇭','🇾🇪','🇿🇲','🇿🇼',]

@client.on(events.NewMessage(pattern="^/ftag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(futbol)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(futbol)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

futbol = ('Maldonado', 'JUNIOR MHASSI', 'Bobô', 'Matías Delgado', 'Márcio Nobre1', 'Rodrigo Tello', 'Federico Higuaín', 'Lamine Diatta', 'Édouard Cissé', 'Gordon Schildenfeld', 'Filip Hološko', 'Anthony Šerić', 'Tomáš Sivok', 'Tomáš Zápotočný', 'Fabian Ernst', 'Michael Fink', 'Matteo Ferrari', 'Rodrigo Tabata', 'Ricardo Quaresma', 'Roberto Hilbert', 'Guti', 'Marco Aurélio1', 'Manuel Fernandes', 'Simao Sabrosa', 'Hugo Almeida', 'Sidnei', 'Bébé', 'Júlio Alves', 'Edú', 'Julien Escudé', 'Allan McGregor', 'Dentinho', 'Mamadou Niang', 'Pedro Franco', 'Michael Eneramo', 'Atiba Hutchinson', 'Ramon Motta', 'Jermaine Jones', 'Dany Nounkeu', 'Demba Ba', 'José Sosa', 'Alexander Milošević', 'Daniel Opare', 'Duško Tošić', 'Andreas Beck', 'Luiz Rhodolfo', 'Mario Gómez', 'Denis Boyko', 'Aras Özbiliz', 'Alexis Delgado', 'Marcelo Guedes', 'Fabri', 'Adriano Correia', 'Talisca', 'Vincent Aboubakar', 'Ryan Babel', 'Matej Mitrović', 'Pepe', 'Álvaro Negredo', 'Jeremain Lens', 'Gary Medel', 'Cyle Larin', 'Vágner Love', 'Domagoj Vida', 'Enzo Roco', 'Loris Karius', 'Adem Ljajić', 'Nicolas Isimat-Mirin', 'Shinji Kagawa', 'Tyler Boyd', 'Douglas', 'Víctor Ruiz', 'Pedro Rebocho', "Georges-Kévin N'Koudou", 'Muhammed Elneni', 'Abdoulay Diaby', 'Ajdin Hasić', 'Kevin-Prince Boateng', "Fabrice N'Sakala", 'Bernard Mensah', 'Welinton', 'Francisco Montero', 'Josef de Souza', 'Valentin Rosier', 'Raşit Gezzal', 'Alex Teixeira', 'Michy Batshuayi', 'Miralem Pjanić', 'Gedson Fernandes', 'Romain Saïss', 'Mert Günok', 'Ersin Destanoğlu', 'Emre Bilgin', 'Goktug Baytekin', 'Domagoj Vida', 'Welinton', 'Douglas', 'Fabrice NSkala', 'Umut Meras', 'Francisco Montero', 'Valentin Rosier', 'Kerem Kalafat', 'Rıdvan Yılmaz', 'Serdar Saatçi', 'Serkan Emrecan Terzi', 'Aytug Batur Komec', 'Atiba Hutchinson', 'Mehmet Topal', 'Miralem Pjanic', 'Adem Ljajic', 'Alex Teixeira', 'Necip Uysal', 'Gökhan Töre', 'Rachid Ghezzal', 'Oğuzhan Özyakup', 'Georges-Kevin Nkoudou', 'Muhayer Oktay', 'Can Bozdogan', 'Berkay Vardar', 'Emirhan İlkhan', 'Emirhan Delibas', 'Demir Tiknaz', 'Jeremain Lens', 'Michy Batshuayi', 'Kenan Karıman', 'Cyle Larin', 'Güven Yalçın', 'Koray Yagci', 'Ariel Ortega', 'Robert Enke', 'Vladimir Beschastnykh', 'Ivaylo Petkov', 'Sergiy Rebrov', 'Stjepan Tomas', 'Pierre van Hooijdonk', 'Marco Aurelio', 'Fábio Luciano', 'Mert Nobre', 'Fabiano', 'Alex De Souza', 'Stephen Appiah', 'Nicolas Anelka', 'Mateja Kežman', 'Edu Dracena', 'Diego Lugano', 'Deivid', 'Roberto Carlos', 'Wederson', 'Claudio Maldonado', 'Josico', 'Daniel Güiza', 'Fábio Bilica', 'André Santos', 'Cristian Baroni', 'Miroslav Stoch', 'Issiar Dia', 'Mamadou Niang', 'Joseph Yobo', 'Emmanuel Emenike', 'Reto Ziegler', 'Henri Bienvenu', 'Moussa Sow', 'Dirk Kuyt', 'Miloš Krasić', 'Raul Meireles', 'Pierre Webó', 'Bruno Alves', 'Michal Kadlec', 'Samuel Holmén', 'Diego', 'Simon Kjær', 'Fernandão', 'Abdoulaye Ba', 'Fabiano Ribeiro', 'Nani', 'Josef de Souza', 'Robin van Persie', 'Lazar Marković', 'Aatif Chahechouhe', 'Gregory van der Wiel', 'Roman Neustädter', 'Martin Škrtel', 'Jeremain Lens', 'Oleksandr Karavayev', 'Mathieu Valbuena', 'Nebil Dirar', 'Carlos Kameni', 'Mauricio Isla', 'Elif Elmas', 'Roberto Soldado', 'Giuliano', 'Luís Neto', 'Vincent Janssen', 'André Ayew', 'Islam Slimani', 'Michael Frey', 'Diego Reyes', 'Jailson', 'Yassine Benzia', 'Victor Moses', 'Miha Zajc', 'Max Kruse', 'Allahyar Seyyadmeneş', 'Vedat Muriqi', 'Garry Rodrigues', 'Zanka', 'Adil Rami', 'Luiz Gustavo', 'Simon Falette', 'Filip Novák', 'Mame Thiam', 'José Sosa', 'Mauricio Lemos', 'Ener Valensiya', 'Marcel Tisserand', 'Mbwana Samatta', 'Papiss Cissé', 'Kemal Ademi', 'Dimitris Pelkas', 'Diego Perotti', 'Attila Szalai', 'Bright Osayi-Samuel', 'Mesut Özil', 'Steven Caulker', 'Kim Min-jae', 'Diego Rossi', 'Mërgim Berisha', 'Max Meyer', 'Miguel Crespo', 'Erol Bulut', 'Saffet Akbaş', 'Tayfun Korkut', 'Elvir Bolić', 'Mustafa Doğan', 'Samuel Johnson', 'Abdullah Ercan', 'Ogün Temizkanoğlu', 'Semih Şentürk', 'Ali Güneş', 'Serhat Akın', 'Ümit Özat', 'Volkan Demirel', 'Tuncay Şanlı', 'Selçuk Şahin', 'Fabio Luciano', 'Mehmet Yozgatlı', 'Mehmet Aurelio', 'Serkan Balcı', 'Önder Turacı', 'Uğur Boral', 'Gökhan Gönül', 'Gökçek Vederson', 'Colin Kâzım Richards', 'Emre Belözoğlu', 'Mehmet Topuz', 'Bekir İrtegün', 'Caner Erkin', 'Hasan Ali Kaldırım', 'Mehmet Topal', 'Alper Topuk', 'Şener Özbayraklı', 'Ozan Tufan', 'Aykut Erçetin', 'Çağlar Birinci', 'Gökhan Zan', 'Ceyhun Gülselam', 'Aydın Yılmaz', 'Selçuk İnan', 'Johan Elmander', 'Felipe Melo', 'Dida', 'Cafu', 'Stam', 'Nesta', 'Maldini', 'Pirlo', 'Gattuso', 'Seedorf', 'Kaka', 'Shevchenko', 'Inzaghi', 'Crespo', 'Diego Altube', 'Thibaut Courtois', 'Alphonse Areola', 'Andriy Lunin', 'Lucas Canizares', 'Luis Lopez', 'Toni Fuidias', 'Diego Del Alamo', 'Luis Federico', 'Sergio Ramos', 'Raphael Varane', 'Daniel Carvajal', 'Adrian De La Fuente', 'Ferland Mendy', 'Marcelo', 'Eder Militao', 'Alvaro Odriozola', 'Victor Chust', 'Sergio Santos', 'Pablo Ramon Parra', 'Miguel Gutierrez', 'David Alaba', 'Jesus Vallejo', 'Rafa Marin', 'Mario Gila', 'Reinier', 'Marco Asensio', 'Federico Valverde', 'Brahim Diaz', 'Luka Modric', 'Toni Kroos', 'Isco', 'Carlos Casemiro', 'Lucas Vazquez', 'Martin Odegaard', 'Marvin Park', 'Sergio Arribas', 'Antonio Blanco', 'Hugo Duro', 'Eduardo Camavinga', 'Dani Ceballos', 'Peter Gonzalez', 'Karim Benzema', 'Luka Jovic', 'Eden Hazard', 'Gareth Bale', 'Vinicius Junior', 'Rodrygo', 'James Rodriguez', 'Mariano Diaz', 'Borja Mayoral', 'Oscar Aranda', 'Juan Latasa', 'Neto', 'Marc-Andre Ter Stegen', 'Inaki Pena', 'Arnau Tenas', 'Lazar Carevic', 'Jordi Alba', 'Sergi Roberto', 'Ronald Araujo', 'Samuel Umtiti', 'Nelson Semedo', 'Clement Lenglet', 'Dani Morer', 'Junior Firpo', 'Gerard Pique', 'Sergio Akieme', 'Santiago Ramos', 'Arnau Comas', 'Sergino Dest', 'Oscar Mingueza', 'Eric Garcia', 'Emerson', 'Alejandro Balde', 'Dani Alves', 'Mika Marmol', 'Sergio Busquets', 'Hiroki Abe', 'Alex Collado', 'Frenkie De Jong', 'Ivan Rakitic', 'Arturo Vidal', 'Riqui Puig', 'Guillem Jaime', 'Miralem Pjanic', 'Philippe Coutinho', 'Carles Alena', 'Konrad De La Fuente', 'Ilaix Moriba', 'Matheus Fernandes', 'Yusuf Demir', 'Nico Gonzalez', 'Abde Ezzalzouli', 'Alvaro Sanz', 'Ferran Jutgla', 'Matheus Pereira', 'Lucas De Vega', 'Estanis Pedrola', 'Adama Traore', 'Luis Suarez', 'Ousmane Dembele', 'Antoine Griezmann', 'Ansu Fati', 'Lionel Messi', 'Rey Manaj', 'Martin Braithwaite', 'Memphis Depay', 'Sergio Agüero', 'Luuk De Jong', 'Ilias Akhomach', 'Ferran Torres', 'Pierre Aubameyang', 'Albert Riera', 'Milan Baroš', 'Tomáš Ujfaluši', 'Mehmet Batdal', 'Serkan Kurtuluş', 'Ypğit Götolan', 'Hakan Balta', 'Fernando Muslera', 'Semih Kaya', 'Emmanuel Eboué', 'Yekta Kurtuluş', 'Engin Baytar', 'Emre Çolak', 'Sabri Sarıoğlu', 'Servet Çetin', 'Necati Ateş', 'Ufuk Ceylan', 'Sercan Yıldırım', 'Fernando Muslera', 'Felipe Melo', 'Hamit Altıntop', 'Gökhan Zan', 'Blerim Džemaili', 'Aydın Yılmaz', 'Selçuk İnan', 'Umut Bulut', 'Wesley Sneijder', 'Bruma', 'Alex Telles', 'Burak Yılmaz', 'Sinan Gümüş', 'Goran Pandev', 'Aurélien Chedjou', 'Fernando Muslera', 'Mariano', 'Maicon', 'Serdar Aziz', 'Ahmet Çalık', 'Tolga Ciğerci', 'Yasin Öztekin', 'Selçuk İnan', 'Eren Derdiyok', 'Younès Belhanda', 'Sinan Gümüş', 'Martin Linnes', 'Ryan Donk', 'Cédric Carrasso', 'Şener Özbayraklı', 'Omar Elabdellaoui', 'Taylan Antalyalı', 'Henry Onyekuru', 'Ryan Babel', 'Radamel Falcao', 'Halil Dervişoğlu', 'Oghenekaro Etebo', 'Martin Linnes', 'Ryan Donk', 'Oğulcan Çağlayan', 'Kerem Aktürkoğlu', 'Ömer Bayram', 'Emre Akbaba Kürşad', 'Cristiano 𝚁𝚘𝚗𝚊𝚕𝚍𝚘', 'Pele', 'Marodona', 'Ronaldo', 'Thierry Henry', 'Kaka', 'Sergio Agüero', 'Xavi', 'Ruud Gullit', 'Arthur Zico', 'Lev Yashin', 'Iniesta', 'Lothar Matthäus', 'Giuseppe Meazza', 'Franz Beckenbauer', 'George Best', 'Roberto Baggio', 'Johan Cruyff', 'Luis Figo', 'Andrea Pirlo', 'Marco Van Basten', 'Zlatan Ibrahimovic', 'Sandro Mazzola', 'Ferenc Puskas', 'Zinedine Zidane', 'Alfredo Di Stéfano', 'Rio Ferdinand', 'Paolo Maldini', 'Robin van Persie', 'Iker Casillas', 'Neymar', 'Fabio Cannavaro', 'Yaya Toure', 'Edinson Cavani', 'Gabriel Batistuta', 'Thiago Silva', 'Dennis Bergkamp', 'Franck Ribery', 'Carles Puol', 'Mesut Özil', 'Dani Alves', 'David Silva', 'Karim Benzema', 'Javier Zanetti', 'Radamel Falcao', 'Bastian Schweinsteiger', 'Gianluigi Buffon', 'Arjen Robben', 'Wayne Rooney', 'Luis Suarez', 'Mbappe', 'Juan Román Riquelme', 'Sergio Ramos', 'Muhammed Salak', 'Cesc Fabregas', 'Gerard Pique', 'Pepe', 'Didier Drogba', 'Robert Lewandowski', 'David Villa', 'Wesley Sneijder', 'Philipp Lahm', "Samuel Eto'o", 'Carlos Tevez', 'Sergio Busquets', 'Samir Nasri', 'Eden Hazard', 'Diego Forlan', 'Klaas Jan Huntelaar', 'Sabri Saraçolu')
 

@client.on(events.NewMessage(pattern="^/mafia ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

mafia = (
"Senin oyundaki rolün 👮🏼 Çavuş!",
"Senin oyundaki rolün 🐺 Oboroten!",
"Senin oyundaki rolün 🤓 Satkın!",
"Senin oyundaki rolün 💃 Meşukə!",
"Senin oyundaki rolün 🤵🏼 Mafya!",
"Senin oyundaki rolün 🧙‍ Maq!",
"Senin oyundaki rolün 🤞🏼 Şanslı Vatandaş!",
"Senin oyundaki rolün 💣 Kamikadze!",
"Senin oyundaki rolün 👩🏼‍💻 Jurnalist!",
"Senin oyundaki rolün 🤹🏻 Aferist!",
"Senin oyundaki rolün 👨🏼 Vatandaş!",
"Senin oyundaki rolün 🕵🏼 Komiser Kattani!",
"Senin oyundaki rolün 🎖 Mer!",
"Senin oyundaki rolün 🔪 Manyak!",
"Senin oyundaki rolün 👨🏼‍⚕️️Doktor!",
"Senin oyundaki rolün 🤵🏻 Don!",
"Senin oyundaki rolün 🧙🏼 Bomj!",
"Senin oyundaki rolün 👨🏼‍💼 Vekil!",
"Senin oyundaki rolün 🧟 Arsonist!",
"Senin oyundaki rolün 🕴️ Katil!",
"Senin oyundaki rolün 🧝🏻‍♀️Şehzade!",
"Senin oyundaki rolün 🧟‍♀️Zombi!",
"Senin oyundaki rolün 🧛🏻‍♂️Vampir!",
"Senin oyundaki rolün 🧚🏻‍♀️Melek!",
"Senin oyundaki rolün 🦹🏻‍♂️Hayalet!",
"Senin oyundaki rolün 🦦Köstebek!",
"Senin oyundaki rolün 🦎Bukelamun!",
"Senin oyundaki rolün 🤡Joker!",
"Senin oyundaki rolün 🙍🏻‍♂️Mahpus",
"Senin oyundaki rolün 🙇🏻‍♂️Oğru!",
"Senin oyundaki rolün 🕵️Suikastcı!",
"Senin oyundaki rolün 🔮Reviver!",
"Senin oyundaki rolün 👷🏻‍Madenci!",
"Senin oyundaki rolün 💂Katil!",
"Senin oyundaki rolün 👻Ruh!",
"Senin oyundaki rolün 👳🏻‍♂️Satıcı!",
"Senin oyundaki rolün 👨🏻‍🦱Dedektif!",
"Senin oyundaki rolün 👨🏻‍🎤Specialist!",
"Senin oyundaki rolün ⭐️General!",
"Senin oyundaki rolün 🌂Ninja!"
)

@client.on(events.NewMessage(pattern="^/adtag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu komut gruplar için geçerlidir! **")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir! **")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Önceki Mesajları Cevaplayabilirim! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamak için bir sebep yok! **")
  else:
    return await event.respond("**Başlamak için bir sebep yok, yaz...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(ad)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(ad)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**çağrı Başarıyla Durduruldu! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

ad = ['Üzümlü kek ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Kara fil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu panda 🐼', 'Ay pare 🌛', 'Ballı lokma ✨', 'Lale 🌷', 'Ahtapot 🐙', 'Zambak ⚜️', 'Akasya 🌿', 'Akşam Sefası 🌛', 'Begon fil 🥀', 'Bengenozya eşeği 🪴', 'Bambu 🎍', 'Fesleğen 🌿', 'Kasımpatı 🌸', 'Manolya 🌾', 'Boncuk 🧿', 'Badem 🥭', 'Minnoş 🐹', 'Pokçik 🐣', 'Pofuduk 🐼', 'Unicorn 🦄', 'Karamel 🍫', 'Fındık 🌰', 'Fıstık 🥜', 'Pamuk ☁️', 'Mikroş 🥰', 'Zeytin 🫒', 'Afrodit 🧚🏻', 'Nergis ✨', 'Sümük ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare 🌺', 'Reyhan 🌷', 'Kaktüs 🌵', 'Buket 💐', 'Başak 🌾', 'Kar Tanesi ❄️', 'Tospik 🐢', 'Kelebek 🦋', 'Tavşan 🐰', 'siker 🍬', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği 🌻', 'Tweety 🐥', 'Star ✨', 'Kanca 🍀', 'Ateş böceği ✨']

@client.on(events.NewMessage(pattern='/offline'))
async def handler(event):
    # biri selam veya başka bir şey derse cevaplayın.
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Bana sahip değilsin!__")
    await event.reply(f'''**Bot Çalışıyor Merak Etmeyin** 
     https://t.me/{support} .
     
     ╭━━━╮ 
     ╰╮╭╮┃╱╱╭╮
     ╱┃┃┃┣━━╋╋━━┳╮╭┳╮╭╮
     ╱┃┃┃┃┃━╋┫╭╮┃╰╯┃┃┃┃
     ╭╯╰╯┃┃━┫┃╭╮┣╮╭┫╰╯┃
     ╰━━━┻━━┫┣╯╰╯╰╯╰━━╯
     ╱╱╱╱╱╱╭╯┃
     ╱╱╱╱╱╱╰━╯''',
		     buttons=(
	             [Button.url('Sahibi', f'https://t.me/{owner}'),
	             Button.url('Grup', f'https://t.me/{support}')],
                    ),
                    link_preview=False)

print(f">> Merak etmeyin bot çalışıyor. @{owner} Bilgi için <<")
client.run_until_disconnected()
