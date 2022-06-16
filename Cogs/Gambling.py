import discord
from discord.ext import commands
import random
import mysql.connector
import re
import asyncio

#--------------DEFINITIONS-------------------------------------------------------------
mydb = mysql.connector.connect(
  host="us-dal-mysql-01.plox.host",
  user="u5720_uDUg0WGfvl",
  password="aIiz^LccR^vcb^=EztatJCcU",
  database="s5720_roulettebets"
)
roulettetimer = 1
class Gambling(commands.Cog, description="Commands for using roulette!"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


#---------ROULETTE BLACK------------------------------------------------------------------------------
    @commands.command(name='Black', brief="Place a bet on black!")
    async def black(self, ctx, bet: int):
        global roulettetimer
        aut = ctx.author
        Economy = self.bot.get_cog('Economy')
        user = ctx.message.author.id
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
        myresult = mycursor.fetchall()
        mydb.commit()
        if myresult == []:
            await Economy.open_account(user)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            if bet <= int(balance):
                color = "black"
                await Gambling.remove_balance(self, user, bet)
                await Gambling.write_bet(self, user, color, bet)
                embed = discord.Embed(title= "Minibot | Roulette")
                embed.add_field(name="Bet", value=f"{aut.mention} bet {bet} credits on black!")
                await ctx.send(embed=embed)
                if roulettetimer == 1:
                    await Gambling.start_roll(self, ctx, user, color)
                else:
                    pass

            else: 
                await ctx.send("You do not have enough credits!")
        else:
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            if bet <= int(balance):
                color = "black"
                await ctx.send(str(bet))
                await Gambling.remove_balance(self, user, bet)
                await Gambling.write_bet(self, user, color, bet)
                embed = discord.Embed(title= "Minibot | Roulette")
                embed.add_field(name="Bet", value=f"{aut.mention} bet {bet} credits on black!")
                await ctx.send(embed=embed)
                if roulettetimer == 1:
                    await Gambling.start_roll(self, ctx, user, color)
                else:
                    pass
            else: 
                await ctx.send("You do not have enough credits!")

    #---------ROULETTE RED------------------------------------------------------------------------------
    @commands.command(name='Red', brief="Place a bet on red!")
    async def red(self, ctx, bet: int):
        global roulettetimer
        aut = ctx.author
        Economy = self.bot.get_cog('Economy')
        user = ctx.message.author.id
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
        myresult = mycursor.fetchall()
        mydb.commit()
        if myresult == []:
            await Economy.open_account(user)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            if bet <= int(balance):
                color = "red"
                await Gambling.remove_balance(self, user, bet)
                await Gambling.write_bet(self, user, color, bet)
                embed = discord.Embed(title= "Minibot | Roulette")
                embed.add_field(name="Bet", value=f"{aut.mention} bet {bet} credits on red!")
                await ctx.send(embed=embed)
                if roulettetimer == 1:
                    await Gambling.start_roll(self, ctx, user, color)
                else:
                    pass

            else: 
                await ctx.send("You do not have enough credits!")
        else:
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            if bet <= int(balance):
                color = "red"
                await Gambling.remove_balance(self, user, bet)
                await Gambling.write_bet(self, user, color, bet)
                embed = discord.Embed(title= "Minibot | Roulette")
                embed.add_field(name="Bet", value=f"{aut.mention} bet {bet} credits on red!")
                await ctx.send(embed=embed)
                if roulettetimer == 1:
                    await Gambling.start_roll(self, ctx, user, color)
                else:
                    pass
            else: 
                await ctx.send("You do not have enough credits!")

    #---------ROULETTE GREEN------------------------------------------------------------------------------
    @commands.command(name='Green', brief="Place a bet on green!")
    async def green(self, ctx, bet: int):
        global roulettetimer
        aut = ctx.author
        Economy = self.bot.get_cog('Economy')
        user = ctx.message.author.id
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
        myresult = mycursor.fetchall()
        mydb.commit()
        if myresult == []:
            await Economy.open_account(user)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            if bet <= int(balance):
                color = "green"
                await Gambling.remove_balance(self, user, bet)
                await Gambling.write_bet(self, user, color, bet)
                embed = discord.Embed(title= "Minibot | Roulette")
                embed.add_field(name="Bet", value=f"{aut.mention} bet {bet} credits on green!")
                await ctx.send(embed=embed)
                if roulettetimer == 1:
                    await Gambling.start_roll(self, ctx, user, color)
                else:
                    pass

            else: 
                await ctx.send("You do not have enough credits!")
        else:
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            if bet <= int(balance):
                color = "green"
                await Gambling.remove_balance(self, user, bet)
                await Gambling.write_bet(self, user, color, bet)
                embed = discord.Embed(title= "Minibot | Roulette")
                embed.add_field(name="Bet", value=f"{aut.mention} bet {bet} credits on green!")
                await ctx.send(embed=embed)
                if roulettetimer == 1:
                    await Gambling.start_roll(self, ctx, user, color)
                else:
                    pass
            else: 
                await ctx.send("You do not have enough credits!")

    #---------ROULETTE NUMBER------------------------------------------------------------------------------
    # @commands.command(name='number', brief="Command which adds a gamble to the pool for a number roulette roll")
    # async def number(self, ctx, bet: int, nr: int):
    #     global roulettetimer
    #     global color
    #     aut = ctx.author
    #     user = ctx.message.author.id
    #     mycursor = mydb.cursor()
    #     mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
    #     myresult = mycursor.fetchall()
    #     mydb.commit()
    #     if myresult == []:
    #         await Economy.open_account(user)
    #         mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
    #         bal = mycursor.fetchall()
    #         mydb.commit()
    #         balance = re.sub(r"\W+", '', str(bal))
    #         if bet <= int(balance):
    #             color = "black"
    #             await Gambling.remove_balance(user, bet)
    #             await Gambling.write_bet(user, color, bet)
    #             await ctx.send("{} bet {} credits on black!".format(aut.mention, bet))
    #             if roulettetimer == 1:
    #                 await Gambling.start_roll(self, ctx, user, color)
    #             else:
    #                 pass

    #         else: 
    #             await ctx.send("You do not have enough credits!")
    #     else:
    #         mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
    #         bal = mycursor.fetchall()
    #         mydb.commit()
    #         balance = re.sub(r"\W+", '', str(bal))
    #         if bet <= int(balance):
    #             color = "black"
    #             await Gambling.remove_balance(user, bet)
    #             await Gambling.write_bet(user, color, bet)
    #             await ctx.send("{} bet {} credits on black!".format(aut.mention, bet))
    #             if roulettetimer == 1:
    #                 await Gambling.start_roll(self, ctx, user, color)
    #             else:
    #                 pass
    #         else: 
    #             await ctx.send("You do not have enough credits!")

    #---------CREATE BET LINE-------------------------------------------------------------------------------
    async def write_bet(self, user, color, bet):
        mycursor = mydb.cursor()
        memberid = re.sub(r"\W+", '', str(user))
        sql = ("INSERT INTO bets (id, color, bet) VALUES (%s, %s, %s)")
        val = (memberid, color, bet)
        mycursor.execute(sql, val)
        mydb.commit()

    #---------ROULETTE DEDUCT MONEY HELPER------------------------------------------------------------------------------
    async def remove_balance(self, user, bet):
        Economy = self.bot.get_cog('Economy')
        mycursor = mydb.cursor()
        memberid = re.sub(r"\W+", '', str(user))
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
        myresult = mycursor.fetchall()
        balance = re.sub(r"\W+", '', str(myresult))
        mydb.commit()
        if myresult == []:
            await Economy.open_account(memberid)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
            myresult = mycursor.fetchall()
            balance = re.sub(r"\W+", '', str(myresult))  
            newbal = int(balance) - int(bet)
            mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE balance = {balance}")
            mydb.commit()
        else:
            newbal = int(balance) - int(bet)
            mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE balance = {balance}")
            mydb.commit()

    #---------ROULETTE START------------------------------------------------------------------------------
    async def start_roll(self, ctx, user, color):
        seconds = 30
        black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        nr = random.randint(0, 36)
        secondint = int(seconds)
        embedb = discord.Embed(color=0x000000)
        embedb.add_field(name="Roulette | MiniBot", value="Rolled: **{}**".format(nr))
        embedr = discord.Embed(color=0xff0000)
        embedr.add_field(name="Roulette | MiniBot", value="Rolled: **{}**".format(nr))
        embedg = discord.Embed(color=0x23a300)
        embedg.add_field(name="Roulette | MiniBot", value="Rolled: **{}!!!!!!**".format(nr))
        msg = await ctx.send("**Rolling in**: {}".format(seconds))
        global roulettetimer
        roulettetimer -= 1
        while True:
            secondint -= 1
            if secondint == 0:
                await msg.edit(content="**Rolling...**")
                await asyncio.sleep(1)
                await msg.delete()
                if nr in red:
                    color = "red"
                    await ctx.send(embed=embedr)
                    await Gambling.bets_payout(self, ctx, user, color)
                    roulettetimer += 1
                    break
                else:
                    if nr in black:
                        color = "black"
                        await ctx.send(embed=embedb)
                        await Gambling.bets_payout(self, ctx, user, color)
                        roulettetimer += 1
                        break
                    else:
                        if nr == 0:
                            color = "green"
                            await ctx.send(embed=embedg)
                            await Gambling.bets_payout(self, ctx, user, color)
                            roulettetimer += 1
                            break
            await msg.edit(content=f"Rolling in: {secondint}")
            await asyncio.sleep(1)

    #---------BETS PAYOUT------------------------------------------------------------------------------
    async def bets_payout(self, ctx, user, color):
        userid = user
        sender = ctx.author
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT bet FROM bets WHERE color = '{color}'")
        myresult = mycursor.fetchall()
        mydb.commit()
        if myresult == []:
            mycursor.execute(f"DELETE FROM bets")
            mydb.commit()
            pass
        else:
            if color == "black":
                mycursor.execute(f"SELECT SUM(bet) FROM bets WHERE id = {userid} and color = '{color}'")
                result = mycursor.fetchall()
                bet = re.sub(r"\D+", '', str(result))
                mydb.commit()
                mycursor.execute(f"SELECT balance FROM bank WHERE id = {userid}")
                bal = mycursor.fetchall()
                mydb.commit()
                balance = re.sub(r"\D+", '', str(bal))
                win = int(bet) * 2
                newbal = int(win) + int(balance)
                mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {userid}")
                mydb.commit()
                mycursor.execute(f"DELETE FROM bets")
                mydb.commit()
                await ctx.send(f"{sender.mention} won **{win}** credits and now has **{newbal}** credits!!")
            else:
                if color == "green":
                    mycursor.execute(f"SELECT SUM(bet) FROM bets WHERE id = {userid} and color = '{color}'")
                    result = mycursor.fetchall()
                    bet = re.sub(r"\D+", '', str(result))
                    win = int(bet) * 14
                    mydb.commit()
                    mycursor.execute(f"SELECT balance FROM bank WHERE id = {userid}")
                    bal = mycursor.fetchall()
                    mydb.commit()
                    balance = re.sub(r"\D+", '', str(bal))
                    newbal = int(win) + int(balance)
                    mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {userid}")
                    mydb.commit()
                    mycursor.execute(f"DELETE FROM bets")
                    mydb.commit()
                    await ctx.send(f"{sender.mention} won **{win}** credits and now has **{newbal}** credits!!")

                else:
                    if color == "red":
                        mycursor.execute(f"SELECT SUM(bet) FROM bets WHERE id = {userid} and color = '{color}'")
                        result = mycursor.fetchall()
                        bet = re.sub(r"\D+", '', str(result))
                        mydb.commit()
                        mycursor.execute(f"SELECT balance FROM bank WHERE id = {userid}")
                        bal = mycursor.fetchall()
                        mydb.commit()
                        balance = re.sub(r"\D+", '', str(bal))
                        win = int(bet) * 2
                        newbal = int(win) + int(balance)
                        mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {userid}")
                        mydb.commit()
                        mycursor.execute(f"DELETE FROM bets")
                        mydb.commit()
                        await ctx.send(f"{sender.mention} won **{win}** credits and now has **{newbal}** credits!!")
def setup(bot):
    bot.add_cog(Gambling(bot))