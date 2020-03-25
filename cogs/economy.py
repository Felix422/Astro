import discord, random, os
from discord.ext import commands
import sys   



class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @property 
    def db(self):
        return self.bot.db

    @commands.command()
    async def slots(self, ctx):
        embed = discord.Embed(color=ctx.guild.me.top_role.color)
        responses = [':cherries:',':watermelon:',':banana:',':grapes:',':apple:']
        slot1 = random.choice(responses) 
        slot2 = random.choice(responses)
        slot3 = random.choice(responses)
        embed.add_field(name=(f'**[ ASTRO | SLOTS ]** \n------------------'), value=(f'{random.choice(responses)} : {random.choice(responses)} : {random.choice(responses)} \n \n{slot1} : {slot2} : {slot3}**<** \n \n{random.choice(responses)} : {random.choice(responses)} : {random.choice(responses)} \n------------------'), inline=False)

        await ctx.send(embed=embed)
         


def setup(bot):
    bot.add_cog(Economy(bot))