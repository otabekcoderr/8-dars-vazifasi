from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖 Badiiy kitoblar"),
            KeyboardButton(text="📘 Darsliklar"),
            KeyboardButton(text="📚 IT kitoblar"),
        ],
        [
            KeyboardButton(text="🔍 Kitob qidirish"),
            KeyboardButton(text="📚💬 Kitob muhokama"),
            KeyboardButton(
                text="🔝 Top 10 ta kitob",
            ),
        ],
        [
            KeyboardButton(text="ℹ️ Biz haqimizda"),
            KeyboardButton(text="📞 Biz bilan bog'lanish"),
        ],
    ],
    resize_keyboard=True,
)

inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Ⓜ️ Muhokama qilish",
                callback_data="muhokama_button",
            ),
        ]
    ]
)


badiiy_kitoblar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❤️ O‘tkan kunlar", callback_data="badiiy_1"),
            InlineKeyboardButton(text="⚔️ Mehrobdan chayon", callback_data="badiiy_2"),
        ],
        [
            InlineKeyboardButton(text="🌙 Kecha va kunduz", callback_data="badiiy_3"),
            InlineKeyboardButton(text="🚪 Ikki eshik orasi", callback_data="badiiy_4"),
        ],
        [
            InlineKeyboardButton(text="🌍 Dunyoning ishlari", callback_data="badiiy_5"),
            InlineKeyboardButton(text="👁️ 1984", callback_data="badiiy_6"),
        ],
        [
            InlineKeyboardButton(text="🐷 Molxona", callback_data="badiiy_7"),
            InlineKeyboardButton(text="✨ Alkimyogar", callback_data="badiiy_8"),
        ],
        [
            InlineKeyboardButton(text="⚖️ Jinoyat va jazo", callback_data="badiiy_9"),
            InlineKeyboardButton(
                text="👑 Kichkina shahzoda", callback_data="badiiy_10"
            ),
        ],
    ]
)


darsliklar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📐 Matematika", callback_data="darslik_1"),
            InlineKeyboardButton(text="⚛️ Fizika", callback_data="darslik_2"),
        ],
        [
            InlineKeyboardButton(text="🧪 Kimyo", callback_data="darslik_3"),
            InlineKeyboardButton(text="🧬 Biologiya", callback_data="darslik_4"),
        ],
        [
            InlineKeyboardButton(text="🌍 Geografiya", callback_data="darslik_5"),
            InlineKeyboardButton(text="📜 Tarix", callback_data="darslik_6"),
        ],
        [
            InlineKeyboardButton(text="🇬🇧 Ingliz tili", callback_data="darslik_7"),
            InlineKeyboardButton(text="📖 Ona tili", callback_data="darslik_8"),
        ],
        [
            InlineKeyboardButton(text="💻 Informatika", callback_data="darslik_9"),
            InlineKeyboardButton(text="🧠 Huquq", callback_data="darslik_10"),
        ],
    ]
)


it_kitoblar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🐍 Python", callback_data="it_1"),
            InlineKeyboardButton(text="🌐 HTML & CSS", callback_data="it_2"),
        ],
        [
            InlineKeyboardButton(text="⚡ JavaScript", callback_data="it_3"),
            InlineKeyboardButton(text="☕ Java", callback_data="it_4"),
        ],
        [
            InlineKeyboardButton(text="🔷 C++", callback_data="it_5"),
            InlineKeyboardButton(text="🔵 C#", callback_data="it_6"),
        ],
        [
            InlineKeyboardButton(text="🗄️ SQL", callback_data="it_7"),
            InlineKeyboardButton(text="🐘 PHP", callback_data="it_8"),
        ],
        [
            InlineKeyboardButton(text="🦄 Django", callback_data="it_9"),
            InlineKeyboardButton(text="⚛️ React", callback_data="it_10"),
        ],
    ]
)
