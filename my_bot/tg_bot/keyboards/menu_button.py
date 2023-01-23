from aiogram import Dispatcher, types


# Функция для настройки кнопки Menu бота
async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Начать'),
        types.BotCommand(command='/help', description='Справка'),

    ]
    await dp.bot.set_my_commands(main_menu_commands)