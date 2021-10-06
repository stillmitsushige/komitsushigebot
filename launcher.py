from discord.ext import commands
import config
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("on_ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        # Bot からのメッセージには反応しない
        # この判定をしないと無限ループが起きる
        return

    if "Bot" in message.content:
        await message.channel.send(" は~い、Bot で~す ")


    # ほげ
    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send(f" こん。{ctx.author.name}！")
    
bot.run(config.TOKEN)