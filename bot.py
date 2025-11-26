import telebot
from yt_dlp import YoutubeDL
import os

# Substitua pelo seu token de bot do Telegram
TOKEN = 'Digite aqui o Token do Bot do telegram'
bot = telebot.TeleBot(TOKEN)

# Dicionário para armazenar o link e a qualidade escolhida pelo usuário
user_video_data = {}

# Comando start: inicia o bot e solicita o link do vídeo
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá! Envie o link do vídeo do YouTube que você quer baixar.")

# Função para lidar com mensagens de texto (espera o link do vídeo)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    link = message.text
    user_video_data[message.chat.id] = {"link": link}
    
    # Opções de qualidade com botões
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("1080p", callback_data="1080p"),
        telebot.types.InlineKeyboardButton("720p", callback_data="720p"),
        telebot.types.InlineKeyboardButton("360p", callback_data="360p")
    )
    bot.reply_to(message, "Escolha a qualidade para baixar:", reply_markup=markup)

# Função que trata a escolha da qualidade e realiza o download
@bot.callback_query_handler(func=lambda call: True)
def handle_quality(call):
    chat_id = call.message.chat.id
    link = user_video_data.get(chat_id, {}).get("link")
    quality = call.data

    if not link:
        bot.send_message(chat_id, "Ocorreu um erro ao recuperar o link do vídeo.")
        return

    try:
        # Configuração do yt-dlp para baixar a qualidade desejada sem ffmpeg
        ydl_opts = {
            'format': f'best[height<={quality[:-1]}]',
            'outtmpl': 'downloaded_video.mp4',
            'quiet': True,
        }

        bot.send_message(chat_id, f"Baixando vídeo em {quality}... Isso pode levar alguns segundos.")

        # Baixar o vídeo usando yt-dlp
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        # Enviando o vídeo para o usuário
        with open('downloaded_video.mp4', 'rb') as video_file:
            bot.send_video(chat_id, video_file)

        # Removendo o arquivo após envio
        os.remove('downloaded_video.mp4')

    except Exception as e:
        bot.send_message(chat_id, f"Erro ao baixar o vídeo: {e}")

# Inicia o bot
bot.polling()
