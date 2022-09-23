import asyncio
import os

from aiogram import Bot, Dispatcher, types
from magic_filter import F
from dotenv import load_dotenv
from handlers.personal import admin_commands

load_dotenv(dotenv_path='.env')
API_TOKEN = os.getenv('API_TELEGRAM_TOKEN')
ADMIN_ID = os.getenv('API_TELEGRAM_TOKEN')


async def setup_bot_commands(bot, *args):

    bot_commands = [
        types.BotCommand(command="/start", description="Start bot)"),
        types.BotCommand(command="/help", description="Get info about me"),
        types.BotCommand(command="/start_server", description="Start server"),
        types.BotCommand(command="/stop_server", description="Stop server"),
        ]
    await bot.set_my_commands(bot_commands)



async def main() -> None:
    # Initialize bot and dispatcher
    bot = Bot(API_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    # Add admin filter to admin_router
    if ADMIN_ID.isdigit():
        admin_commands.router.message.filter(F.chat.id == ADMIN_ID)
    dp.include_router(admin_commands.router)
    await setup_bot_commands(bot)
    # [optional] Skip pending updates
    # await bot.delete_webhook(drop_pending_updates=True)
    # Run polling
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())