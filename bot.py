
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في بوت تحليل المنشورات.\n\n"
        "أرسل نصاً أو صورة وسأقوم بتحليلها."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    score = 50

    if len(text) > 50:
        score += 10

    if "!" in text:
        score += 10

    if "الذهب" in text:
        score += 10

    result = f"""
📊 تقييم المنشور: {score}/100

✅ نقاط القوة:
- يحتوي على محتوى جيد

⚠️ التحسينات:
- أضف دعوة للاشتراك
- استخدم عنواناً أقصر
- أضف أرقاماً أو إحصائيات
"""

    await update.message.reply_text(result)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📷 تم استلام الصورة.\n"
        "نسخة التحليل المتقدمة تحتاج ربط OpenAI Vision."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    app.run_polling()

if __name__ == "__main__":
    main()
