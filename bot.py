from telegram.ext import Updater, MessageHandler, Filters
import random

TOKEN = "8463731320:AAEj3LmAmmJjaeqe3geqnlLXYi2rEuRoxmc"

responses = {
    "hello": ["Hello 👋", "Hi there!", "Hey! How are you?"],
    "how are you": ["Doing great.", "All good.", "Focused and growing."],
    "bye": ["Goodbye.", "See you.", "Stay strong."]
}

default_replies = [
    "Interesting.",
    "That makes sense.",
    "Tell me more.",
    "I agree.",
    "Good thought."
]

def chat(update, context):
    text = update.message.text.lower()

    for key in responses:
        if key in text:
            update.message.reply_text(random.choice(responses[key]))
            return

    update.message.reply_text(random.choice(default_replies))

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

updater.start_polling()
updater.idle()
