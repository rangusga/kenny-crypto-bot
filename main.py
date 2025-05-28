import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Fungsi ketika pengguna mengetik /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Ini Kenny’s Crypto Auto Bot.\nKetik /invest untuk mulai investasi.")

# Ambil token dari Railway
TOKEN = os.getenv("BOT_TOKEN")

# Jalankan bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
