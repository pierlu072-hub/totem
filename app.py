import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot attivo")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, echo))
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

