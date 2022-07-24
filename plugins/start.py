from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
        𝗛𝗲𝗹𝗹𝗼 {message.from_user.first_name }
	__🅸 🅰🅼 🅵🅸🅻🅴 🆁🅴🅰🅽🅰🅼🅴🆁 🅱🅾🆃, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐭 🔼 𝐚𝐧𝐲 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦
	**Document Or Video** 𝐚𝐧𝐝 𝐞𝐧𝐭𝐞𝐫 𝐧𝐞𝐰 𝐅𝐈𝐋𝐄 𝐧𝐚𝐦𝐞 𝐭𝐨 𝐫𝐞𝐧𝐚𝐦𝐞 𝐢𝐭 𝐏𝐨𝐰𝐞𝐫𝐝 ©️ **@Tamil_Hackers_Moviess**__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("🌟 𝖩𝖮𝖨𝖭 🌟" ,url="https://t.me/All_language_movie_request_group"), 
	  InlineKeyboardButton("❤️ 𝙎𝙐𝘽𝙎𝘾𝙍𝙄𝘽𝙀 ❤️", url="https://t.me/Tamil_Hackers_Moviess")
          ],[
          InlineKeyboardButton("✨ 𝖢𝖧𝖠𝖭𝖭𝖤𝖫 ✨", url="https://t.me/Tamil_Hackers_Moviess")
          ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f""" Hey👋 {message.from_user.first_name }
       __✨𝚆𝚑𝚊𝚝 𝚍𝚘 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚖𝚎 𝚝𝚘 𝚍𝚘 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝙵𝚒𝚕𝚎📦__\n**🗃️File Name** :- {filename}\n**📦File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 𝗥𝗘𝗡𝗔𝗠𝗘 ",callback_data = "rename")
       ,InlineKeyboardButton("𝗖𝗔𝗡𝗖𝗘𝗟✖️",callback_data = "cancel")  ]]))
