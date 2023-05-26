import os
import random
import telebot
import whisper
import time

TOKEN = "6178723737:AAG-ddfyi6DZU6VgxylQoexpaRiVTROYbPU"  # Telegram bot tokeninizi buraya girin
DOWNLOAD_PATH = "voice/"  # Ses dosyalarının indirileceği klasör yolunu buraya girin

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(chat_id=message.chat.id, text="""Hello! I am a bot that can transcribe audio files. Send me an audio file or song and I'll send you the transcript! You can get more information by typing /info. 
    
      Version: 1.0 --- Owner: @ --- Channel: @ """)

@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(chat_id=message.chat.id, text="You can use the following commands to use our bot: \n\n"
                                                  "/start - It starts the bot and displays the welcome message. \n"
                                                  "/info - It gives information about the bot. \n"
                                                  "/transcribe - Transcribes the audio file. \n"
                                                  "/cancel - Cancels the active operation. \n")

@bot.message_handler(content_types=['voice', 'audio'])
def handle_voice(message):
    try:
        if message.voice:
            file = message.voice
        elif message.audio:
            file = message.audio
        else:
            bot.send_message(chat_id=message.chat.id, text="Only audio files and songs are supported. ")
            return

        file_id = file.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path

        # Ses dosyasını indir
        downloaded_file = bot.download_file(file_path)
        random_number = random.randint(1, 10000)
        file_extension = file_path.split('.')[-1]
        file_name = f"{random_number}_{file_id}.{file_extension}"  # Rastgele sayı ile ses dosyasının adını oluştur
        # Transkripti kullanıcıya gönder ve tamamlanan yüzdeyi güncelle
        sent_message = bot.send_message(chat_id=message.chat.id, text=f"The download is %{0} complete. ")
        for i in range(1, 101):
            bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text=f"Download %{i} completed. ")
   #         time.sleep(2)  # Her bir istek arasına 2 saniye bekleme süresi ekleyin



        # Ses dosyasını diske kaydet
        with open(os.path.join(DOWNLOAD_PATH, file_name), 'wb') as f:
            f.write(downloaded_file)

        # Ses dosyasını transkript et
        model = whisper.load_model("tiny")
        result = model.transcribe(os.path.join(DOWNLOAD_PATH, file_name))
        text = result["text"]

#https://github.com/openai/whisper Parametersss

#Size	Parameters	English-only model	   Multilingual model	Required VRAM	Relative speed
#tiny	39 M	     tiny.en	               tiny               ~1 GB	            ~32x
#base	74 M	     base.en	               base	              ~1 GB	            ~16x
#small	244 M	     small.en	               small	          ~2 GB	            ~6x
#medium	769 M	     medium.en                 medium	          ~5 GB	            ~2x
#large	1550 M	     N/A	                   large	          ~10 GB	        ~1x


        # Transkripti kullanıcıya gönder ve tamamlanan yüzdeyi güncelle
        sent_message = bot.send_message(chat_id=message.chat.id, text=f"Transcript process %{0} complete. ")
        for i in range(1, 101):
            bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text=f"Transkript işlemi %{i} tamamlandı.")
            #time.sleep(5)  # Her bir istek arasına 0 saniye bekleme süresi ekleyin

        # Sonuçları kullanıcıya gönder
        bot.send_message(chat_id=message.chat.id, text=f"Transcript: {text}")

    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f"Something went wrong:  {e}")

if __name__ == '__main__':
    bot.polling()