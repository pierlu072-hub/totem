import os
from flask import Flask, request
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def start(update, context):
    await update.message.reply_text("Bot attivo")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT, echo))

@app.route("/", methods=["GET"])
def home():
    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(force=True)
    application.update_queue.put(update)
    return "OK"

if __name__ == "__main__":
    application.run_polling()
