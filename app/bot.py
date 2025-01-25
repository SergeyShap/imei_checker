from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from app.services import check_imei
from app.config import settings

async def start(update: Update, context):
    await update.message.reply_text("Привет! Отправь мне IMEI для проверки.")

async def handle_imei(update: Update, context):
    user_id = update.message.from_user.id
    if user_id not in settings.telegram_whitelist_as_list:
        await update.message.reply_text("Доступ запрещен.")
        return

    imei = update.message.text
    try:
        result = await check_imei(imei, settings.imei_check_api_token)
        await update.message.reply_text(f"Результат проверки IMEI {imei}:\n{result}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

def setup_bot():
    application = Application.builder().token(settings.telegram_bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_imei))
    return application
