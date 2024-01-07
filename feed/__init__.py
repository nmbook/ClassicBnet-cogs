from .feed import ClassicBnetFeed

async def setup(bot):
    await bot.add_cog(ClassicBnetFeed(bot))

