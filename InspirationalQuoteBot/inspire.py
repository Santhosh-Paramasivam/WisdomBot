import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive
import os
import sqlite3
import random

load_dotenv()

connection = sqlite3.connect("inspirational_quotes.db")
cursor = connection.cursor()

def add_quote(quote):
    cursor.execute("INSERT INTO quotes VALUES(?)", (quote,))
    connection.commit()

def get_quote():
    cursor.execute("SELECT count(quote) FROM quotes")
    quoteCount = cursor.fetchall()[0][0]
    rand_index= random.randint(1, quoteCount)

    print(rand_index)

    cursor.execute("SELECT * FROM quotes WHERE quote_number = ?", (rand_index,))
    quoteRecord = cursor.fetchall()[0]

    print(quoteRecord)
    
    return quoteRecord[1]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.tree.command(name="quote", description="Posts an inspirational quote")
async def quote(interaction: discord.Interaction):
    await interaction.response.send_message(get_quote())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")
    
keep_alive()
bot.run(str(os.getenv('API-TOKEN')))
