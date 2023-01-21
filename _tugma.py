from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from main import *
mainMenu = InlineKeyboardMarkup(row_width=2)
bolm2 = InlineKeyboardMarkup(row_width=2)
bolm3 = InlineKeyboardMarkup(row_width=2)
bolm4 = InlineKeyboardMarkup(row_width=2)
adminMenu = InlineKeyboardMarkup(row_width=2)
btnRandom = InlineKeyboardButton(text="Kuchuklar 🐕"  , callback_data="btnRandom" )
btnRandom2 = InlineKeyboardButton(text="Mushuklar 🐈‍" , callback_data="btnRandom2")
btnRandom3 = InlineKeyboardButton(text="Ilonlar 🐍" , callback_data="btnRandom3")
btnRandom4 = InlineKeyboardButton(text="Quyonlar  🐇" , callback_data="btnRandom4")
btnRandom5 = InlineKeyboardButton(text="Sichqonlar  🐁" , callback_data="btnRandom5")
btnRandom6 = InlineKeyboardButton(text="Qushlar  🦚" , callback_data="btnRandom6")
statik = InlineKeyboardButton(text="Statistika 📊"  , callback_data="stats" )
foydalanuvchilar = InlineKeyboardButton(text="Foydalanuvchilar 👥" , callback_data="userfayl")
ikkibol = InlineKeyboardButton(text="Boshqa hayvonlar rasmi 🦫"  , callback_data="boshqa" )
uchbol = InlineKeyboardButton(text="Boshqa hayvonlar rasmi 🏕"  , callback_data="boshqa2" )

mainMenu.row(btnRandom, btnRandom2)
mainMenu.row(btnRandom3,btnRandom4)
mainMenu.row(btnRandom5,btnRandom6)
mainMenu.add(ikkibol)
# mainMenu.add(statik)



xabar_yuborish = InlineKeyboardButton(text="Xabarlar ✍️"  , callback_data="sendmsg" )
statlar = InlineKeyboardButton(text="Statistika 📊"  , callback_data="stats" )
adminMenu.insert(xabar_yuborish)
adminMenu.add(statlar)
adminMenu.add(foydalanuvchilar)


ikkibolm1 = InlineKeyboardButton(text="Otlar 🐎"  , callback_data="otlar" )
ikkibolm2 = InlineKeyboardButton(text="Pandalar 🐼"  , callback_data="pandalar" )
ikkibolm3 = InlineKeyboardButton(text="Pingvinlar 🐧"  , callback_data="pinvgin" )
ikkibolm4 = InlineKeyboardButton(text="Sherlar 🦁 "  , callback_data="sherlar" )
ikkibolm5 = InlineKeyboardButton(text="Tovuslar 🦚 "  , callback_data="tovus" )
ikkibolm6 = InlineKeyboardButton(text="Tovuqlar 🐓 "  , callback_data="tovuq" )
ikkibolm7 = InlineKeyboardButton(text="Orqaga 🔙 "  , callback_data="ortga" )
bolm2.row(ikkibolm1,ikkibolm2)
bolm2.row(ikkibolm3,ikkibolm4)
bolm2.row(ikkibolm5,ikkibolm6)
bolm2.add(uchbol)
bolm2.add(ikkibolm7)

uchbolm1 = InlineKeyboardButton(text="Sigir 🐄"  , callback_data="sigir" )
uchbolm2 = InlineKeyboardButton(text="Bo\'rilar 🐺"  , callback_data="bori" )
uchbolm3 = InlineKeyboardButton(text="Leopard 🐆"  , callback_data="gepard" )
uchbolm4 = InlineKeyboardButton(text="Fillar 🐘 "  , callback_data="fil" )
uchbolm5 = InlineKeyboardButton(text="Kenguru 🦘 "  , callback_data="kenguru" )
uchbolm6 = InlineKeyboardButton(text="Kiyiklar 🦌 "  , callback_data="kiyik" )
uchbolm7 = InlineKeyboardButton(text="Orqaga 🔙 "  , callback_data="ortga" )
bolm3.row(uchbolm1,uchbolm2)
bolm3.row(uchbolm3,uchbolm4)
bolm3.row(uchbolm5,uchbolm6)
bolm3.add(uchbolm7)


reklam = InlineKeyboardMarkup(row_width=2)

rekbtn = InlineKeyboardButton(text="Kirish ✅", url="https://t.me/hayvonlar_rasmibot" )
reklam.add(rekbtn)
