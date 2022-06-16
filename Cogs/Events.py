import discord
from discord.ext import commands
from better_profanity import profanity
from discord.utils import get

logschannel = 985624507580563474

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as ', self.bot.user)

    @commands.Cog.listener()
    async def on_message(self, message):
        disabledChannels = [985624507580563473, 985624507580563474]
        logs = get(message.guild.channels, id = logschannel)
        channel = message.channel
        embed = discord.Embed(title = "Profanity filter", description = f"{message.author.mention} profanity is not allowed in this channel!")
        badword = profanity.contains_profanity(message.content)
        if badword == True:
            if message.channel.id in disabledChannels:
                pass
            else:
                await message.delete()
                await channel.send(embed=embed, delete_after = 5)
                profanityEmbed = discord.Embed(title = "Profanity warning", description = f"{message.author} expressed profanity in {message.channel.mention}\n\n**Message:** {message.content}", color = 0xff0000)
                profanityEmbed.add_field(name="Important!", value="This is not an official warning to the user, if you want to punish the user use the warn command!")
                await logs.send(embed=profanityEmbed)


async def setup(bot):
    await bot.add_cog(Events(bot))