import discord
from discord.ext import commands
from discord.utils import get
import re
import mysql.connector


mydb = mysql.connector.connect(
  host="66.11.118.47",
  user="u2422_VEWl4C9eF3",
  password="K=1LLXB=sRP5S4vPYgMlpILJ",
  database="s2422_pyeradb"
)

class Supportive(commands.Cog, description="Supportive cog for space taking code."):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

#---------------------------------------------------------------------------------------------------------------------------
    async def games(self, ctx):
        Overwatch = get(ctx.guild.roles, name="Overwatch")
        League = get(ctx.guild.roles, name="League of Legends")
        Elden = get(ctx.guild.roles, name="Elden Ring")
        Arma = get(ctx.guild.roles, name="Arma Reforger")
        CSGO = get(ctx.guild.roles, name="Counter Strike: Global Offensive")
        Valorant = get(ctx.guild.roles, name="Valorant")
        Squad = get(ctx.guild.roles, name="Squad")
        CrusaderKings = get(ctx.guild.roles, name="Crusader Kings")
        RocketLeague = get(ctx.guild.roles, name="Rocket League")
        HumanFallFlat = get(ctx.guild.roles, name="Human Fall Flat")
        WarThunder = get(ctx.guild.roles, name="War Thunder")
        Battlefield = get(ctx.guild.roles, name="Battlefield")
        channel = get(ctx.guild.text_channels, name="get-your-roles")

        class my_games(discord.ui.View):
            @discord.ui.button(label = "Overwatch", style=discord.ButtonStyle.gray, custom_id = "Overwatch")
            async def Overwatch(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Overwatch in userRoles:
                    await user.remove_roles(Overwatch)
                    await interaction.response.send_message("Removed Overwatch!", ephemeral=True)
                else:
                    await user.add_roles(Overwatch)
                    await interaction.response.send_message("Added Overwatch!", ephemeral=True)

            @discord.ui.button(label = "League of Legends", style=discord.ButtonStyle.gray, custom_id = "Orange")
            async def League(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if League in userRoles:
                    await user.remove_roles(League)
                    await interaction.response.send_message("Removed League of Legends!", ephemeral=True)
                else:
                    await user.add_roles(League)
                    await interaction.response.send_message("Added League of Legends!", ephemeral=True)

            @discord.ui.button(label = "Elden Ring", style=discord.ButtonStyle.gray, custom_id = "Elden Ring")
            async def Elden(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Elden in userRoles:
                    await user.remove_roles(Elden)
                    await interaction.response.send_message("Removed Elden Ring!", ephemeral=True)
                else:
                    await user.add_roles(Elden)
                    await interaction.response.send_message("Added Elden Ring!", ephemeral=True)

            @discord.ui.button(label = "Arma Reforger", style=discord.ButtonStyle.gray, custom_id = "Arma Reforger")
            async def Arma(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Arma in userRoles:
                    await user.remove_roles(Arma)
                    await interaction.response.send_message("Removed Arma Reforger!", ephemeral=True)
                else:
                    await user.add_roles(Arma)
                    await interaction.response.send_message("Added Arma Reforger!", ephemeral=True)

            @discord.ui.button(label = "Counter Strike: Global Offensive", style=discord.ButtonStyle.gray, row = 2, custom_id = "Counter Strike: Global Offensive")
            async def CSGO(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                CSGO = get(ctx.guild.roles, name="Counter Strike: Global Offensive")
                userRoles = interaction.user.roles
                if CSGO in userRoles:
                    await user.remove_roles(CSGO)
                    await interaction.response.send_message("Removed Counter Strike: Global Offensive!", ephemeral=True)
                else:
                    await user.add_roles(CSGO)
                    await interaction.response.send_message("Added Counter Strike: Global Offensive!", ephemeral=True)

            @discord.ui.button(label = "Valorant", style=discord.ButtonStyle.gray, custom_id = "Valorant")
            async def Valorant(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Valorant in userRoles:
                    await user.remove_roles(Valorant)
                    await interaction.response.send_message("Removed Valorant!", ephemeral=True)
                else:
                    await user.add_roles(Valorant)
                    await interaction.response.send_message("Added Valorant!", ephemeral=True)

            @discord.ui.button(label = "Squad", style=discord.ButtonStyle.gray, custom_id = "Squad")
            async def Squad(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Squad in userRoles:
                    await user.remove_roles(Squad)
                    await interaction.response.send_message("Removed Squad!", ephemeral=True)
                else:
                    await user.add_roles(Squad)
                    await interaction.response.send_message("Added Squad!", ephemeral=True)

            @discord.ui.button(label = "Crusader Kings", style=discord.ButtonStyle.gray, custom_id = "CrusaderKings")
            async def CrusaderKings(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if CrusaderKings in userRoles:
                    await user.remove_roles(CrusaderKings)
                    await interaction.response.send_message("Removed Crusader Kings!", ephemeral=True)
                else:
                    await user.add_roles(CrusaderKings)
                    await interaction.response.send_message("Added Crusader Kings!", ephemeral=True)
                    
            @discord.ui.button(label = "Rocket League", style=discord.ButtonStyle.gray, custom_id = "RocketLeague")
            async def RocketLeague(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if RocketLeague in userRoles:
                    await user.remove_roles(RocketLeague)
                    await interaction.response.send_message("Removed Rocket League!", ephemeral=True)
                else:
                    await user.add_roles(RocketLeague)
                    await interaction.response.send_message("Added Rocket League!", ephemeral=True)

            @discord.ui.button(label = "Human Fall Flat", style=discord.ButtonStyle.gray, custom_id = "HumanFallFlat")
            async def HumanFallFlat(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if HumanFallFlat in userRoles:
                    await user.remove_roles(HumanFallFlat)
                    await interaction.response.send_message("Removed Human Fall Flat!", ephemeral=True)
                else:
                    await user.add_roles(HumanFallFlat)
                    await interaction.response.send_message("Added Human Fall Flat!", ephemeral=True)

            @discord.ui.button(label = "War Thunder", style=discord.ButtonStyle.gray, custom_id = "War Thunder")
            async def WarThunder(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if WarThunder in userRoles:
                    await user.remove_roles(WarThunder)
                    await interaction.response.send_message("Removed War Thunder!", ephemeral=True)
                else:
                    await user.add_roles(WarThunder)
                    await interaction.response.send_message("Added War Thunder!", ephemeral=True)

            @discord.ui.button(label = "Battlefield", style=discord.ButtonStyle.gray, custom_id = "Battlefield")
            async def Battlefield(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Battlefield in userRoles:
                    await user.remove_roles(Battlefield)
                    await interaction.response.send_message("Removed Battlefield!", ephemeral=True)
                else:
                    await user.add_roles(Battlefield)
                    await interaction.response.send_message("Added Battlefield!", ephemeral=True)

        await channel.send(content="Choose which games you play!",view=my_games(timeout=None))
        

#---------------------------------------------------------------------------------------------------------------------------
    async def interests(self, ctx):
        DnD = get(ctx.guild.roles, name="DnD")
        Anime = get(ctx.guild.roles, name="Anime")
        Fitness = get(ctx.guild.roles, name="Fitness")
        Finance = get(ctx.guild.roles, name="Finance")
        Pets = get(ctx.guild.roles, name="Pets")
        Voyeur = get(ctx.guild.roles, name="Voyeur")
        Gaming = get(ctx.guild.roles, name="Gaming")
        Techie = get(ctx.guild.roles, name="Techie")
        channel = get(ctx.guild.text_channels, name="get-your-roles")

        class my_interests(discord.ui.View):
            @discord.ui.button(label = "DnD", style=discord.ButtonStyle.gray, custom_id = "DnD")
            async def DnD(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if DnD in userRoles:
                    await user.remove_roles(DnD)
                    await interaction.response.send_message("Removed DnD!", ephemeral=True)
                else:
                    await user.add_roles(DnD)
                    await interaction.response.send_message("Added DnD!", ephemeral=True)

            @discord.ui.button(label = "Anime", style=discord.ButtonStyle.gray, custom_id = "Anime")
            async def Anime(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Anime in userRoles:
                    await user.remove_roles(Anime)
                    await interaction.response.send_message("Removed Anime!", ephemeral=True)
                else:
                    await user.add_roles(Anime)
                    await interaction.response.send_message("Added Anime!", ephemeral=True)

            @discord.ui.button(label = "Fitness", style=discord.ButtonStyle.gray, custom_id = "Fitness")
            async def Fitness(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Fitness in userRoles:
                    await user.remove_roles(Fitness)
                    await interaction.response.send_message("Removed Fitness!", ephemeral=True)
                else:
                    await user.add_roles(Fitness)
                    await interaction.response.send_message("Added Fitness!", ephemeral=True)

            @discord.ui.button(label = "Finance", style=discord.ButtonStyle.gray, custom_id = "Finance")
            async def Finance(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Finance in userRoles:
                    await user.remove_roles(Finance)
                    await interaction.response.send_message("Removed Finance!", ephemeral=True)
                else:
                    await user.add_roles(Finance)
                    await interaction.response.send_message("Added Finance!", ephemeral=True)

            @discord.ui.button(label = "Pets", style=discord.ButtonStyle.gray, custom_id = "Pets")
            async def Pets(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Pets in userRoles:
                    await user.remove_roles(Pets)
                    await interaction.response.send_message("Removed Pets!", ephemeral=True)
                else:
                    await user.add_roles(Pets)
                    await interaction.response.send_message("Added Pets!", ephemeral=True)

            @discord.ui.button(label = "Voyeur", style=discord.ButtonStyle.gray, custom_id = "Voyeur")
            async def Voyeur(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Voyeur in userRoles:
                    await user.remove_roles(Voyeur)
                    await interaction.response.send_message("Removed Voyeur!", ephemeral=True)
                else:
                    await user.add_roles(Voyeur)
                    await interaction.response.send_message("Added Voyeur!", ephemeral=True)

            @discord.ui.button(label = "Gaming", style=discord.ButtonStyle.gray, custom_id = "Gaming")
            async def Gaming(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Gaming in userRoles:
                    await user.remove_roles(Gaming)
                    await interaction.response.send_message("Removed Gaming!", ephemeral=True)
                else:
                    await user.add_roles(Gaming)
                    await interaction.response.send_message("Added Gaming!", ephemeral=True)

            @discord.ui.button(label = "Techie", style=discord.ButtonStyle.gray, custom_id = "Techie")
            async def Techie(self, interaction: discord.Interaction, button: discord.ui.Button):
                user = interaction.user
                userRoles = interaction.user.roles
                if Techie in userRoles:
                    await user.remove_roles(Techie)
                    await interaction.response.send_message("Removed Techie!", ephemeral=True)
                else:
                    await user.add_roles(Techie)
                    await interaction.response.send_message("Added Techie!", ephemeral=True)

        await channel.send(content="Choose your interests!",view=my_interests(timeout=None))

#-----------------------------------------------------------------------------------------------------------------------------------------------
    async def colors(self, ctx):
        channel = get(ctx.guild.text_channels, name="colors")

        class colorView(discord.ui.View):
                @discord.ui.button(label = "Green", style=discord.ButtonStyle.gray, emoji="🟢", row = 1, custom_id = "Green")
                async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    userRoles = interaction.user.roles
                    Green = get(ctx.guild.roles, name="Green")
                    if Green in userRoles:
                        await user.remove_roles(Green)
                        await interaction.response.send_message("Removed green!", ephemeral=True)
                    else:
                        await user.add_roles(Green)
                        await interaction.response.send_message("Your color is now green!", ephemeral=True)

                @discord.ui.button(label = "Orange", style=discord.ButtonStyle.gray, emoji="🟠", row = 1, custom_id = "Orange")
                async def orange(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Orange = get(ctx.guild.roles, name="Orange")
                    userRoles = interaction.user.roles
                    if Orange in userRoles:
                        await user.remove_roles(Orange)
                        await interaction.response.send_message("Removed orange!", ephemeral=True)
                    else:
                        await user.add_roles(Orange)
                        await interaction.response.send_message("Your color is now orange!", ephemeral=True)

                @discord.ui.button(label = "Purple", style=discord.ButtonStyle.gray, emoji="🟣", row = 1, custom_id = "Purple")
                async def purple(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Purple = get(ctx.guild.roles, name="Purple")
                    userRoles = interaction.user.roles
                    if Purple in userRoles:
                        await user.remove_roles(Purple)
                        await interaction.response.send_message("Removed purple!", ephemeral=True)
                    else:
                        await user.add_roles(Purple)
                        await interaction.response.send_message("Your color is now purple!", ephemeral=True)

                @discord.ui.button(label = "Yellow", style=discord.ButtonStyle.gray, emoji="🟡", row = 1, custom_id = "Yellow")
                async def yellow(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Yellow = get(ctx.guild.roles, name="Yellow")
                    userRoles = interaction.user.roles
                    if Yellow in userRoles:
                        await user.remove_roles(Yellow)
                        await interaction.response.send_message("Removed yellow!", ephemeral=True)
                    else:
                        await user.add_roles(Yellow)
                        await interaction.response.send_message("Your color is now yellow!", ephemeral=True)

                @discord.ui.button(label = "Red", style=discord.ButtonStyle.gray, emoji="🔴", row = 2, custom_id = "Red")
                async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Red = get(ctx.guild.roles, name="Red")
                    userRoles = interaction.user.roles
                    if Red in userRoles:
                        await user.remove_roles(Red)
                        await interaction.response.send_message("Removed red!", ephemeral=True)
                    else:
                        await user.add_roles(Red)
                        await interaction.response.send_message("Your color is now red!", ephemeral=True)

                @discord.ui.button(label = "Blue", style=discord.ButtonStyle.gray, emoji="🔵", row = 2, custom_id = "Blue")
                async def blue(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Blue = get(ctx.guild.roles, name="Blue")
                    userRoles = interaction.user.roles
                    if Blue in userRoles:
                        await user.remove_roles(Blue)
                        await interaction.response.send_message("Removed blue!", ephemeral=True)
                    else:
                        await user.add_roles(Blue)
                        await interaction.response.send_message("Your color is now blue!", ephemeral=True)

                @discord.ui.button(label = "Teal", style=discord.ButtonStyle.gray, emoji="💠", row = 2, custom_id = "Teal")
                async def teal(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Teal = get(ctx.guild.roles, name="Teal")
                    userRoles = interaction.user.roles
                    if Teal in userRoles:
                        await user.remove_roles(Teal)
                        await interaction.response.send_message("Removed teal!", ephemeral=True)
                    else:
                        await user.add_roles(Teal)
                        await interaction.response.send_message("Your color is now teal!", ephemeral=True)

                @discord.ui.button(label = "Pink", style=discord.ButtonStyle.gray, emoji="💗", row = 2, custom_id = "Pink")
                async def pink(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    Pink = get(ctx.guild.roles, name="Pink")
                    userRoles = interaction.user.roles
                    if Pink in userRoles:
                        await user.remove_roles(Pink)
                        await interaction.response.send_message("Removed pink!", ephemeral=True)
                    else:
                        await user.add_roles(Pink)
                        await interaction.response.send_message("Your color is now pink!", ephemeral=True)
        
        await channel.send(content="Choose the color of your name!\nClick the button again to remove the color.",view=colorView(timeout=None))

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def uservoting(self, ctx, subject: str):
        global yesCount
        global noCount
        yesVoters = []
        noVoters = []
        yesCount = 0
        noCount = 0
        author = ctx.author
        embed = discord.Embed(color = 0x800080, title=f"{subject}?", description=f"Vote started by {author.mention}")
        embed.add_field(name="Yes", value=yesCount)
        embed.add_field(name="No", value=noCount)

        class voteopt(discord.ui.View):
                @discord.ui.button(label = "Yes", style=discord.ButtonStyle.gray, emoji="🟢", custom_id = "Yes")
                async def yes(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    msg = interaction.message
                    if user.id in yesVoters:
                        await interaction.response.send_message("Removed your vote from yes!", ephemeral=True)
                        yesVoters.remove(user.id)
                        mycursor.execute(f"SELECT yes_count FROM voting WHERE message_id = {msg.id}")
                        count = mycursor.fetchall()
                        recount = re.sub(r"\W+", '', str(count))
                        mycursor.execute(f"SELECT no_count FROM voting WHERE message_id = {msg.id}")
                        noCount = mycursor.fetchall()
                        noCountParsed = re.sub(r"\W+", '', str(noCount))
                        newcount = int(recount) - 1
                        mycursor.execute(f"UPDATE voting SET yes_count = {newcount} WHERE message_id = {msg.id}")
                        mydb.commit()
                        embed = discord.Embed(color = 0x800080, title=f"{subject}?", description=f"Vote started by {author.mention}")
                        embed.add_field(name="Yes", value=newcount)
                        embed.add_field(name="No", value=noCountParsed)
                        await message.edit(embed=embed, view=voteopt(timeout=None))
                    else:
                        yesVoters.append(user.id)
                        await interaction.response.send_message("You voted yes!", ephemeral=True)
                        mycursor.execute(f"SELECT yes_count FROM voting WHERE message_id = {msg.id}")
                        count = mycursor.fetchall()
                        recount = re.sub(r"\W+", '', str(count))
                        mycursor.execute(f"SELECT no_count FROM voting WHERE message_id = {msg.id}")
                        noCount = mycursor.fetchall()
                        noCountParsed = re.sub(r"\W+", '', str(noCount))
                        newcount = int(recount) + 1
                        mycursor.execute(f"UPDATE voting SET yes_count = {newcount} WHERE message_id = {msg.id}")
                        mydb.commit()
                        embed = discord.Embed(color = 0x800080, title=f"{subject}?", description=f"Vote started by {author.mention}")
                        embed.add_field(name="Yes", value=newcount)
                        embed.add_field(name="No", value=noCountParsed)
                        await message.edit(embed=embed, view=voteopt(timeout=None))

                @discord.ui.button(label = "No", style=discord.ButtonStyle.gray, emoji="🔴", custom_id = "No")
                async def no(self, interaction: discord.Interaction, button: discord.ui.Button):
                    user = interaction.user
                    msg = interaction.message
                    if user.id in noVoters:
                        await interaction.response.send_message("Removed your vote from no!", ephemeral=True)
                        noVoters.remove(user.id)
                        mycursor.execute(f"SELECT no_count FROM voting WHERE message_id = {msg.id}")
                        count = mycursor.fetchall()
                        recount = re.sub(r"\W+", '', str(count))
                        mycursor.execute(f"SELECT yes_count FROM voting WHERE message_id = {msg.id}")
                        yesCount = mycursor.fetchall()
                        yesCountParsed = re.sub(r"\W+", '', str(yesCount))
                        newcount = int(recount) - 1
                        mycursor.execute(f"UPDATE voting SET no_count = {newcount} WHERE message_id = {msg.id}")
                        mydb.commit()
                        embed = discord.Embed(color = 0x800080, title=f"{subject}?", description=f"Vote started by {author.mention}")
                        embed.add_field(name="Yes", value=yesCountParsed)
                        embed.add_field(name="No", value=newcount)
                        await message.edit(embed=embed, view=voteopt(timeout=None))
                    else:
                        noVoters.append(user.id)
                        await interaction.response.send_message("You voted no!", ephemeral=True)
                        mycursor.execute(f"SELECT no_count FROM voting WHERE message_id = {msg.id}")
                        count = mycursor.fetchall()
                        recount = re.sub(r"\W+", '', str(count))
                        mycursor.execute(f"SELECT yes_count FROM voting WHERE message_id = {msg.id}")
                        yesCount = mycursor.fetchall()
                        yesCountParsed = re.sub(r"\W+", '', str(yesCount))
                        newcount = int(recount) + 1
                        mycursor.execute(f"UPDATE voting SET no_count = {newcount} WHERE message_id = {msg.id}")
                        mydb.commit()
                        embed = discord.Embed(color = 0x800080, title=f"{subject}?", description=f"Vote started by {author.mention}")
                        embed.add_field(name="Yes", value=yesCountParsed)
                        embed.add_field(name="No", value=newcount)
                        await message.edit(embed=embed, view=voteopt(timeout=None))

        message = await ctx.send(embed=embed, view=voteopt(timeout=None))
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO voting (message_id) VALUES ({message.id})")
        mydb.commit()
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def warning(self, ctx, user: discord.Member, reason, author=None):
        warnCount = 0
        mycursor = mydb.cursor()
        if author == None:
            author = ctx.author.name
            sql = "INSERT INTO warnings (user_id, issue, warned_by) VALUES (%s, %s, %s)"
            val = user.id, reason, author
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.execute(f"SELECT user_id FROM warnings WHERE user_id = {user.id}")
            warnings = mycursor.fetchall()
            mydb.commit()
            for x in warnings:
                warnCount += 1
            embed = discord.Embed(color = 0x800080, title=f"{user} has been warned!", description = f"Warned by: {ctx.author}\n\n**Reason:** {reason}")
            embed.add_field(name=f"{user}'s total warnings", value = warnCount)
            await ctx.send(embed=embed)
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def warnings(self, ctx, user: discord.Member):
        warnCount = 0
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT issue FROM warnings WHERE user_id = {user.id}")
        warnings = mycursor.fetchall()
        mydb.commit()
        for x in warnings:
            warnCount += 1
        embed = discord.Embed(color = 0x800080, title = f"{user}'s warnings:", description = f"**Total warnings:**\n{warnCount}")
        for x in warnings:
            reason = re.sub(r"[^\w\s]", '', str(x))
            sql = (f"SELECT warned_by FROM warnings WHERE issue = '{reason}'")
            val = reason
            mycursor.execute(sql, val)
            warner = mycursor.fetchall()
            mydb.commit()
            warnerParsed = re.sub(r"[^\w\s]", '', str(warner))
            embed.add_field(name=f"{warnerParsed} warned with reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    async def clear(self, ctx, user: discord.Member):
        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM warnings WHERE user_id = {user.id}")
        mydb.commit()
        await ctx.send(f"Cleared all warnings from {user.name}")
        
async def setup(bot):
    await bot.add_cog(Supportive(bot))