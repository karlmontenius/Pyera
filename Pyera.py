import discord
from discord.ext import commands
import asyncio
from better_profanity import profanity

#--------------DEFINITIONS-------------------------------------------------------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)
bot.owner_ids = [238834157181075456]
startup_extensions = ["Cogs.Music",
                      "Cogs.Commands",
                      "Cogs.Supportive",
                      "Cogs.Events"]
                      
#-------------------READY------------------------------------------------------------------------------------------
async def loader():
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                await bot.load_extension(extension)
                print(f"{extension} loaded")
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))

async def main():
    await loader()
    profanity.load_censor_words()
    await bot.start('ODU5MDk2NjE1MDYzMjU3MDk4.G6vIJW.QKz1PyTrTIEW7EqGYHF1nrLMyl0XjzMoBuNOQc')



asyncio.run(main())