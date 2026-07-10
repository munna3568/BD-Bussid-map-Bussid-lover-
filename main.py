from telegram.ext import Application
from config import BOT_TOKEN


def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN পাওয়া যায়নি!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    print("BD Bussid Map Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
