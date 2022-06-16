import discord
from discord.ext import commands
from discord.ext.commands.core import has_role
from discord.utils import get
import mysql.connector
import re
import datetime
from dpymenus import Page, ButtonMenu

#--------------DEFINITIONS-------------------------------------------------------------
mydb = mysql.connector.connect(
  host="us-dal-mysql-01.plox.host",
  user="u5720_uDUg0WGfvl",
  password="aIiz^LccR^vcb^=EztatJCcU",
  database="s5720_roulettebets"
)
print(mydb)
class Economy(commands.Cog, description="All commands related to your economy, such as balance!"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


#---------OPENS AN ACCOUNT FOR USER IF NOT ALREADY OPENED-------------------------------------------------------------
    async def open_account(user):
        cursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO bank (id, balance) VALUES (%s, %s)"
        val = (user, 500)
        cursor.execute(sql, val)
        mydb.commit()
#--------ECONOMY--------------------------------------------------------------------------------------------------------------
    async def store_purchase(self, ctx, user, cost):
        mycursor = mydb.cursor()
        memberid = re.sub(r"\W+", '', str(user))
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
        myresult = mycursor.fetchall()
        balance = re.sub(r"\W+", '', str(myresult))
        mydb.commit()
        if myresult == []:
            await Economy.Economy.open_account(memberid)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
            myresult = mycursor.fetchall()
            balance = re.sub(r"\W+", '', str(myresult)) 
            if cost <= int(balance): 
                newbal = int(balance) - int(cost)
                mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE balance = {balance}")
                mydb.commit()
        else:
            if cost <= int(balance):
                newbal = int(balance) - int(cost)
                mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE balance = {balance}")
                mydb.commit()

    #-------STORE--------------------------------------------------------------------------------------
    @commands.command(name='Store', brief="Opens the menu for the server store.")
    async def store(self, ctx):
        user = ctx.author.id
        forward = '⏩'
        select = '⏺️'
        reverse = '⏪'
        stop = '⏹️'
        Gigachad = get(ctx.guild.roles, name="Gigachad")
        Chad = get(ctx.guild.roles, name="Chad")
        Succesfulking = get(ctx.guild.roles, name="Succesful king")
        Degenerate = get(ctx.guild.roles, name="Degenerate")
        async def first(menu):
            if menu.button_pressed(forward):
                await menu.next()

            if menu.button_pressed(stop):
                await menu.close()

            elif menu.button_pressed(select):
                cost = 1000
                await menu.close()
                await Economy.store_purchase(self, ctx, user, cost)
                mycursor = mydb.cursor()
                memberid = re.sub(r"\W+", '', str(user))
                mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
                myresult = mycursor.fetchall()
                balance = re.sub(r"\W+", '', str(myresult))
                if cost <= int(balance):
                    await ctx.author.add_roles(Degenerate)
                    await ctx.send(f"{ctx.author.mention} is a Degenerate!")
                else:
                    await ctx.send("You don't have enough credits!")

        async def second(menu):
            if menu.button_pressed(reverse):
                await menu.go_to('first')

            elif menu.button_pressed(forward):
                await menu.next()

            elif menu.button_pressed(stop):
                await menu.close()

            elif menu.button_pressed(select):
                cost = 20000
                await menu.close()
                await Economy.store_purchase(self, ctx, user, cost)
                mycursor = mydb.cursor()
                memberid = re.sub(r"\W+", '', str(user))
                mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
                myresult = mycursor.fetchall()
                balance = re.sub(r"\W+", '', str(myresult))
                if cost <= int(balance):
                    await ctx.author.add_roles(Chad)
                    await ctx.send(f"{ctx.author.mention} is a Chad!")
                else:
                    await ctx.send("You don't have enough credits!")

        async def third(menu):
            if menu.button_pressed(reverse):
                await menu.go_to('second')

            elif menu.button_pressed(forward):
                await menu.next()

            elif menu.button_pressed(stop):
                await menu.close()

            elif menu.button_pressed(select):
                cost = 50000
                await menu.close()
                await Economy.store_purchase(self, ctx, user, cost)
                mycursor = mydb.cursor()
                memberid = re.sub(r"\W+", '', str(user))
                mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
                myresult = mycursor.fetchall()
                balance = re.sub(r"\W+", '', str(myresult))
                if cost <= int(balance):
                    await ctx.author.add_roles(Gigachad)
                    await ctx.send(f"{ctx.author.mention} is a Gigachad!")
                else:
                    await ctx.send("You don't have enough credits!")

        async def fourth(menu):
            if menu.button_pressed(reverse):
                await menu.go_to('third')

            elif menu.button_pressed(forward):
                await menu.next()

            elif menu.button_pressed(stop):
                await menu.close()

            elif menu.button_pressed(select):
                cost = 100000
                await menu.close()
                await Economy.store_purchase(self, ctx, user, cost)
                mycursor = mydb.cursor()
                memberid = re.sub(r"\W+", '', str(user))
                mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
                myresult = mycursor.fetchall()
                balance = re.sub(r"\W+", '', str(myresult))
                if cost <= int(balance):
                    await ctx.author.add_roles(Succesfulking)
                    await ctx.send(f"{ctx.author.mention} is a Succesful king!")
                else:
                    await ctx.send("You don't have enough credits!")



        page1 = Page(title='Store | Page 1', description='Purchase role by reacting with circle!')
        page1.add_field(name='Degenerate', value='1000')
        page1.buttons([select, stop, forward]).on_next(first)

        page2 = Page(title='Store | Page 2', description='Purchase role by reacting with circle!')
        page2.add_field(name='Chad', value='20,000 credits')
        page2.buttons([reverse, select, stop, forward]).on_next(second)

        page3 = Page(title='Store | Page 3', description='Purchase role by reacting with circle!')
        page3.add_field(name='Gigachad', value='50,000')
        page3.buttons([reverse, select, stop, forward]).on_next(third)

        page4 = Page(title='Store | Page 4', description='Purchase role by reacting with circle!')
        page4.add_field(name='Succesful king', value='100,000')
        page4.buttons([reverse, select, stop]).on_next(fourth)



        menu = ButtonMenu(ctx)
        menu.add_pages([page1, page2, page3, page4])
        await menu.open()


    #---------BALANCE-------------------------------------------------------------------------------
    @commands.command(name='Balance', brief="Command which shows users their balance")
    async def balance(self, ctx):
        user = ctx.author.id
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
            embed = discord.Embed(title= f"{ctx.author.name}'s credits:")
            embed.add_field(name = f"Credits",value= balance)
            await ctx.send(embed=embed)
        else:
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {user}")
            bal = mycursor.fetchall()
            mydb.commit()
            balance = re.sub(r"\W+", '', str(bal))
            embed = discord.Embed(title= f"{ctx.author.name}'s credits:")
            embed.add_field(name = "Credits",value= balance)
            await ctx.send(embed=embed)


    #---------GIVE MONEY-------------------------------------------------------------------------------
    @has_role("Bonker")
    @commands.command(name='Give', brief="Command which adds money to the mentioned users balance")
    async def give(self, ctx, member, amt):
        await Economy.give_process(member, amt)
        await ctx.send("Given {} credits to {}".format(amt, member))

    #---------DAILY-MONEY-------------------------------------------------------------------------------
    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command(name='Daily', brief="Command to recive daily 50 credits!")
    async def daily(self, ctx):
        amt = 50
        mycursor = mydb.cursor()
        memberid = re.sub(r"\W+", '', str(ctx.author.id))
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
        myresult = mycursor.fetchall()
        balance = re.sub(r"\W+", '', str(myresult))
        mydb.commit()
        if myresult == []:
            await Economy.open_account(memberid)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
            myresult = mycursor.fetchall()
            balance = re.sub(r"\W+", '', str(myresult))  
            newbal = int(amt) + int(balance)
            mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {memberid}")
            mydb.commit()
        else:
            newbal = int(amt) + int(balance)
            mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {memberid}")
            mydb.commit()
        await ctx.send(f"Given 50 credits to {ctx.author.mention}")

    @daily.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))

            embed = discord.Embed(title=":clock1: Cooldown!", description=f'You can use this command again in ' + str(remaining_time), color=0xE74C3C)
            await ctx.send(embed=embed) 

    #---------GIVE MONEY HELPER-------------------------------------------------------------------------------
    async def give_process(member, amt):
        mycursor = mydb.cursor()
        memberid = re.sub(r"\W+", '', str(member))
        mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
        myresult = mycursor.fetchall()
        balance = re.sub(r"\W+", '', str(myresult))
        mydb.commit()
        if myresult == []:
            await Economy.open_account(memberid)
            mycursor.execute(f"SELECT balance FROM bank WHERE id = {memberid}")
            myresult = mycursor.fetchall()
            balance = re.sub(r"\W+", '', str(myresult))  
            newbal = int(amt) + int(balance)
            mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {memberid}")
            mydb.commit()
        else:
            newbal = int(amt) + int(balance)
            mycursor.execute(f"UPDATE bank SET balance = {newbal} WHERE id = {memberid}")
            mydb.commit()
def setup(bot):
    bot.add_cog(Economy(bot))