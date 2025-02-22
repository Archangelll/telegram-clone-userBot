"""
https://my.telegram.org/auth para pegar as chaves API
"""


from pyrogram import Client

from asyncio import run
import asyncio

from time import sleep

fromChatGLOBAL = ''
toChatGLOBAL   = ''

api_id_global   = 0
api_hash_global = 0

app = Client(
	'userBotDLClone',
	api_id=api_id_global,
	api_hash=api_hash_global
)

funcTrue   = lambda x: True

async def main():
	global fromChatGLOBAL, toChatGLOBAL

	await app.start()

	print('============\nPine os dois grupos nas conversas\n============')
	input('Assim q pinar de Enter')

	##get_pinned_chats
	chats = {}

	#### update chat list
	# ['chat']['type'] # "ChatType.CHANNEL" or ChatType.GROUP or ChatType.SUPERGROUP
	# ['chat']['id']
	async for dialog in app.get_dialogs():
		#if dialog.chat.type == ChatType.GROUP or dialog.chat.type == ChatType.SUPERGROUP:
		if dialog.is_pinned: # vms pegar só os chat pinados
			chats[dialog.chat.id] = dialog.chat.title # id do chat q vamos clonar
			print(dialog.chat.type, dialog.chat.title)
		print('=============')
	print(chats)
	print('++++++++++++++')
	#### update chat list

	fromChatGLOBAL = input('Digite o ID do chat a ser clonado: ')
	toChatGLOBAL   = input('Digite o ID do chat novo: ')

	##get_pinned_chats

	##clone_chats
	# i = input('Digite o id a ser copiado: [ID/n]: ').upper()
	quant = int(input('quantas mensagens deseja copiar ? '))

	for i in range(1, quant + 1):
		await app.get_messages(fromChatGLOBAL, int(i))
		try:
			await app.copy_message(toChatGLOBAL, fromChatGLOBAL, int(i))
			print('sucess')
		except Exception as error:
			print(error)
	##clone_chats


	print('run sucessfully')
	
	await app.stop()

app.run(main())
print('BOT FOI DESLIGADO')