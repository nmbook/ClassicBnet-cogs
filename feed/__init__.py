from .feed import ClassicBnetFeed

def setup(bot):
    bot.add_cog(ClassicBnetFeed(bot))

