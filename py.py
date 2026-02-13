import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.filters import Command

TOKEN = "8284151707:AAENkDQc0nrHztvqzXUMMnqxb5l5XXuCQYQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):

    text = (
        "Добро пожаловать в интернет-магазин CloudHub. У нас вы можете приобрести жидкости для электронных сигарет, устройства, одноразовые вейпы и картриджи. "
        "Мы предлагаем широкий ассортимент, актуальные вкусы и популярные бренды. Удобное оформление заказа с быстрой доставкой. "
        "CloudHub всё для комфортного вейпинга в одном месте.\n\n"
        "Что-бы перейти в бота нажмите ниже кнопку:"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🚀Открыть приложение",
                    url="https://t.me/CloudsHub_bot/cloudhub"
                )
            ]
        ]
    )

    photo = FSInputFile("image.jpg")  # <-- сюда вставь имя своего изображения

    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
