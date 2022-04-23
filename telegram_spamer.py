from pyrogram import Client, filters
import os, pyfiglet
os.system("cls")
print("""Script by CLOTI(Xsarz)
Github : https://github.com/xXxCLOTIxXx""")
print(pyfiglet.figlet_format("Telegram Spamer", font="eftitalic"))
while True:
	try:
		print("Получить айди и хэш можно тут: https://my.telegram.org/auth")
		api_id = input("Введите ваш айди>> ")
		api_hash = input("Введите ваш Хэш>> ")
		app = Client("account", api_id, api_hash)
		break
	except:
		print("\n\n\nОшибка, неверные данные\nПолучить айди и хэш можно тут: https://my.telegram.org/auth\n\n\n")

text = str(input("\n\nВведите сообщение для рейда>>"))
print("\n\n\nДля начала спама напишите /start в нужный чат")
@app.on_message(filters.command('start', prefixes='/') & filters.me)
async def spam(_, message):
	try:
		while True:
			await message.reply_text(text)
	except Exception as ex:
		print(f"Произошла ошибка!\n\n{ex}")
app.run()

