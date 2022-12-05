from tg_botting.bot import Bot

token = ''
user_id= ''
user_hash = ''

bot = Bot(['!'],user_id,user_hash)

@bot.command('ping')
async def ping(message):
    await message.reply('pong')

bot.run(token)