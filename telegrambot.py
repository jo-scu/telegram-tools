import telebot
import time

TOKEN = "" 

bot = telebot.TeleBot(TOKEN)

print("Bot iniciado. Esperando mensajes...")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    print("=" * 50)
    print(f"Nuevo mensaje recibido:")
    print(f"ID del chat: {message.chat.id}")
    print(f"Nombre del chat: {message.chat.title if message.chat.title else 'Chat privado'}")
    print(f"ID del usuario: {message.from_user.id}")
    print(f"Nombre del usuario: {message.from_user.first_name} {message.from_user.last_name or ''}")
    print(f"Username: @{message.from_user.username}")
    print(f"Texto del mensaje: {message.text}")
    print(f"Fecha: {message.date}")
    print("=" * 50)

@bot.message_handler(commands=['start', 'help'])
def handle_commands(message):
    print(f"Comando recibido: {message.text}")
    bot.reply_to(message, "Bot receptor activado. Todos los mensajes serán registrados.")

@bot.message_handler(content_types=['photo', 'audio', 'video', 'document', 'location', 'contact'])
def handle_media(message):
    print("=" * 50)
    print(f"Mensaje multimedia recibido:")
    print(f"ID del chat: {message.chat.id}")
    print(f"Nombre del chat: {message.chat.title if message.chat.title else 'Chat privado'}")
    print(f"ID del usuario: {message.from_user.id}")
    print(f"Nombre del usuario: {message.from_user.first_name} {message.from_user.last_name or ''}")
    print(f"Username: @{message.from_user.username}")
    print(f"Tipo de contenido: {message.content_type}")
    print(f"Fecha: {message.date}")
    print("=" * 50)

def main():
    print("Iniciando bot receptor de mensajes...")
    print("Presiona Ctrl+C para detener el bot.")
    
    try:
        bot.polling(none_stop=True)
    except KeyboardInterrupt:
        print("\nBot detenido por el usuario.")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
        main()

if __name__ == "__main__":
    main()
