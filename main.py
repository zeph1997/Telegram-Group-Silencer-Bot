import telebot

TOKEN = "Your Telegram API Token"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members','left_chat_member'])
def delete_join_leave_message(m):
    # If bot is not admin, then it will not be able to delete message.
    try:
        bot.delete_message(m.chat.id,m.message_id)
    except:
        bot.send_message(m.chat.id, "Please make me an admin in order for me to remove the join and leave messages on this group!")
        
bot.polling()