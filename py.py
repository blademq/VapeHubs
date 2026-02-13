import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()  # Загружаем BOT_TOKEN из .env

API_TOKEN = os.getenv("8284151707:AAENkDQc0nrHztvqzXUMMnqxb5l5XXuCQYQ")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WELCOME_TEXT = (
    "Добро пожаловать в интернет-магазин CloudHub.\n"
    "У нас вы можете приобрести жидкости для электронных сигарет, устройства, одноразовые вейпы и картриджи. "
    "Мы предлагаем широкий ассортимент, актуальные вкусы и популярные бренды. "
    "Удобное оформление заказа с быстрой доставкой. CloudHub — всё для комфортного вейпинга в одном месте.\n\n"
    "Что-бы перейти в бота нажмите ниже кнопку:"
)

IMAGE_URL = "https://i.imgur.com/tz1GnLS.jpeg"
BUTTON_URL = "https://t.me/CloudsHub_bot/cloudhub"

# Кнопка
keyboard = InlineKeyboardMarkup(row_width=1)
button = InlineKeyboardButton(text="🚀 Открыть приложение", url=BUTTON_URL)
keyboard.add(button)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=IMAGE_URL, caption=WELCOME_TEXT, reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
