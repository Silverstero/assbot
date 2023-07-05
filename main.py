import hikari
import lightbulb
import os

my_secret = os.environ['TOLKIEN']
bot = lightbulb.BotApp(token=my_secret, prefix='!')


@bot.command
@lightbulb.command('ping', 'says pong ')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  await ctx.respond('Fuck Poprock')


@bot.command
@lightbulb.option('confession', 'the confession')
@lightbulb.command('confess', 'Confess someting secretly')
@lightbulb.implements(lightbulb.SlashCommand)
async def confess(ctx):
  targetchannel = await bot.rest.fetch_channel('1125971259570802769')
  await targetchannel.send('Somebody did someting embarrasing! they: ' +
                           ctx.options.confession + 'should we forgive them?')


bot.run()
