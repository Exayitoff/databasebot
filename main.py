import logging
from aiogram import Bot, Dispatcher, executor, types
from db import Database
import _tugma as nav
import requests
import random
from _tugma import *
logging.basicConfig(level=logging.INFO)
bot =   Bot(token="5860263373:AAGfShT7P4YDb3A8caV5QbKwZ3HICQfqdbU")
dp = Dispatcher(bot)
db = Database('database.db')
admin = 693313498
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
  if message.chat.type == 'private':
    if not db.user_exists(message.from_user.id):
      db.add_user(message.from_user.id)
    await bot.send_photo(message.from_user.id, "https://w0.peakpx.com/wallpaper/368/742/HD-wallpaper-cool-cat.jpg", caption=" <i>Assalomu alaykum </i> <b>"+message.from_user.first_name + "</b> <i>hush kelibsiz bo'limlardan birini tanlang va sizga bot qiziqarli rasmlar jo\'natadi \nbot 3.0 versiyada ishlamoqda</i>",parse_mode="HTML", reply_markup=nav.mainMenu)


@dp.message_handler(commands=["sendall"])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
      if message.from_user.id == admin:
        text = message.text[9:]
        users = db.get_users()
        print(sum(1 for line in users))
        for row in users:
          try:
            await bot.send_message(chat_id=row[0], text=text)
            if int(row[1]) !=1:
              db.set_active(user_id=row[0], active=1)
          except:
            db.set_active(user_id=row[0], active=0)
        await bot.send_message(chat_id=message.from_user.id, text="Xabar muvaffaqiyatli yuborildi.")

@dp.message_handler(commands=['admin'])
async def admin_panel(message : types.Message):
    if message.from_user.id == admin:
      await bot.send_photo(admin, "https://sliderzemo.cf/img/p3.jpg", caption="Salom Ezozbek hush kelibsiz Bot amringizga muntazir 😁",  reply_markup=nav.adminMenu)
    else:
      await bot.send_message(chat_id=message.from_user.id, text="<i> Kechirasiz </i> <b>" + str(message.from_user.first_name) + "</b> <i> siz admin emassiz 😝 \n \n Bot admini: @MrXayitov </i>", parse_mode="HTML")

@dp.callback_query_handler(text="btnRandom")
async def randomize(calb: types.CallbackQuery):
          link = 'https://dog.ceo/api/breeds/image/random'
          response = requests.get(link)
          itlar= response.json()
          xbr=itlar['message']
          await bot.send_photo(calb.from_user.id, xbr , caption="Kuchuklar ❤️", reply_markup=nav.mainMenu)





@dp.callback_query_handler(text="btnRandom2")
async def randomize(calb: types.CallbackQuery):  
          link = 'https://api.thecatapi.com/v1/images/search?limit=1'
          response = requests.get(link)
          itlar= response.json()
          xbr=""
          for i in itlar :
            xbr+=i['url']
          await bot.send_photo(calb.from_user.id, xbr , caption="Mushuklar ❤️", reply_markup=nav.mainMenu)


@dp.callback_query_handler(text="btnRandom3")
async def randomize(calb: types.CallbackQuery):  
        taxmin = random.randint(1, 19)
        link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=snakes&image_type=photo&pretty='+str(taxmin)
        response = requests.get(link)
        itlar= response.json()
        hts = itlar["hits"]
        lists = []
        for n in hts:
          lists.append(n["largeImageURL"])
        await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Ilonlar 🐍", reply_markup=nav.mainMenu)
@dp.callback_query_handler(text="btnRandom4")
async def randomize(calb: types.CallbackQuery):
        taxmin = random.randint(1, 20)
        link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=rabbit&image_type=photo&pretty='+str(taxmin)
        response = requests.get(link)
        itlar= response.json()
        hts = itlar["hits"]
        lists = []
        for n in hts:
          lists.append(n["largeImageURL"])
        await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Quyonlar 🐇", reply_markup=nav.mainMenu)


@dp.callback_query_handler(text="btnRandom5")
async def randomize(calb: types.CallbackQuery):  
        taxmin = random.randint(1, 20)
        link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=animal+mouse&image_type=photo&pretty='+str(taxmin)
        response = requests.get(link)
        itlar= response.json()
        hts = itlar["hits"]
        lists = []
        for n in hts:
          lists.append(n["largeImageURL"])
        await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Sichqonlar  🐁", reply_markup=nav.mainMenu)

@dp.callback_query_handler(text="btnRandom6")
async def randomize(calb: types.CallbackQuery): 
        taxmin = random.randint(1, 19)
        link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=birds&image_type=photo&pretty='+str(taxmin)
        response = requests.get(link)
        itlar= response.json()
        hts = itlar["hits"]
        lists = []
        for n in hts:
          lists.append(n["largeImageURL"])
        await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Qushlar  🦚", reply_markup=nav.mainMenu)
@dp.callback_query_handler(text="boshqa")
async def randomize(calb: types.CallbackQuery): 
        await bot.send_photo(chat_id=calb.from_user.id, photo="https://i.pinimg.com/564x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg", caption=" <i>Assalomu alaykum </i> <b>"+calb.from_user.first_name + "</b> <i>hush kelibsiz bo'limlardan birini tanlang va sizga bot qiziqarli rasmlar jo\'natadi</i>",parse_mode="HTML", reply_markup=nav.bolm2)

@dp.callback_query_handler(text="otlar")
async def randomize(calb: types.CallbackQuery):  
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=horses&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Otlar 🐎", reply_markup=nav.bolm2)
@dp.callback_query_handler(text="pandalar")
async def randomize(calb: types.CallbackQuery): 
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=white+panda&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Pandalar 🐼", reply_markup=nav.bolm2)
@dp.callback_query_handler(text="pinvgin")
async def randomize(calb: types.CallbackQuery):  
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=pinguin&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Pingvinlar 🐧", reply_markup=nav.bolm2)
@dp.callback_query_handler(text="sherlar")
async def randomize(calb: types.CallbackQuery):  
        taxmin = random.randint(1, 19)
        link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=lion&image_type=photo&pretty='+str(taxmin)
        response = requests.get(link)
        itlar= response.json()
        hts = itlar["hits"]
        lists = []
        for n in hts:
          lists.append(n["largeImageURL"])
        await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Sherlar 🦁", reply_markup=nav.bolm2)
@dp.callback_query_handler(text="tovus")
async def randomize(calb: types.CallbackQuery):  
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=peacock&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Tovuslar 🦚", reply_markup=nav.bolm2)
 
@dp.callback_query_handler(text="tovuq")
async def randomize(calb: types.CallbackQuery):            
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=chicken&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Kulguli Tovuqlar 🐓 ", reply_markup=nav.bolm2)
@dp.callback_query_handler(text="ortga")
async def randomize(calb: types.CallbackQuery):        
        await bot.send_photo(chat_id=calb.from_user.id, photo="https://w0.peakpx.com/wallpaper/368/742/HD-wallpaper-cool-cat.jpg", caption="Siz orqaga qaytdingiz 😜", reply_markup=nav.mainMenu)

@dp.callback_query_handler(text="stats")
async def randomize(calb: types.CallbackQuery):  
        users = db.get_users()
        son=sum(1 for line in users)
        await bot.send_message(chat_id=calb.message.chat.id, text="<i>👨🏻‍💻 Obunachilar soni - </i> <b>"+str(son)+" </b>  ta. \n \n📊@hayvonlar_rasmibot  <i> statistikasi  </i>",parse_mode="HTML")        
@dp.callback_query_handler(text="userfayl")
async def randomize(calb: types.CallbackQuery):
        users = db.get_users()
        od=[line for line in users]
        await bot.send_message(chat_id=admin , text=str(od))
        
@dp.callback_query_handler(text="boshqa2")
async def randomize(calb: types.CallbackQuery):  
        await bot.send_photo(chat_id=calb.from_user.id, photo="https://mobimg.b-cdn.net/v3/fetch/c7/c78069a2d7416ad906cc92b05a71c082.jpeg", caption="Ajoyib siz endi 3-bo'limdasiz \nHayvonlardan birini tanlang", reply_markup=nav.bolm3)
      
@dp.callback_query_handler(text="sigir")
async def randomize(calb: types.CallbackQuery):        
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=cow&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Sigirlar 🐄 ", reply_markup=nav.bolm3)
@dp.callback_query_handler(text="bori")
async def randomize(calb: types.CallbackQuery):     
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=wolf&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Bo\'rilar 🐺", reply_markup=nav.bolm3)   
@dp.callback_query_handler(text="gepard")
async def randomize(calb: types.CallbackQuery):        
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=leopard&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Leopard 🐆", reply_markup=nav.bolm3)
@dp.callback_query_handler(text="fil")
async def randomize(calb: types.CallbackQuery):   
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=elephant&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Fillar 🐘", reply_markup=nav.bolm3)     
@dp.callback_query_handler(text="kenguru")
async def randomize(calb: types.CallbackQuery):  
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=kangaroo&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Kenguru 🦘", reply_markup=nav.bolm3)      
@dp.callback_query_handler(text="kiyik")
async def randomize(calb: types.CallbackQuery): 
          taxmin = random.randint(1, 19)
          link = 'https://pixabay.com/api/?key=32452369-fb4ecba71876a7c19595878f8&q=deer&image_type=photo&pretty='+str(taxmin)
          response = requests.get(link)
          itlar= response.json()
          hts = itlar["hits"]
          lists = []
          for n in hts:
            lists.append(n["largeImageURL"])
          await bot.send_photo(calb.from_user.id, lists[taxmin] , caption="Kiyiklar 🦌", reply_markup=nav.bolm3) 



if __name__ == "__main__":
  executor.start_polling(dp,skip_updates=True)
