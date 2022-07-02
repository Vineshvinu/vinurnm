from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
        Hello {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram
	**Document Or Video** and enter new file name to rename it Powerd ©️ @Tamil_Hackers_Moviess__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("🌟 Join 🌟" ,url="https://t.me/All_language_movie_request_group"), 
	  InlineKeyboardButton("❤️ Subscribe ❤️", url="https://t.me/Tamil_Hackers_Moviess")
          ],[
          InlineKeyboardButton("✨ Channel ✨", url="https://t.me/Tamil_Hackers_Moviess")
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
       __✨What do you want me to do with this File **Replay Fast Don't Delay ©️Powerd by vinu😎**__\n**🗃️File Name** :- {filename}\n**📦File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
