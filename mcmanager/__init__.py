from redbot.core.bot import Red
from .mcmanager import McManager

async def setup(bot: Red):
    cog = McManager(bot)
    await bot.add_cog(cog)
