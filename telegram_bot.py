# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup


def echo(update, context):
    update.message.reply_text('''Error 00000000000000000000000000000
    A problem has been detected and Android has been shut down to prevent damage
to your computer.

The problem seems to be caused by the following file: xNtKrnl.exe

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED

If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps:

Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Windows updates you might need.

If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use safe mode to remove or disable components, restart
your computer, press F8 to select Advanced Startup Options, and then
select Safe Mode.

Technical Information:

*** STOP: 0x1000007e (0xffffffffc0000005, 0xfffff80002e55151, 0xfffff880009a99d8,
0xfffff880009a9230)

*** xNtKrnl.exe - Address 0xfffff80002e55151 base at 0xfffff80002e0d000 DateStamp
0x4ce7951a
''')


def main():
    REQUEST_KWARGS = {
        'proxy_url': 'socks5://148.251.234.93:1080'}

    updater = Updater('1242649621:AAH0aGPCowr8TVQ2F-zizFJn3JZK0qLkd5Y', use_context=True,
                      request_kwargs=REQUEST_KWARGS)

    dp = updater.dispatcher

    def start(update, context):
        update.message.reply_text(
            "Привет! Че надо?")

    def help(update, context):
        update.message.reply_text(
            "Комманды: /help, /phone, /site")

    def phone(update, context):
        update.message.reply_text("Телефон: Не дам")

    def site(update, context):
        update.message.reply_text(
            "Сайт: Нема")
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()