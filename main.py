import logging
from tkinter.constants import CURRENT

#import requests
from aiogram import Bot, Dispatcher,types,executor

API_TOKEN="7607664066:AAGjR9vQKNc4WOmqhexttCd9qVmCg8qGrx0"

logging.basicConfig(level=logging.INFO)



bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

#start kamondasi uchun handler
@dp.message_handler(commands="start")
async def start_handler(message:types.Message):
     username=message.from_user.first_name
     text=f"Assalomu alaykum {username}\n\n"
     text+=f"Valyuta kurslari telegram botiga xush kelibsiz"
     await message.answer(text)



@dp.message_handler(commands="valyuta")
async def valyuta_course(message:types.Message):

    request=requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    response=request.json()



    text=f"Sana: {response[0]['Date']}\n\n"
    CURRENSY=['US','EUR','RUB','EPG']
    for i in response:
        if i['Ccy'] in CURRENSY:
            text+=f" 1{i['CctNm_UZC']}  ~  {i['Rate']} so`m\n"
    await message.answer(text)



if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)

