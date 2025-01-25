import multiprocessing
import uvicorn
from app.api import app as fastapi_app
from app.bot import setup_bot

def run_fastapi():
    uvicorn.run(fastapi_app, host="localhost", port=8001)

def run_bot():
    bot = setup_bot()
    bot.run_polling()

if __name__ == "__main__":
    # Запуск FastAPI в отдельном процессе
    fastapi_process = multiprocessing.Process(target=run_fastapi)
    fastapi_process.start()

    # Запуск Telegram-бота в основном процессе
    run_bot()