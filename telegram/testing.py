from telethon import TelegramClient, events
import logging
import pytz

# Configuración de la zona horaria
cet = pytz.timezone('Etc/GMT+5')

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('telethon').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Función de inicio
def start():
    # Inicializa los clientes de Telegram con tus API ID y Hash
    client = TelegramClient('client1', 27134009, 'b9fd535093c2868f2231610dcd0bf6d5')
    client.start()

    # ID del canal donde se emiten los mensajes que deseas capturar
    input_channel_id = -1002110119318
    # ID del canal donde deseas reenviar los mensajes
    output_channel_id = -1001948656029

    # Manejador para mensajes nuevos en el canal especificado
    @client.on(events.NewMessage(chats=input_channel_id))
    async def handler(event):
        message = event.message
        # Verifica si el mensaje contiene la palabra "amazon"
        string_validation_msg = 'amazon' in message.text.lower() if message.text else False

        # Si la palabra "amazon" está presente, reenvía el mensaje al canal de destino
        if string_validation_msg:
            await client.send_message(output_channel_id, message)
    
    client.run_until_disconnected()

# Ejecución del script
if __name__ == "__main__":
    start()

