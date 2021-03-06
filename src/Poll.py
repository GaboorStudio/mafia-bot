import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler


class Poll:

    def __init__(self, title, votes_list, sent_id, state):
        self.sent_id = sent_id
        self.votes_list = votes_list
        self.title = title
        self.keyboard = []
        if state == "night":
            self.init_keyboard_night()
        else:
            self.init_keyboard_day()

    def send_poll(self, context: telegram.ext.CallbackContext):
        return context.bot.send_message(chat_id=self.sent_id, text=self.title,
                                        reply_markup=self.reply_markup, parse_mode="Markdown")

    def reset(self):
        self.sent_id = None
        self.title = None
        self.keyboard = []
        self.reply_markup = None

    def set_asked_player(self, sent_id):
        self.sent_id = sent_id

    def set_title(self, title):
        self.title = title

    def init_keyboard_day(self):
        for vote in self.votes_list:
            self.keyboard.append(
                [InlineKeyboardButton(vote, callback_data=vote)])
        self.reply_markup = InlineKeyboardMarkup(self.keyboard)

    def init_keyboard_night(self):
        for vote in self.votes_list:
            self.keyboard.append(
                [InlineKeyboardButton(vote.name, callback_data=vote.user_id)])
        self.reply_markup = InlineKeyboardMarkup(self.keyboard)

    def sicktir_poll(self, context: telegram.ext.CallbackContext):
        context.bot.edit_message_text()
