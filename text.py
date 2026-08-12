from aiogram.types import FSInputFile

top_kitoblar = """🔝 TOP 10 TA KITOB

1. Atom odatlar — Jeyms Klir
2. 1984 — Jorj Oruell
3. Molxona — Jorj Oruell
4. O‘sish nuqtasi — Alisher Isayev
5. Mamlakatlar tanazzuli sabablari — Daron Ajemo‘g‘li, Jeyms A. Robinson
6. Qo‘rqma — Javlon Jovliyev
7. Yuksaklik sari tasodif bo‘lmagan 100 ta uchrashuv — Otabek Mahkamov
8. Hokimiyatning 48 qoidasi — Robert Grin
9. Diqqat — Kel Nyuport
10. Urush san’ati — Sun Szi

Kitob haqida ma'lumot olish uchun tartib raqamini kiriting
"""


muhokama_text = {
    "muhokama_button": {
        "text": "Tez orada tugmalar ishlaydi ⚠️\nNoqulaylik uchun uzur so‘raymiz 😔",
        "photo": "https://www.cloudways.com/blog/wp-content/uploads/fix-503-service-unavailable-error-in-wordpress.jpg",
    }
}


badiiy_kitoblar = {
    "badiiy_1": {
        "text": "📖 **O‘tkan kunlar**\n"
        "✍️ **Muallif:** Abdulla Qodiriy\n\n"
        "❤️ **Muhabbat. Sadoqat. Fojia.**\n"
        "Otabek va Kumushning unutilmas muhabbati orqali XIX asr Turkistonidagi "
        "ijtimoiy hayot, oilaviy nizolar va siyosiy muhit tasvirlanadi.\n\n"
        "💭 *Haqiqiy muhabbat taqdir sinovlariga dosh bera oladimi?*",
        "photo": FSInputFile(r"D:\Telegram botlar\Kitob_bot\rasmlar\otgan kunlar.jpg"),
    },
    "badiiy_2": {
        "text": "📖 **Mehrobdan chayon**\n"
        "✍️ **Muallif:** Abdulla Qodiriy\n\n"
        "⚔️ **Muhabbat va hokimiyat to‘qnashuvi.**\n"
        "Rano va Anvarning sevgisi fonida Xudoyorxon saroyidagi fitnalar, "
        "mansabparastlik va adolatsizliklar ochib beriladi.\n\n"
        "💭 *Hokimiyat insonni qanchalik o‘zgartira oladi?*",
        "photo": FSInputFile(
            r"D:\Telegram botlar\Kitob_bot\rasmlar\mehrobdan chayon.jpg"
        ),
    },
    "badiiy_3": {
        "text": "📖 **Kecha va kunduz**\n"
        "✍️ **Muallif:** Cho‘lpon\n\n"
        "🌙 **Bir qiz taqdiri — butun bir davr aksi.**\n"
        "Zebining fojeali taqdiri orqali chor Rossiyasi hukmronligi ostidagi "
        "Turkiston hayoti, jaholat va ayolning jamiyatdagi o‘rni yoritiladi.\n\n"
        "💭 *Zebi o‘z taqdirini o‘zi tanlay olarmidi?*",
        "photo": FSInputFile(
            r"D:\Telegram botlar\Kitob_bot\rasmlar\kecha va kunduz.jpg"
        ),
    },
    "badiiy_4": {
        "text": "📖 **Ikki eshik orasi**\n"
        "✍️ **Muallif:** O‘tkir Hoshimov\n\n"
        "🕊️ **Urush — inson qalbining sinovi.**\n"
        "Urush yillaridagi og‘ir taqdirlar, ayriliq, sadoqat, xiyonat va "
        "insoniylik haqida hikoya qiluvchi ta’sirchan roman.\n\n"
        "💭 *Insonni og‘ir kunlarda nima inson qilib qoladi?*",
        "photo": FSInputFile(
            r"D:\Telegram botlar\Kitob_bot\rasmlar\ikki eshik orasi.jpg"
        ),
    },
    "badiiy_5": {
        "text": "📖 **Dunyoning ishlari**\n"
        "✍️ **Muallif:** O‘tkir Hoshimov\n\n"
        "🌿 **Ona — hayotdagi eng buyuk hikoya.**\n"
        "Oddiy hayot manzaralari, bolalik xotiralari va ona mehrini samimiy "
        "tasvirlagan ta’sirchan qissalar to‘plami.\n\n"
        "💭 *Onangizning qadriga yetish uchun yana qancha vaqt kerak?*",
        "photo": FSInputFile(
            r"D:\Telegram botlar\Kitob_bot\rasmlar\dunyoning ishlari.jpg"
        ),
    },
    "badiiy_6": {
        "text": "📖 **1984**\n"
        "✍️ **Muallif:** Jorj Oruell\n\n"
        "👁️ **Sizni kimdir doimo kuzatayotgan bo‘lsa-chi?**\n"
        "Inson fikri, xotirasi va erkinligi nazorat qilinadigan totalitar "
        "jamiyat haqidagi mashhur antiutopik roman.\n\n"
        "💭 *Erkin fikrni taqiqlash mumkinmi?*",
        "photo": FSInputFile(r"D:\Telegram botlar\Kitob_bot\rasmlar\1984.jpg"),
    },
    "badiiy_7": {
        "text": "📖 **Molxona**\n"
        "✍️ **Muallif:** Jorj Oruell\n\n"
        "🐷 **Barcha hayvonlar teng... yoki shundaymi?**\n"
        "Hayvonlar fermasidagi qo‘zg‘olon orqali hokimiyat, propaganda, "
        "tenglik g‘oyalarining buzilishi va diktatura majoziy tarzda tasvirlanadi.\n\n"
        "💭 *Hokimiyat qo‘lga kirgach, ideallar saqlanib qoladimi?*",
        "photo": FSInputFile(r"D:\Telegram botlar\Kitob_bot\rasmlar\molxona.jpg"),
    },
    "badiiy_8": {
        "text": "📖 **Alkimyogar**\n"
        "✍️ **Muallif:** Paulo Koelyo\n\n"
        "✨ **Orzuing ortidan borishga jur’at etasanmi?**\n"
        "Yosh cho‘pon Santyago o‘zining katta orzusini izlab safarga chiqadi. "
        "Bu yo‘l uni nafaqat xazinaga, balki o‘zini anglashga ham olib boradi.\n\n"
        "💭 *Ba’zan izlayotgan narsamiz o‘zimizdan uzoq emas.*",
        "photo": FSInputFile(r"D:\Telegram botlar\Kitob_bot\rasmlar\alkimyogar.jpg"),
    },
    "badiiy_9": {
        "text": "📖 **Jinoyat va jazo**\n"
        "✍️ **Muallif:** Fyodor Dostoyevskiy\n\n"
        "🧠 **Jinoyatdan qochish mumkin. Vijdondan-chi?**\n"
        "Raskolnikovning jinoyatdan keyingi ruhiy kurashi, vijdon azobi va "
        "insonning o‘z qilmishi bilan yuzma-yuz kelishi tasvirlanadi.\n\n"
        "💭 *Inson o‘z vijdonidan qochib qutula oladimi?*",
        "photo": FSInputFile(
            r"D:\Telegram botlar\Kitob_bot\rasmlar\jinoyat va jazo.webp"
        ),
    },
    "badiiy_10": {
        "text": "📖 **Kichkina shahzoda**\n"
        "✍️ **Muallif:** Antuan de Sent-Ekzyuperi\n\n"
        "🌹 **Kattalar ko‘pincha eng muhim narsalarni unutib qo‘yadi.**\n"
        "Kichkina shahzodaning sayohati orqali do‘stlik, mehr, mas’uliyat va "
        "hayotning asl qadri haqida chuqur fikrlar beriladi.\n\n"
        "💭 *Siz hayotdagi eng muhim narsani ko‘ra olyapsizmi?*",
        "photo": FSInputFile(
            r"D:\Telegram botlar\Kitob_bot\rasmlar\kichkina shahzoda.webp"
        ),
    },
}

badiiy_kitob_sarlavha = {"text": """📚 **BADIIY KITOBLAR**

1. O‘tkan kunlar — Abdulla Qodiriy
2. Mehrobdan chayon — Abdulla Qodiriy
3. Kecha va kunduz — Cho‘lpon
4. Ikki eshik orasi — O‘tkir Hoshimov
5. Dunyoning ishlari — O‘tkir Hoshimov
6. 1984 — Jorj Oruell
7. Molxona — Jorj Oruell
8. Alkimyogar — Paulo Koelyo
9. Jinoyat va jazo — Fyodor Dostoyevskiy
10. Kichkina shahzoda — Antuan de Sent-Ekzyuperi

👇 *Mutolaa qilish uchun pastdagi tugmalardan birini bosing:*"""}


darsliklar = {
    "darslik_1": {
        "text": "📐 **Matematika**\n\n"
        "📚 Matematika faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Bilimni mustahkamlash uchun darslikdan foydalaning.*",
        "photo":""
    },
    "darslik_2": {
        "text": "⚛️ **Fizika**\n\n"
        "📚 Fizika faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Tabiat qonunlarini tushunishdan boshlang.*",
    },
    "darslik_3": {
        "text": "🧪 **Kimyo**\n\n"
        "📚 Kimyo faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Moddalar olamini o‘rganing.*",
    },
    "darslik_4": {
        "text": "🧬 **Biologiya**\n\n"
        "📚 Biologiya faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Tirik organizmlar sirlarini o‘rganing.*",
    },
    "darslik_5": {
        "text": "🌍 **Geografiya**\n\n"
        "📚 Geografiya faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Yer va uning tabiatini kashf eting.*",
    },
    "darslik_6": {
        "text": "📜 **Tarix**\n\n"
        "📚 Tarix faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *O‘tmishni bilish — bugunni anglashga yordam beradi.*",
    },
    "darslik_7": {
        "text": "🇬🇧 **Ingliz tili**\n\n"
        "📚 Ingliz tili faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Til o‘rganish — yangi imkoniyatlar eshigi.*",
    },
    "darslik_8": {
        "text": "📖 **Ona tili**\n\n"
        "📚 Ona tili faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Tilni yaxshi bilish — fikrni aniq ifodalashdir.*",
    },
    "darslik_9": {
        "text": "💻 **Informatika**\n\n"
        "📚 Informatika faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Texnologiyalar olamini o‘rganing.*",
    },
    "darslik_10": {
        "text": "⚖️ **Huquq**\n\n"
        "📚 Huquq faniga oid darsliklar va o‘quv materiallari.\n\n"
        "💡 *Huquq va majburiyatlaringizni biling.*",
    },
}


darslik_sarlavha = {"text": """📚 **DARSLIKLAR**

1. Matematika
2. Fizika
3. Kimyo
4. Biologiya
5. Geografiya
6. Tarix
7. Ingliz tili
8. Ona tili
9. Informatika
10. Huquq

👇 *Kerakli darslikni tanlash uchun pastdagi tugmalardan birini bosing:*"""}

it_kitoblar = {
    "it_1": {
        "text": "🐍 **Python**\n\n"
        "💻 Python dasturlash tilini o‘rganish uchun kitoblar.\n\n"
        "💡 *Sintaksisdan algoritmlargacha bo‘lgan bilimlarni mustahkamlang.*",
        "photo": "https://altair-rd.ru/uploads/icons/python_logo_png_1124133.webp",
    },
    "it_2": {
        "text": "🌐 **HTML & CSS**\n\n"
        "💻 Web sahifalar yaratish va ularni bezashga oid kitoblar.\n\n"
        "💡 *Web dasturlashning asoslarini o‘rganing.*",
        "photo": "https://static.tildacdn.com/tild6562-3834-4866-b162-363735653531/htmlcss.jpg",
    },
    "it_3": {
        "text": "⚡ **JavaScript**\n\n"
        "💻 Zamonaviy web dasturlash va JavaScript bo‘yicha kitoblar.\n\n"
        "💡 *Web sahifalarni interaktiv qiling.*",
        "photo": "https://poll2know.com/img/exams_photos/1682205605.jpg",
    },
    "it_4": {
        "text": "☕ **Java**\n\n"
        "💻 Java dasturlash tili va obyektga yo‘naltirilgan dasturlash bo‘yicha kitoblar.\n\n"
        "💡 *Mustahkam dasturlash asoslarini o‘rganing.*",
        "photo": "https://resizer.mail.ru/p/75baebcc-aab2-5e7c-83e5-ad948b1586ef/AQAKqOenBX1fuhbCQRy4JZ80eakPINL3tZdfqXZqLXgf1pRNn4capR2ijkWvY8Yu8EdJOLd96EK8DqHprHXbINDPRE0.jpg",
    },
    "it_5": {
        "text": "🔷 **C++**\n\n"
        "💻 C++ dasturlash tili, algoritmlar va ma'lumotlar tuzilmalari bo‘yicha kitoblar.\n\n"
        "💡 *Algoritmik fikrlashni rivojlantiring.*",
        "photo": "https://media.tproger.ru/uploads/2020/02/cpp-logo-cover.png",
    },
    "it_6": {
        "text": "🔵 **C#**\n\n"
        "💻 C# dasturlash tili va .NET texnologiyalari bo‘yicha kitoblar.\n\n"
        "💡 *Zamonaviy dasturlar yaratishni o‘rganing.*",
        "photo": "https://i.pinimg.com/originals/6e/46/e7/6e46e7dbe2bb73dacc055e5dbd85c3ad.png?nii=t",
    },
    "it_7": {
        "text": "🗄️ **SQL**\n\n"
        "💻 Ma'lumotlar bazasi va SQL so‘rovlarini o‘rganishga oid kitoblar.\n\n"
        "💡 *Ma'lumotlar bilan professional ishlashni o‘rganing.*",
        "photo": "https://habrastorage.org/webt/hh/ac/ed/hhacedu8okr3jeoi0i2awmpptyq.jpeg",
    },
    "it_8": {
        "text": "🐘 **PHP**\n\n"
        "💻 PHP va server tomon dasturlash bo‘yicha kitoblar.\n\n"
        "💡 *Backend dasturlash asoslarini o‘rganing.*",
        "photo": "https://codelab.pro/wp-content/uploads/2023/07/xynyljkh.jpg",
    },
    "it_9": {
        "text": "🦄 **Django**\n\n"
        "💻 Python asosidagi Django framework bo‘yicha kitoblar.\n\n"
        "💡 *Professional web ilovalar yaratishni o‘rganing.*",
        "photo": "https://i.ytimg.com/vi/VTOJmhKYoxE/maxresdefault.jpg",
    },
    "it_10": {
        "text": "⚛️ **React**\n\n"
        "💻 React va zamonaviy frontend dasturlash bo‘yicha kitoblar.\n\n"
        "💡 *Interaktiv va zamonaviy interfeyslar yarating.*",
        "photo": "https://intrid.ru/files/image/cache/Pages/Page155/160c366be2-1.webp",
    },
}


it_kitoblar_sarlavha = {"text": """💻 **IT KITOBLAR**

1. Python
2. HTML & CSS
3. JavaScript
4. Java
5. C++
6. C#
7. SQL
8. PHP
9. Django
10. React

👇 *Kerakli IT kitobni tanlash uchun pastdagi tugmalardan birini bosing:*"""}

kitob_muhokama = {
    "text":"Bu kitob haqida muhokama qilishga tayyorman 😊\nQanday savolingiz bor?"
    }
