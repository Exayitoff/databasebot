import logging
from aiogram import Bot, Dispatcher, executor, types
from db import Database
logging.basicConfig(level=logging.INFO)
bot =   Bot(token="1826428249:AAFMIuI7TjdZcZsnf0e35Cwh53FVltYsm7g")
dp = Dispatcher(bot)
db = Database('database.db')
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
  if message.chat.type == 'private':
    if not db.user_exists(message.from_user.id):
      db.add_user(message.from_user.id)
    await bot.send_message(chat_id=message.from_user.id, text="Xush kelibsiz "+message.from_user.first_name)

@dp.message_handler(commands=["sendall"])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
      if message.from_user.id == 693313498:
        text = message.text[9:]
        users = db.get_users()
        for row in users:
          try:
            await bot.send_message(chat_id=row[0], text=text)
            if int(row[1]) !=1:
              db.set_active(user_id=row[0], active=1)
          except:
            db.set_active(user_id=row[0], active=0)
        await bot.send_message(chat_id=message.from_user.id, text="Xabar muvaffaqiyatli yuborildi.")



if __name__ == "__main__":
  executor.start_polling(dp,skip_updates=True)