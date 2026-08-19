import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Sizning tokeningiz va ID raqamingiz to'g'ridan-to'g'ri joylandi:
TOKEN = "8742411514:AAHCvgknNZzanOqD18VkDRWpBHz33_89w5M"
ADMIN_ID = 8007029227

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start komandasi
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Kurslarni ko'rish", callback_data="show_courses")
    await message.answer(
        "Assalomu alaykum! O'quv markazimizga xush kelibsiz. Quyidagi tugma orqali kurslarimiz bilan tanishing:",
        reply_markup=builder.as_markup()
    )

# Kurslar ro'yxati
@dp.callback_query(F.data == "show_courses")
async def show_courses(callback: types.CallbackQuery):
    text = (
        "Bizdagi kurslar:\n"
        "1. Matematika (Asosiy / Majburiy / Online)\n"
        "2. Ona tili\n"
        "3. Ingliz tili\n"
        "4. Fizika\n"
        "5. Prezident maktabiga tayyorlov\n\n"
        "Ro'yxatdan o'tish uchun telefon raqamingizni yuboring (masalan: +998901234567)."
    )
    await callback.message.edit_text(text)
    await callback.answer()

# Telefon raqam yoki xabar yuborilganda adminchaga jo'natish
@dp.message(F.text.regexp(r'\+?\d+')) 
async def handle_contact(message: types.Message):
    # Arizani to'g'ridan-to'g'ri sizga (admin ID ga) yuboradi
    await bot.send_message(
        ADMIN_ID, 
        f"📩 Yangi ariza:\nFoydalanuvchi: {message.from_user.full_name}\nUsername: @{message.from_user.username}\nTelefon/Ma'lumot: {message.text}"
    )
    await message.answer("Rahmat! Arizangiz qabul qilindi, adminlarimiz tez orada siz bilan bog'lanishadi.")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())