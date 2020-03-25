import logging
import os
import asyncpg

from discord.ext import commands

from config import BOT_TOKEN, DB_BIND

logging.basicConfig(level=logging.ERROR)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='a!',
            help_command=None,
            case_insensitive=True,
            owner_ids=set([404739517971562506, 285738922519035904])
        )

    async def on_connect(self):
        print('Connected to discord')

    async def on_ready(self):
        print('Bot is ready')
        extensions = 0
        for filename in filter(lambda filename: filename.endswith('.py') and not filename.startswith('_'), os.listdir('cogs')):
            cog_name = filename[:-3]
            extensions += 1
            try:
                self.load_extension(f'cogs.{cog_name}')
            except commands.errors.ExtensionAlreadyLoaded:
                pass 
        print(f'Loaded {extensions} extensions')
        self.db = await asyncpg.create_pool(DB_BIND)
    
Bot().run(BOT_TOKEN)    
