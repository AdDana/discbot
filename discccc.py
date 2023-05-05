import discord
import logging
import sqlite3
from random import randint

#ссылка на сервер с ботом: https://discord.gg/qqJRNdND
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "MTEwMDUzMTA4MjkyNDkzNzI0Ng.G2yVUv.-5neG5V5IUJzSx5qFbH9N5GEzbrVgkRt2mh9s4" 
bleed = False
resistdark = 0
sqlite_connection = sqlite3.connect('E:/disc.db')
cursor = sqlite_connection.cursor()

class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Добро пожаловать, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if ".dice" in message.content.lower():
            dice = randint(1,20)
            await message.channel.send(f'Результат броска костей: {dice}')
        elif ".help" in message.content.lower():
            help = [".help", ".dice", ".attack 1person 2person", ".heal", ".slow", ".poison", ".bleed", ".solace", ".persuation", ".miss"]
            n = '\n'
            await message.channel.send(f'Имеющиеся на данный момент команды: {n}{n.join(help)}')
        elif ".baff" in message.content.lower():
            if "resistblood" in message.content.lower():
                await message.channel.send(f'Результат использования усиления: сопротивление к школе крови повышено на {randint(0,2)} на {randint(1,3)} ход(а)')
            elif "resistdark" in message.content.lower():
                await message.channel.send(f'Результат использования усиления: сопротивление к школе тьмы повышено на {randint(0,2)} на {randint(1,3)} ход(а)')
        elif ".heal" in message.content.lower():
            await message.channel.send(f'Результат исцеления: восполнено {randint(0,10)} хп')
        elif ".miss" in message.content.lower():
            if "kori" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Kori Rodrigues"')
            elif "oden" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Oden Rodenbush"')
            elif "daat" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Daat"')            
            elif "misha" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Mishelle Iber"')
            elif "henry" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Henricus Esposito"')
            elif "adler" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Adler Schultz"')
            elif "aroida" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Aroida"')
            agility = cursor.fetchall()
            for x in agility:
                agility = x[0]
            if randint(1,20) >= 12 and agility > 2:
                await message.channel.send(f'Результат уклонения: успех')
            else:
                await message.channel.send(f'Результат уклонения: провал')
        elif ".poison" in message.content.lower():
              poison = randint(1,5)
              time = randint(1,5)
              await message.channel.send(f'Результат использования яда: в течение следующих {time} ходов противнику наносится урон в количестве {poison} хп')
        elif ".bleed" in message.content.lower():
            bleed = randint(1,3)
            timebl = randint(1,6)
            await message.channel.send(f'Результат кровотечения: у противника кровопотеря в течение следующих {timebl} ходов в количестве {bleed} хп')
        elif ".slow" in message.content.lower():
            if "kori" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Kori Rodrigues"')
            elif "oden" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Oden Rodenbush"')
            elif "daat" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Daat"')            
            elif "misha" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Mishelle Iber"')
            elif "henry" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Henricus Esposito"')
            elif "adler" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Adler Schultz"')
            elif "aroida" in message.content.lower():
                cursor.execute('SELECT agility FROM disc WHERE name="Aroida"')
            agility = cursor.fetchall()
            for x in agility:
                agility = x[0]
            if randint(1,20) < 14 and agility >= 3:
                await message.channel.send(f'Результат использования замедления: провал')
            else:
                await message.channel.send(f'Результат использования замедления: противник замедлен на {randint(1,3)} хода')
        elif ".solace" in message.content.lower():
            if "kori" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Kori Rodrigues"')
            elif "oden" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Oden Rodenbush"')
            elif "daat" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Daat"')            
            elif "misha" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Mishelle Iber"')
            elif "henry" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Henricus Esposito"')
            elif "adler" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Adler Schultz"')
            elif "aroida" in message.content.lower():
                cursor.execute('SELECT relation FROM disc WHERE name="Aroida"')
            relation = cursor.fetchall()
            for x in relation:
                relation = x[0]
            if randint(1,20) >= 15 and relation >= 0:
                await message.channel.send(f'Результат успокоения: успех')
            else:
                await message.channel.send(f'Результат успокоения: провал')
        elif ".persuasion" in message.content.lower():
            if randint(0,1) == 1:
                await message.channel.send(f'Результат уговоров: успех')
            else:
                await message.channel.send(f'Результат уговоров: провал')
        elif ".attack" in message.content.lower():
            #первый чел
            if "1kori" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Kori Rodrigues"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,20)
                type = "blood"
            elif "1adler" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Adler Schultz"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,25)
                type = "psycho"
            elif "1aroida" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Aroida"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,30)
                type = "electro"
            elif "1daat" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Daat"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,20)
                type = "ether"
            elif "1henry" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Henricus Esposito"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,30)
                type = "wave"
            elif "1misha" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Mishelle Iber"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,25)
                type = "dark"
            elif "1oden" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Oden Rodenbush"')
                strong = cursor.fetchall()
                for x in strong:
                    strong = x[0]
                att = randint(1,30)
                type = "blood"
            #второй чел    
            if "2kori" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Kori Rodrigues"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Kori Rodrigues"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            elif "2adler" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Adler Schultz"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Adler Schultz"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            elif "2aroida" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Aroida"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Aroida"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            elif "2misha" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Mishelle Iber"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Mishelle Iber"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            elif "2oden" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Oden Rodenbush"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Oden Rodenbush"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            elif "2daat" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Daat"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Daat"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            elif "2henry" in message.content.lower():
                cursor.execute('SELECT strong FROM disc WHERE name="Henricus Esposito"')
                defence = cursor.fetchall()
                for x in defence:
                    defence = x[0]
                cursor.execute(f'SELECT res{type} FROM disc WHERE name="Henricus Esposito"')
                resist = cursor.fetchall()
                for x in resist:
                    resist = x[0]
            res = (att + strong - defence) // resist
            if res > 0:
                await message.channel.send(f'Результат атаки: -{res} хп')
            else:
                await message.channel.send(f'Результат атаки: провал')
            
           # if "mishadaat" in message.content.lower():
#                strong = 3
#                defence = 5
#                att = randint(1,20)
#                type = "dark"
#                resistdark = 1
#                res = (att + strong - defence) // resistdark 
#                if res > 0:
#                    await message.channel.send(f'Результат атаки: -{res} хп')
#                else:
#                    await message.channel.send(f'Результат атаки: провал')
#            if "aroidahenry" in message.content.lower():
#                strong = 12
#                defence = 18
#                att = randint(1,20)
#                type = "electricity"
#                resistel = 3
#                res = (att + strong - defence) // resistel 
#                if res > 0:
#                    await message.channel.send(f'Результат атаки: -{res} хп')
#                else:
#                    await message.channel.send(f'Результат атаки: провал')
         
                    
#я жена кодерки (Пэ.сэ. Екатерина the second) и я официально заявляю что все кто пользует этого бота должен нам по чакчаку!

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
