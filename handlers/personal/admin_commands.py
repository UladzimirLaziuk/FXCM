from aiogram import types
from aiogram import Router

from fxcm_start import start_server

router = Router()
connection = None

@router.message(commands=['start', 'help'])
async def send_welcome(message: types.Message, *args, **kwargs):
    bot_objects = kwargs.get('bot')
    bot = await bot_objects.get_me()
    # await commands_list_menu(db)
    """ This handlers will be called when user sends `/start` or `/help` command   """
    await message.reply(f"Hi!\nI'm {bot.first_name}!\n")

@router.message(commands=['start_server'])
async def send_welcome(message: types.Message, *args, **kwargs):
    global connection
    bot_objects = kwargs.get('bot')
    bot = await bot_objects.get_me()

    connection = start_server()

    # await commands_list_menu(db)
    """ This handlers will be called when user sends `/start` or `/help` command   """
    await message.reply(f"Hi!Start server\nI'm {bot.first_name}!\n")

@router.message(commands=['stop_server'])
async def send_welcome(message: types.Message, *args, **kwargs):
    global connection
    bot_objects = kwargs.get('bot')
    bot = await bot_objects.get_me()
    # await commands_list_menu(db)
    if connection:
        connection.close()
    """ This handlers will be called when user sends `/start` or `/help` command   """
    await message.reply(f"Goodbuy!\nI'm {bot.first_name}!\n")


@router.message()
async def echo_handler(message: types.Message, *arqs, **kwargs) -> None:
    """
    Handler will forward received message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker and etc.)
    """
    try:
        # Send copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")