from redbot.core import commands
from redbot.core.bot import Red


class McManager(commands.Cog):
    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hello")
