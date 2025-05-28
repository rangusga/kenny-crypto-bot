from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Fungsi ketika /start diketik
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selamat datang di Kenny’s Crypto Auto Bot! Ketik /invest untuk mulai.")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7111276849:AAHf5IUnrSZ2HhN-SQNLsZSeVzZV8YU86Jo").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
