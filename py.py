import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("8284151707:AAENkDQc0nrHztvqzXUMMnqxb5l5XXuCQYQ")
WEBHOOK_PATH = f"/webhook/8284151707:AAENkDQc0nrHztvqzXUMMnqxb5l5XXuCQYQ"
WEBAPP_URL = "https://t.me/CloudsHub_bot/cloudhub"  # ваша ссылка на мини-приложение

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Стартовое сообщение с картинкой и кнопкой
@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="🚀Открыть приложение",
        url=WEBAPP_URL
    )
    keyboard.add(button)
    
    await message.answer_photo(
        photo="https://i.imgur.com/tz1GnLS.jpeg",
        caption=(
            "Добро пожаловать в интернет-магазин CloudHub.\n"
            "У нас вы можете приобрести жидкости для электронных сигарет, "
            "устройства, одноразовые вейпы и картриджи.\n"
            "Мы предлагаем широкий ассортимент, актуальные вкусы и популярные бренды.\n"
            "Удобное оформление заказа с быстрой доставкой.\n"
            "CloudHub — всё для комфортного вейпинга в одном месте.\n\n"
            "Чтобы перейти в бота нажмите ниже кнопку:"
        ),
        reply_markup=keyboard
    )

# Вебхук хэндлер для Railway
async def handle(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.process_update(update)
    return web.Response(text="ok")

async def on_startup(app):
    await bot.set_webhook(f"{os.getenv('RAILWAY_STATIC_URL')}{WEBHOOK_PATH}")

async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()

app = web.Application()
app.router.add_post(WEBHOOK_PATH, handle)
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=int(os.getenv("PORT", 3000)))
