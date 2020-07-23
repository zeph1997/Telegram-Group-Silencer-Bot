import telebot

TOKEN = "Your Telegram API Token"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(m):
    # If bot is not admin, then it will not be able to delete message.
    try:
        bot.delete_message(m.chat.id,m.message_id)
    except:
        if m.new_chat_member.id != bot.get_me().id:
            bot.send_message(m.chat.id,"Please make me an admin in order for me to remove the join and leave messages on this group!")
        else:
            bot.send_message(m.chat.id,"Hi! I am your trusty GroupSilencer Bot! Thanks for adding me! To use me, make me an admin and I will be able to delete all the pesky notification when a member joins or leaves the group!")
        
@bot.message_handler(content_types=['left_chat_member'])
def delete_leave_message(m):
    # If bot is the one that is being removed, it will not be able to delete the leave message.
    if m.left_chat_member.id != bot.get_me().id:
        try:
            bot.delete_message(m.chat.id,m.message_id)
        except:
            bot.send_message(m.chat.id,"Please make me an admin in order for me to remove the join and leave messages on this group!")

bot.polling()