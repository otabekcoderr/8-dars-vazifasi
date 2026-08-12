import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile

from button import (
    start_button,
    inline_button,
    badiiy_kitoblar_button,
    darsliklar_button,
    it_kitoblar_button,
    qaytish_button_badiiy,
    darslik_sinf_button,
)
from contact_text import contact_text
from about_us_text import about_text
from text import (
    top_kitoblar,
    muhokama_text,
    badiiy_kitoblar,
    badiiy_kitob_sarlavha,
    darslik_sarlavha,
    darsliklar,
    it_kitoblar_sarlavha,
    it_kitoblar,
    qidirish_bolim_tugmasi,
    muhokama_bolim_tugmasi,
)

TOKEN = "8750415210:AAFWvQr7-Ds5emWL6cjzoTZLyStL2UNGVMk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

photo_file = FSInputFile(
    r"D:\Telegram botlar\Kitob_bot\ChatGPT Image Aug 10, 2026, 04_20_12 PM.png"
)

badiiy_kitoblar_png = FSInputFile(
    r"D:\Telegram botlar\Kitob_bot\rasmlar\badiiy kitoblar.png"
)


# Muhokama inline tugmasi uchun
@dp.callback_query(F.data == "muhokama_button")
async def muhokama_but(callback: CallbackQuery):
    await callback.message.bot.send_photo(
        chat_id=callback.from_user.id,
        photo=muhokama_text[callback.data]["photo"],
        caption=muhokama_text[callback.data]["text"],
        reply_markup=qaytish_button_badiiy,
    )
    await callback.answer()


# Qaytish inline tugmasi uchun
@dp.callback_query(F.data == "orqaga_qaytish_badiiy")
async def orqaga_qaytish_tugmasi(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(reply_markup=badiiy_kitoblar_button)

    await callback.answer()


# Badiiy kitoblar inline tugmalari uchun
@dp.callback_query(F.data.in_(badiiy_kitoblar.keys()))
async def badiy_but(callback_badiy: CallbackQuery):
    await callback_badiy.message.bot.send_photo(
        chat_id=callback_badiy.from_user.id,
        photo=badiiy_kitoblar[callback_badiy.data]["photo"],
        caption=badiiy_kitoblar[callback_badiy.data]["text"],
        parse_mode="Markdown",
        reply_markup=inline_button,
    )
    await callback_badiy.answer()


# It kitoblarning inline tugmasi uchun
@dp.callback_query(F.data.in_(it_kitoblar.keys()))
async def it_but(callback: CallbackQuery):
    await callback.message.bot.send_photo(
        chat_id=callback.from_user.id,
        photo=it_kitoblar[callback.data]["photo"],
        caption=it_kitoblar[callback.data]["text"],
        reply_markup=inline_button,
        parse_mode="Markdown",
    )
    await callback.message()


# Darslar inline tugmasining javobi uchun
@dp.callback_query(
    F.data.in_(
        [
            "darslik_1",
            "darslik_2",
            "darslik_3",
            "darslik_4",
            "darslik_5",
            "darslik_6",
            "darslik_7",
            "darslik_8",
            "darslik_9",
            "darslik_10",
        ]
    )
)
async def sinf_button(callback: CallbackQuery):
    await callback.message.answer(
        text="Kerakli sinfni tanlang:", reply_markup=darslik_sinf_button
    )
    await callback.answer()


@dp.message(Command("start"))
async def quick_start(msg: Message):
    chatId = msg.from_user.id
    fullname = msg.from_user.full_name
    metion = f"<a href='tg://user?id={chatId}'>{fullname}</a>"
    await msg.answer(
        f"Assalomu alaykum {metion}! \nMen kitobchi AI botman,\nkitoblar haqida savolingiz bo'lsa javob beraman 😊",
        parse_mode="html",
        reply_markup=start_button,
    )


@dp.message()
async def answer_func(msg: Message):

    # Badiiy kitoblar
    if msg.text == "📖 Badiiy kitoblar":
        await msg.answer(
            text=badiiy_kitob_sarlavha["text"],
            reply_markup=badiiy_kitoblar_button,
            parse_mode="Markdown",
        )
        return

    # darsliklar
    if msg.text == "📘 Darsliklar":
        await msg.answer(text=darslik_sarlavha["text"], reply_markup=darsliklar_button)

        return

    # it kitoblar

    if msg.text == "📚 IT kitoblar":
        await msg.answer(
            text=it_kitoblar_sarlavha["text"], reply_markup=it_kitoblar_button
        )
        return

    # Admin contact
    if msg.text == "📞 Biz bilan bog'lanish":
        await msg.answer(contact_text)
        return

    # Biz haqimizda
    if msg.text == "ℹ️ Biz haqimizda":
        await msg.bot.send_photo(
            chat_id=msg.from_user.id,
            photo=photo_file,
            caption=about_text,
        )
        return

    # top 10 kitob
    if msg.text == "🔝 Top 10 ta kitob":
        await msg.answer(top_kitoblar, reply_markup=inline_button)
        return

    # kitob qidirish

    servis_505 = "https://www.cloudways.com/blog/wp-content/uploads/fix-503-service-unavailable-error-in-wordpress.jpg"

    if msg.text == "🔍 Kitob qidirish":
        await msg.bot.send_photo(
            chat_id=msg.from_user.id, photo=servis_505, caption=qidirish_bolim_tugmasi
        )
        return

    if msg.text == "📚💬 Kitob muhokama":
        await msg.bot.send_photo(
            chat_id=msg.from_user.id, photo=servis_505, caption=muhokama_bolim_tugmasi
        )
        return

    if msg.contact:
        await msg.answer("Raqamingizni ulashganingizdan mamnunman 😊")
    await msg.reply(msg.text)


async def main():
    print("Ishga tushdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
