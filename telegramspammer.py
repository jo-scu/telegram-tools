import telebot
import time
import random
from threading import Thread
import sys

TOKEN = ""
CHAT_ID = ""

MENSAJE_RAID = ""

NUM_THREADS = 10

MENSAJES_POR_HILO = 50

INTERVALO_MINIMO = 0.1
INTERVALO_MAXIMO = 0.5

def enviar_mensajes_raid():
    bot = telebot.TeleBot(TOKEN)
    
    for i in range(MENSAJES_POR_HILO):
        try:
            bot.send_message(CHAT_ID, MENSAJE_RAID, parse_mode="Markdown")
            print(f"Mensaje enviado #{i+1}: {MENSAJE_RAID}")
            
            time.sleep(random.uniform(INTERVALO_MINIMO, INTERVALO_MAXIMO))
            
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
            time.sleep(2)

def main():
    print("=" * 50)
    print("INICIANDO RAID DE DISCORD EN TELEGRAM")
    print("=" * 50)
    print(f"Mensaje de raid: {MENSAJE_RAID}")
    print(f"Hilos simultáneos: {NUM_THREADS}")
    print(f"Mensajes por hilo: {MENSAJES_POR_HILO}")
    print(f"Total de mensajes: {NUM_THREADS * MENSAJES_POR_HILO}")
    print("=" * 50)
    print("Presione Ctrl+C para detener el raid...")
    
    hilos = []
    for i in range(NUM_THREADS):
        hilo = Thread(target=enviar_mensajes_raid)
        hilos.append(hilo)
        hilo.start()
        print(f"Hilo {i+1} iniciado")
    
    try:
        for hilo in hilos:
            hilo.join()
    except KeyboardInterrupt:
        print("\nSpam detenido por el usuario.")
        sys.exit(0)
    
    print("Spam completado.")

if __name__ == "__main__":
    main()
