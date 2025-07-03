import logging
from telegram.ext import *
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import responses 

API_KEY = '7889080801:AAFVoiJA4YxtL3RWTghYKIbjYAH67YwOYHg'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Iniciando el Bot de InventarioApp...')

async def start_command(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Consultar stock 📦", callback_data='stock')],
        [InlineKeyboardButton("Reportar un error 🛠", callback_data='error')],
        [InlineKeyboardButton("Hablar con soporte 👩‍💻", callback_data='soporte')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        '¡Hola! 👋 Bienvenido al soporte de InventarioApp 🧾📦. ¿Qué deseas hacer?',
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'stock':
        await query.edit_message_text(text="🔍 Por favor indícame el nombre del producto o código que deseas consultar.")
    elif query.data == 'error':
        await query.edit_message_text(text="🚨 ¿Qué error estás experimentando? Nuestro equipo lo revisará.")
    elif query.data == 'soporte':
        await query.edit_message_text(text="📞 Contactanos por WhatsApp: +54 123456789 o por correo a soporte@inventarioapp.com.")

async def help_command(update: Update, context):
    await update.message.reply_text('Escribime tu problema y trataré de ayudarte.')

async def custom_command(update: Update, context):
    await update.message.reply_text('¿En qué puedo ayudarte con InventarioApp?')

async def handle_message(update: Update, context):
    texto = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) escribe: {texto}')
    bot_response = responses.get_response(texto)
    await update.message.reply_text(bot_response)

async def error(update: Update, context):
    logging.error(f'update {update} caused error {context.error}')

if __name__ == '__main__':
    application = Application.builder().token(API_KEY).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('custom', custom_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    application.add_error_handler(error)
    application.run_polling(poll_interval=0.0)
