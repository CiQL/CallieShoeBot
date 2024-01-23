# Imports required libraries
import interactions
import random
import os

# Initializes the bot
bot = interactions.Client(token=os.environ.get('BOT_TOKEN'))

# Creates list containing the game modifiers
modifiers = ['Randomized Weapons', 'Randomized Weapons', 'Same Random Weapon', 'Same Random Weapon',
             'Two Random Weapons', 'Two Random Weapons', 'Random Weapon Mirror', 'Random Weapon Mirror',
             'Same Random Sub', 'Same Random Sub', 'Same Random Special', 'Same Random Special',
             'Same Random Weapon Class', 'Same Random Weapon Class', 'Enemy Comp Swap', 'Team Comp Swap',
             'Force at Gunpoint', 'Turf War', 'Trade a Player', 'Deathmatch',
             'Rubberband Map Pick', 'Rubberband Modifier Pick', 'Permanent Random Weapon', 'Death',
             'Sacrificial Specials', 'Randomized Gear', 'Besties', 'Killer Wail Kerfuffle', 'Secret Agents',
             'Bubble Bath', 'Double Down', 'Double Down']


@bot.event
async def on_ready():
    print('Bot started successfully.')


# Defines the args and name of the 'spin' command
@interactions.slash_command(name='spin', description='Spin the Wheel.')
async def spin(ctx: interactions.SlashContext):
    # The sole purpose of this is to make the bot shut up
    global embed

    # Selects a random index of the 'modifiers' dictionary
    mod = modifiers[random.randrange(0, len(modifiers))]

    # Randomized Weapons (Boosted Odds)
    if mod == 'Randomized Weapons':
        embed = interactions.Embed(title='Randomized Weapons', color=0x83eeff,
                                   description=f'Each player in the lobby must use the weapon corresponding '
                                               f'with their slot in the team menu.')
        x = 1
        y = 4
        msg = ''
        while x < 3:
            while y > 0:
                if y > 1:
                    weapon = randomWeapon()
                    msg += f'{weapon}\n'
                    y -= 1
                else:
                    weapon = randomWeapon()
                    msg += f'{weapon}'
                    y -= 1
            if x == 1:
                embed.add_field(name=f'Team Alpha:', value=msg, inline=True)
            if x == 2:
                embed.add_field(name=f'Team Bravo:', value=msg, inline=True)
            y = 4
            msg = ''
            x += 1
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Same Random Weapon (Boosted Odds)
    elif mod == 'Same Random Weapon':

        weapon = randomWeapon()
        embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                   description=f'All players must use the __**{weapon}**__ for this game.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Two Random Weapons (Boosted Odds)
    elif mod == 'Two Random Weapons':

        weapon1 = randomWeapon()
        weapon2 = randomWeapon()
        while weapon2 == weapon1:
            weapon2 = randomWeapon()
        embed = interactions.Embed(title='Two Random Weapons', color=0x83eeff,
                                   description=f'Every player may select between __**{weapon1}**__ or __**{weapon2}**__. There must be at least one of each weapon on both teams.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Random Weapon Mirror (Boosted Odds)
    elif mod == 'Random Weapon Mirror':

        x = 0
        weapons = ''
        while x < 4:
            weapons += '**__'
            weapons += randomWeapon()
            weapons += '__**\n'
            x += 1
        embed = interactions.Embed(title='Random Weapon Mirror', color=0x83eeff,
                                   description=f'Each team must select which team member uses each of the following weapons:\n\n{weapons}')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Same Random Sub (Boosted Odds)
    elif mod == 'Same Random Sub':

        sub = randomSub()
        embed = interactions.Embed(title='Same Random Sub', color=0x83eeff,
                                   description=f'All players must use a weapon with __**{sub}**__ for this game. The main abilities on every player’s gear can only be Sub Saver or Sub Power.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Same Random Special (Boosted Odds)
    elif mod == 'Same Random Special':

        special = randomSpecial()
        embed = interactions.Embed(title='Same Random Special', color=0x83eeff,
                                   description=f'All players must use a weapon with __**{special}**__ for this game. The main abilities on every player’s gear can only be Special Charge or Special Power.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Same Random Weapon Class (Boosted Odds)
    elif mod == 'Same Random Weapon Class':

        randClass = randomClass()
        embed = interactions.Embed(title='Same Random Weapon Class', color=0x83eeff,
                                   description=f'All players must use a weapon that is part of the __**{randClass}**__ class for this game. No duplicate weapons are allowed.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Trade Enemy Weapons (Normal Odds)
    elif mod == 'Enemy Comp Swap':

        embed = interactions.Embed(title='Enemy Comp Swap', color=0x83eeff,
                                   description=f'Both teams must use the enemy’s weapons from the previous game. If this is game 1, roll a new modifier. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Trade Team Weapons (Normal Odds)
    elif mod == 'Team Comp Swap':

        embed = interactions.Embed(title='Team Comp Swap', color=0x83eeff,
                                   description=f'Both teams must use the same weapons from the previous game, but they must swap which player uses each weapon. If this is game 1, roll a new modifier. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Force at Gunpoint (Normal Odds)
    elif mod == 'Force at Gunpoint':

        embed = interactions.Embed(title='Force at Gunpoint', color=0x83eeff,
                                   description=f'Each team must select two specific players on the opposite team. Those players must use the weapons that the other team told them to use.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Turf War (Normal Odds)
    elif mod == 'Turf War':

        embed = interactions.Embed(title='Turf War', color=0x83eeff,
                                   description=f'Play Turf War instead of the mode listed on the maplist.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Trade a Player (Normal Odds)
    elif mod == 'Trade a Player':

        embed = interactions.Embed(title='Trade a Player', color=0x83eeff,
                                   description=f'Both teams must trade one of their players to the other team. Your team will choose which teammate to send. The traded teammate can sabotage the enemy team and relay information over VC. Idling is not allowed. Return teammates after the game.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Deathmatch (Normal Odds)
    elif mod == 'Deathmatch':

        embed = interactions.Embed(title='Deathmatch', color=0x83eeff,
                                   description=f'Select Turf War on the current round’s map. The team with the most total kills+assists will win the match.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Rubberband Map Pick (Normal Odds)
    elif mod == 'Rubberband Map Pick':

        embed = interactions.Embed(title='Rubberband Map Pick', color=0x83eeff,
                                   description=f'The team with less points changes the current map/mode to one of their choosing. If both teams are tied, roll a new modifier.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Rubberband Modifier Pick (Normal Odds)
    elif mod == 'Rubberband Modifier Pick':

        embed = interactions.Embed(title='Rubberband Modifier Pick', color=0x83eeff,
                                   description=f'The team with less points chooses the modifier for this round. If both teams are tied, roll a new modifier. You cannot select Double Down.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Permanent Random Weapon (Normal Odds)
    elif mod == 'Permanent Random Weapon':

        embed = interactions.Embed(title='Permanent Random Weapon', color=0x83eeff,
                                   description=f'Roll a number from 1 to 4. On each team, the corresponding player will roll a random weapon separately. They must use this weapon for the rest of the set, regardless of what other modifiers say.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Death (Normal Odds)
    elif mod == 'Death':

        embed = interactions.Embed(title='Death', color=0x83eeff,
                                   description=f'Determine the player with the highest kill count on both teams. Those players will be eliminated from the round. This game will be played as a 3v3.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Sacrificial Specials (Normal Odds)
    elif mod == 'Sacrificial Specials':

        embed = interactions.Embed(title='Sacrificial Specials', color=0x83eeff,
                                   description=f'If a player uses a special during this game, they must jump off the map after the user’s role in using said special is complete. Any weapons are allowed.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Randomized Gear (Normal Odds)
    elif mod == 'Randomized Gear':

        headgear = randomHeadgearAbility()
        clothing = randomClothingAbility()
        shoes = randomShoesAbility()

        embed = interactions.Embed(title='Randomized Gear', color=0x83eeff,
                                   description=f'The main abilities of your gear must match:\nHeadgear - __**{headgear}**__\nClothing - __**{clothing}**\n__Shoes - __**{shoes}**__')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Besties (Normal Odds)
    elif mod == 'Besties':

        embed = interactions.Embed(title='Besties', color=0x83eeff,
                                   description=f'Every player on your team must wear the same gear pieces. There are no restrictions on gear abilities.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Killer Wail Kerfuffle (Normal Odds)
    elif mod == 'Killer Wail Kerfuffle':
        embed = interactions.Embed(title='Killer Wail Kerfuffle', color=0x83eeff,
                                   description=f'Vanilla Splattershot Nova or Vanilla Inkbrush must be selected by all players. This game will be played on Eeltail Alley TC.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Secret Agents (Normal Odds)
    elif mod == 'Secret Agents':

        embed = interactions.Embed(title='Secret Agents', color=0x83eeff,
                                   description=f'Every player must select Undercover Brella. This game will be played on Wahoo World SZ.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Bubble Bath (Normal Odds)
    elif mod == 'Bubble Bath':

        embed = interactions.Embed(title='Bubble Bath', color=0x83eeff,
                                   description=f'Every player must select Vanilla Bloblobber, except for one player on each team who may select Bloblobber Deco. This game will be played on Inkblot Art Academy RM.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    # Double Down (Boosted Odds)
    elif mod == 'Double Down':

        # Generates double down modifiers
        mod1, mod2 = doubleDown()

        # Checks to see if modifiers are the same, if they are then group C was rolled
        if mod1 != mod2:

            if mod1 == 'Randomized Weapons':
                embed = interactions.Embed(title='Randomized Weapons', color=0x83eeff,
                                           description=f'Each player in the lobby must use the weapon corresponding with their slot in the team menu.')
                x = 1
                y = 4
                msg = ''
                while x < 3:
                    while y > 0:
                        if y > 1:
                            weapon = randomWeapon()
                            msg += f'{weapon}\n'
                            y -= 1
                        else:
                            weapon = randomWeapon()
                            msg += f'{weapon}'
                            y -= 1
                    if x == 1:
                        embed.add_field(name=f'Team Alpha:', value=msg, inline=True)
                    if x == 2:
                        embed.add_field(name=f'Team Bravo:', value=msg, inline=True)
                    y = 4
                    msg = ''
                    x += 1
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Same Random Weapon':
                weapon = randomWeapon()
                embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                           description=f'All players must use the __**{weapon}**__ for this game.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Two Random Weapons':

                weapon1 = randomWeapon()
                weapon2 = randomWeapon()
                while weapon2 == weapon1:
                    weapon2 = randomWeapon()
                embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                           description=f'Every player may select between __**{weapon1}**__ or __**{weapon2}**__. There must be at least one of each weapon on both teams.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Same Random Sub':
                sub = randomSub()
                embed = interactions.Embed(title='Same Random Sub', color=0x83eeff,
                                           description=f'All players must use a weapon with __**{sub}**__ for this game. The main abilities on every player’s gear can only be Sub Saver or Sub Power.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Same Random Special':
                special = randomSpecial()
                embed = interactions.Embed(title='Same Random Special', color=0x83eeff,
                                           description=f'All players must use a weapon with __**{special}**__ for this game. The main abilities on every player’s gear can only be Special Charge or Special Power.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Same Random Weapon Class':
                randClass = randomClass()
                embed = interactions.Embed(title='Same Random Weapon Class', color=0x83eeff,
                                           description=f'All players must use a weapon that is part of the __**{randClass}**__ class for this game. No duplicate weapons are allowed.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Enemy Comp Swap':
                embed = interactions.Embed(title='Enemy Comp Swap', color=0x83eeff,
                                           description=f'Both teams must use the enemy’s weapons from the previous game. If this is game 1, roll a new pair of modifiers. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Team Comp Swap':
                embed = interactions.Embed(title='Team Comp Swap', color=0x83eeff,
                                           description=f'Both teams must use the same weapons from the previous game, but they must swap which player uses each weapon. If this is game 1, roll a new pair of modifiers. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Random Weapon Mirror':
                x = 0
                weapons = ''
                while x < 4:
                    weapons += '**__'
                    weapons += randomWeapon()
                    weapons += '__**\n'
                    x += 1
                embed = interactions.Embed(title='Random Weapon Mirror', color=0x83eeff,
                                           description=f'Both teams must select which team member uses each of the following weapons:\n\n{weapons}')
                embed.set_author(name='DOUBLE DOWN')

            elif mod1 == 'Least Favorites':
                embed = interactions.Embed(title='Least Favorites', color=0x83eeff,
                                           description=f'Roll a number from 1 to 8. Have the corresponding player in the lobby find out what their least used weapon is according to Splatnet. Determine this using the “Weapons” tab, and find the weapon lowest on the “Most Used” list that still has at least 1 Win. All players must use that weapon.')
                embed.set_author(name='DOUBLE DOWN')

            if mod2 == 'Turf War':
                embed.add_field(name='Turf War', value=f'Play Turf War instead of the mode listed on the maplist.')

            elif mod2 == 'Trade a Player':
                embed.add_field(name='Trade a Player',
                                value=f'Both teams must trade one of their players to the other team. Your team will choose which teammate to send. The traded teammate can sabotage the enemy team and relay information over VC. Idling is not allowed. Return teammates after the game.')

            elif mod2 == 'Deathmatch':
                embed.add_field(name='Deathmatch',
                                value=f'Select Turf War on the current round’s map. The team with the most total kills will win the match.')

            elif mod2 == 'Rubberband Map Pick':
                embed.add_field(name='Rubberband Map Pick',
                                value=f'The team with less points changes the current map/mode to one of their choosing. If both teams are tied, roll a new pair of modifiers.')

            elif mod2 == 'Death':
                embed.add_field(name='Death',
                                value=f'Determine the player with the highest kill count on both teams. Those players will be eliminated from the round. This game will be played as a 3v3.')

            elif mod2 == 'Permanent Random Weapon':
                embed.add_field(name='Permanent Random Weapon',
                                value=f'Roll a number from 1 to 4. After following the other weapon selection rule, the rolled number slot on each team must use their weapon for the remainder of the set regardless of what other modifiers say.')

            elif mod2 == 'Besties':
                embed.add_field(name='Besties',
                                value=f'Every player on your team must wear the same gear pieces. There are no restrictions on gear abilities.')

            elif mod2 == 'Sacrificial Specials':
                embed.add_field(name='No Specials',
                                value=f'If a player uses a special during this game, they must jump off the map after the user’s role in using said special is complete. Any weapons are allowed.')

            elif mod2 == 'Randomized Gear':
                headgear = randomHeadgearAbility()
                clothing = randomClothingAbility()
                shoes = randomShoesAbility()
                embed.add_field(name='Randomized Gear',
                                value=f'The main abilities of your gear must match:\nHeadgear - __**{headgear}**__\nClothing - __**{clothing}**\n__Shoes - __**{shoes}**__')

        else:

            if mod1 == 'Same Random Weapon':
                weapon1 = randomWeapon()
                weapon2 = randomWeapon()
                embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                           description=f'All players must use the __**{weapon1}**__ or __**{weapon2}**__ for this game.')

            elif mod1 == 'Same Random Sub':
                sub1 = randomSub()
                sub2 = randomSub()
                embed = interactions.Embed(title='Same Random Sub', color=0x83eeff,
                                           description=f'All players must use a weapon with __**{sub1}**__ or __**{sub2}**__ for this game. The main abilities on every player’s gear can only be Sub Saver or Sub Power.')

            elif mod1 == 'Same Random Special':
                special1 = randomSpecial()
                special2 = randomSpecial()
                embed = interactions.Embed(title='Same Random Special', color=0x83eeff,
                                           description=f'All players must use the __**{special1}**__ or __**{special2}**__ for this game. The main abilities on every player’s gear can only be Special Charge or Special Power.')

            elif mod1 == 'Same Random Weapon Class':
                class1 = randomClass()
                class2 = randomClass()
                embed = interactions.Embed(title='Same Random Weapon Class', color=0x83eeff,
                                           description=f'All players must use a weapon that is part of the __**{class1}**__ class or __**{class2}**__ class for this game. No duplicate weapons are allowed.')

        embed.set_author(name='DOUBLE DOWN')

    # Indicates that something has gone wrong
    else:
        embed = interactions.Embed(title='ERROR: INVALID ROLL', color=0x83eeff,
                                   description=f'Something has gone wrong. Please ping or DM <@371465781260845058> to see what went wrong.')
        embed.set_author(name='THE WHEEL HAS SPOKEN')

    embed.set_footer(text='')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'roll' command
@interactions.slash_command(name='roll', description='Rolls a die with the specified amount of sides.')
@interactions.slash_option(opt_type=interactions.OptionType.INTEGER, name='value', description='number of sides of a die')
async def roll(ctx: interactions.SlashContext, value):
    await ctx.send(f'You rolled a {random.randrange(1, value + 1)}.')


# Defines the args and name of the 'flip' command
@interactions.slash_command(name='flip', description='Heads or Tails?')
async def flip(ctx: interactions.SlashContext):
    num = random.randrange(0, 2)
    if num == 0:
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')


# Defines the args and name of the 'weapons' command
@interactions.slash_command(name='weapons', description='Selects random weapon(s)')
@interactions.slash_option(opt_type=interactions.OptionType.INTEGER, name="amount",
                     description="Choose the amount of weapons to generate.", required=True)
async def weapons(ctx: interactions.SlashContext, amount: int):
    arg = amount
    if arg <= 12:
        str = ''
        while arg >= 1:
            str += randomWeapon() + '\n'
            arg -= 1
        embed = interactions.Embed(title='Weapons List', description=f'{str}', color=0x83eeff)
        embed.set_footer(text='')
        await ctx.send(embeds=embed)
    else:
        await ctx.send(
            'There is a limit of 12 weapons that can be generated at once, please lower the amount specified.')


# Defines the args and name of the 'sub' command
@interactions.slash_command(name='sub', description='Generates a random subweapon')
async def sub(ctx: interactions.SlashContext):
    sub = randomSub()
    embed = interactions.Embed(title='Random Sub:', description=f'{sub}', color=0x83eeff)
    embed.set_footer(text='')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'class' command
@interactions.slash_command(name='class', description='Generates a random weapon class')
async def Class(ctx: interactions.SlashContext):
    randClass = randomClass()
    embed = interactions.Embed(title='Random Class:', description=f'{randClass}', color=0x83eeff)
    embed.set_footer(text='')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'special' command
@interactions.slash_command(name='special', description='Generates a random special.')
async def special(ctx: interactions.SlashContext):
    special = randomSpecial()

    # Selects a random index of the 'modifiers' dictionary
    embed = interactions.Embed(title='Random Special:', color=0x83eeff, description=f'{special}')
    embed.set_footer(text='')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'maplist' command
@interactions.slash_command(name='maplist', description='Generates [num] random map(s).')
@interactions.slash_option(name='amount', description='The amount of maps you would like to generate.', opt_type=interactions.OptionType.INTEGER,
                     required=True)
async def mapList(ctx: interactions.SlashContext, amount: int):
    maps = ['Scorch Gorge', 'Eeltail Alley', 'Hagglefish Market', 'Undertow Spillway', 'Mincemeat Metalworks',
            'Hammerhead Bridge', 'Museum D\'Alfonsino', 'Mahi-Mahi Resort', 'Inkblot Art Academy',
            'Sturgeon Shipyard', 'MakoMart', 'Wahoo World']
    gameModes = ['Splat Zones', 'Tower Control', 'Rainmaker', 'Clam Blitz']

    num = amount

    length1 = 0
    for x in maps:
        length1 += 1

    length2 = 0
    for x in gameModes:
        length2 += 1

    msg = ''

    if int(num) <= 0:
        return await ctx.send('Invalid Input: Input a positive number')
    while num > 0:
        if num > 1:

            num1 = random.randrange(0, length1)
            msg += f'{maps[num1]} - '

            num1 = random.randrange(0, length2)
            msg += f'{gameModes[num1]}\n'

            num -= 1
        else:

            num1 = random.randrange(0, length1)
            msg += f'{maps[num1]} - '

            num1 = random.randrange(0, length2)
            msg += f'{gameModes[num1]}'

            num -= 1
    embed = interactions.Embed(title='Maps:', color=0x83eeff, description=msg)
    embed.set_footer(text='')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'doubledown' command
@interactions.slash_command(name='doubledown', description='Generates 2 random modifiers.')
async def doubledown(ctx: interactions.SlashContext):
    # The sole purpose of this is to make the bot shut up
    global embed

    # Generates two modifiers
    mod1, mod2 = doubleDown()

    # Checks if
    if mod1 != mod2:

        if mod1 == 'Randomized Weapons':
            embed = interactions.Embed(title='Randomized Weapons', color=0x83eeff,
                                       description=f'Each player in the lobby must use the weapon corresponding with '
                                                   f'their slot in the team menu.')
            x = 1
            y = 4
            msg = ''
            while x < 3:
                while y > 0:
                    if y > 1:
                        weapon = randomWeapon()
                        msg += f'{weapon}\n'
                        y -= 1
                    else:
                        weapon = randomWeapon()
                        msg += f'{weapon}'
                        y -= 1
                if x == 1:
                    embed.add_field(name=f'Team Alpha:', value=msg, inline=True)
                if x == 2:
                    embed.add_field(name=f'Team Bravo:', value=msg, inline=True)
                y = 4
                msg = ''
                x += 1
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Same Random Weapon':
            weapon = randomWeapon()
            embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                       description=f'All players must use the __**{weapon}**__ for this game.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Two Random Weapons':

            weapon1 = randomWeapon()
            weapon2 = randomWeapon()
            while weapon2 == weapon1:
                weapon2 = randomWeapon()
            embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                       description=f'Every player may select between __**{weapon1}**__ or __**{weapon2}**__. There must be at least one of each weapon on both teams.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Same Random Sub':
            sub = randomSub()
            embed = interactions.Embed(title='Same Random Sub', color=0x83eeff,
                                       description=f'All players must use a weapon with __**{sub}**__ for this game. The main abilities on every player’s gear can only be Sub Saver or Sub Power.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Same Random Special':
            special = randomSpecial()
            embed = interactions.Embed(title='Same Random Special', color=0x83eeff,
                                       description=f'All players must use a weapon with __**{special}**__ for this game. The main abilities on every player’s gear can only be Special Charge or Special Power.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Same Random Weapon Class':
            randClass = randomClass()
            embed = interactions.Embed(title='Same Random Weapon Class', color=0x83eeff,
                                       description=f'All players must use a weapon that is part of the __**{randClass}**__ for this game. No duplicate weapons are allowed.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Enemy Comp Swap':
            embed = interactions.Embed(title='Enemy Comp Swap', color=0x83eeff,
                                       description=f'Both teams must use the enemy’s weapons from the previous game. If this is game 1, roll a new modifier. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Team Comp Swap':
            embed = interactions.Embed(title='Team Comp Swap', color=0x83eeff,
                                       description=f'Both teams must use the same weapons from the previous game, but they must swap which player uses each weapon. If this is game 1, roll a new modifier. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Random Weapon Mirror':
            x = 0
            weapons = ''
            while x < 4:
                weapons += '**__'
                weapons += randomWeapon()
                weapons += '__**\n'
                x += 1
            embed = interactions.Embed(title='Random Weapon Mirror', color=0x83eeff,
                                       description=f'Both teams must select which team member uses each of the following weapons:\n\n{weapons}')
            embed.set_author(name='DOUBLE DOWN')

        elif mod1 == 'Least Favorites':
            embed = interactions.Embed(title='Least Favorites', color=0x83eeff,
                                       description=f'Roll a number from 1 to 8. Have the corresponding player in the lobby find out what their least used weapon is according to Splatnet. Determine this using the “Weapons” tab, and find the weapon lowest on the “Most Used” list that still has at least 1 Win. All players must use that weapon.')
            embed.set_author(name='DOUBLE DOWN')

        if mod2 == 'Turf War':
            embed.add_field(name='Turf War', value=f'Play Turf War instead of the mode listed on the maplist.')

        elif mod2 == 'Trade a Player':
            embed.add_field(name='Trade a Player',
                            value=f'Both teams must trade one of their players to the other team. Your team will choose which teammate to send. The traded teammate can sabotage the enemy team and relay information over VC. Idling is not allowed. Return teammates after the game.')

        elif mod2 == 'Deathmatch':
            embed.add_field(name='Deathmatch',
                            value=f'Select Turf War on the current round’s map. The team with the most total kills will win the match.')

        elif mod2 == 'Rubberband Map Pick':
            embed.add_field(name='Rubberband Map Pick',
                            value=f'The team with less points changes the current map/mode to one of their choosing. If both teams are tied, roll a new modifier.')

        elif mod2 == 'Death':
            embed.add_field(name='Death',
                            value=f'Flip a coin. If heads, determine the player with the highest kill count on both teams. If tails, determine the player with the lowest paint on both teams. After determining these players, they will be eliminated from the round. This game will be played as a 3v3.')

        elif mod2 == 'Permanent Random Weapon':
            embed.add_field(name='Permanent Random Weapon',
                            value=f'Follow the rule of the other weapon selection modifier. After selecting the weapon as required, you cannot change weapons for the remainder of the set, regardless of what other modifiers say.')

        elif mod2 == 'Besties':
            embed.add_field(name='Besties',
                            value=f'Every player on your team must wear the same gear pieces. There are no restrictions on gear abilities.')

        elif mod2 == 'Sacrificial Specials':
            embed.add_field(name='No Specials',
                            value=f'Players are not allowed to use their specials in this game. Any weapons are allowed.')

        elif mod2 == 'Randomized Gear':
            headgear = randomHeadgearAbility()
            clothing = randomClothingAbility()
            shoes = randomShoesAbility()
            embed.add_field(name='Randomized Gear',
                            value=f'The main abilities of your gear must match:\nHeadgear - __**{headgear}**__\nClothing - __**{clothing}**\n__Shoes - __**{shoes}**__')

    else:

        if mod1 == 'Same Random Weapon':
            weapon1 = randomWeapon()
            weapon2 = randomWeapon()
            embed = interactions.Embed(title='Same Random Weapon', color=0x83eeff,
                                       description=f'All players must use the __**{weapon1}**__ or __**{weapon2}**__ for this game.')

        elif mod1 == 'Same Random Sub':
            sub1 = randomSub()
            sub2 = randomSub()
            embed = interactions.Embed(title='Same Random Sub', color=0x83eeff,
                                       description=f'All players must use a weapon with __**{sub1}**__ or __**{sub2}**__ for this game. The main abilities on every player’s gear can only be Sub Saver or Sub Power.')

        elif mod1 == 'Same Random Special':
            special1 = randomSpecial()
            special2 = randomSpecial()
            embed = interactions.Embed(title='Same Random Special', color=0x83eeff,
                                       description=f'All players must use the __**{special1}**__ or __**{special2}**__ for this game. The main abilities on every player’s gear can only be Special Charge or Special Power.')

        elif mod1 == 'Same Random Weapon Class':
            class1 = randomClass()
            class2 = randomClass()
            embed = interactions.Embed(title='Same Random Weapon Class', color=0x83eeff,
                                       description=f'All players must use a weapon that is part of the __**{class1}**__ class or __**{class2}**__ class for this game. No duplicate weapons are allowed.')

    await ctx.send(embeds=embed)


# Defines the args and name of the 'help' command
@interactions.slash_command(name='help', description='Explains the various commands this bot can execute.')
async def help(ctx: interactions.SlashContext):
    embed = interactions.Embed(title='Commands', color=0x83eeff)
    embed.add_field(name='/spin', value='Selects a random game modifier')
    embed.add_field(name='/weapons [num]', value='Generates a specified amount of random weapons')
    embed.add_field(name='/sub', value='Selects a random sub weapon')
    embed.add_field(name='/special', value='Selects a random special')
    embed.add_field(name='/class', value='Selects a random weapon class')
    embed.add_field(name='/maplist [x]', value='Selects [x] random maps and game modes')
    embed.add_field(name='/doubledown', value='The wheel has spoken')
    embed.set_footer(text='')
    await ctx.send(embeds=embed)


def randomWeapon():
    weapon = ['.52 Gal', '.96 Gal', '.96 Gal Deco', 'Aerospray MG', 'Aerospray RG', 'Annaki Splattershot Nova',
              'Ballpoint Splatling', 'Ballpoint Splatling Noveau', 'Bamboozler 14 Mk I', 'Big Swig Roller',
              'Big Swig Roller Express', 'Blaster', 'Bloblobber', 'Bloblobber Deco', 'Carbon Roller',
              'Carbon Roller Deco',
              'Clash Blaster', 'Clash Blaster Neo', 'Classic Squiffer', 'Custom Blaster', 'Custom Dualie Squelchers',
              'Custom Goo Tuber', 'Custom Jet Squelcher', 'Custom Splattershot Jr.', 'Dapple Dualies',
              'Dapple Dualies Nouveau',
              'Dark Tetra Dualies', 'Dread Wringer', 'Dualie Squelchers', 'Dynamo Roller', 'E-liter 4K',
              'E-liter 4K Scope',
              'Enperry Splat Dualies', 'Explosher', 'Flingza Roller', 'Forge Splattershot Pro',
              'Glooga Dualies', 'Goo Tuber', 'H-3 Nozzlenose', 'H-3 Nozzlenose D', 'Heavy Edit Splatling',
              'Heavy Splatling',
              'Heavy Splatling Deco', 'Hero Shot Replica', 'Hydra Splatling', 'Inkbrush', 'Inkbrush Nouveau',
              'Inkline Tri-Stringer',
              'Jet Squelcher', 'Krak-On Splat Roller', 'L-3 Nozzlenose', 'L-3 Nozzlenose D', 'Light Tetra Dualies',
              'Luna Blaster', 'Luna Blaster Neo', 'Mini Splatling', 'N-ZAP \'85', 'N-ZAP \'89', 'Nautilus 47',
              'Neo Splash-o-matic',
              'Neo Splatana Stamper', 'Neo Sploosh-o-matic', 'Octobrush', 'Octobrush Nouveau', 'Painbrush',
              'Painbrush Nouveau',
              'Range Blaster', 'Rapid Blaster', 'Rapid Blaster Deco', 'Rapid Blaster Pro', 'Rapid Blaster Pro Deco',
              'REEF-LUX 450', 'REEF-LUX 450 Deco', 'S-BLAST \'91', 'S-BLAST \'92', 'Slosher', 'Slosher Deco',
              'Sloshing Machine', 'Sloshing Machine Neo', 'Snipewriter 5B', 'Snipewriter 5H', 'Sorella Brella',
              'Splash-o-matic', 'Splat Brella', 'Splat Charger', 'Splat Dualies', 'Splat Roller',
              'Splatana Stamper', 'Splatana Wiper', 'Splatana Wiper Deco', 'Splatterscope', 'Splattershot',
              'Splattershot Jr.',
              'Splatter Shot Nova', 'Splattershot Pro', 'Sploosh-o-matic', 'Squeezer', 'Tenta Brella',
              'Tenta Sorella Brella',
              'Tentatek Splattershot', 'Tri-Slosher', 'Tri-Slosher Nouveau', 'Tri-Stringer', 'Undercover Brella',
              'Z+F Splat Charger', 'Z+F Splatterscope', 'Zink Mini Splatling']

    length = 0
    for x in weapon:
        length += 1

    num = random.randrange(0, length)
    return weapon[num]


def randomSub():
    subs = ['Splat Bomb', 'Suction Bomb', 'Burst Bomb', 'Curling Bomb', 'Autobomb', 'Ink Mine', 'Toxic Mist',
            'Point Sensor', 'Splash Wall', 'Sprinkler', 'Squid Beakon', 'Fizzy Bomb', 'Torpedo', 'Angle Shooter']

    length = 0
    for x in subs:
        length += 1

    num = random.randrange(0, length)
    return subs[num]


def randomSpecial():
    specials = ['Inkjet', 'Ink Storm', 'Booyah Bomb', 'Ultra Stamp', 'Trizooka', 'Big Bubbler', 'Zipcaster',
                'Wavebreaker', 'Ink Vac', 'Killer Wail 5.1', 'Crab Tank', 'Reefslider', 'Tacticooler',
                'Triple Inkstrike',
                'Triple Splashdown']

    length = 0
    for x in specials:
        length += 1

    num = random.randrange(0, length)
    return specials[num]


def randomClass():
    classes = ['Shooter', 'Roller', 'Charger', 'Dualies', 'Brella', 'Splatling', 'Blaster', 'Brush', 'Stringer',
               'Splatana']

    length = 0
    for x in classes:
        length += 1

    num = random.randrange(0, length)
    return classes[num]


def randomHeadgearAbility():
    headgearAbility = ['Ink Saver (Main)', 'Ink Saver (Sub)', 'Ink Recovery Up', 'Run Speed Up', 'Swim Speed Up',
                       'Special Charge Up', 'Special Saver', 'Special Power Up', 'Quick Respawn', 'Quick Super Jump',
                       'Sub Power Up', 'Ink Resistance Up', 'Sub Resistance Up', 'Intensify Action', 'Opening Gambit',
                       'Last-Ditch Effort', 'Tenacity', 'Comeback']

    length = 0
    for x in headgearAbility:
        length += 1

    num = random.randrange(0, length)
    return headgearAbility[num]


def randomClothingAbility():
    clothingAbility = ['Ink Saver (Main)', 'Ink Saver (Sub)', 'Ink Recovery Up', 'Run Speed Up', 'Swim Speed Up',
                       'Special Charge Up', 'Special Saver', 'Special Power Up', 'Quick Respawn', 'Quick Super Jump',
                       'Sub Power Up', 'Ink Resistance Up', 'Sub Resistance Up', 'Intensify Action', 'Ninja Squid',
                       'Haunt', 'Thermal Ink', 'Respawn Punisher']

    length = 0
    for x in clothingAbility:
        length += 1

    num = random.randrange(0, length)
    return clothingAbility[num]


def randomShoesAbility():
    shoesAbility = ['Ink Saver (Main)', 'Ink Saver (Sub)', 'Ink Recovery Up', 'Run Speed Up', 'Swim Speed Up',
                    'Special Charge Up', 'Special Saver', 'Special Power Up', 'Quick Respawn', 'Quick Super Jump',
                    'Sub Power Up', 'Ink Resistance Up', 'Sub Resistance Up', 'Intensify Action', 'Stealth Jump',
                    'Object Shredder', 'Drop Roller']

    length = 0
    for x in shoesAbility:
        length += 1

    num = random.randrange(0, length)
    return shoesAbility[num]


def doubleDown():
    # Defines the groups that double down may select from
    groupA = ['Randomized Weapons', 'Same Random Weapon', 'Two Random Weapons', 'Random Weapon Mirror',
              'Same Random Sub', 'Same Random Special', 'Same Random Weapon Class', 'Enemy Comp Swap', 'Team Comp Swap']
    groupB = ['Turf War', 'Trade a Player', 'Deathmatch', 'Rubberband Map Pick', 'Death', 'Permanent Random Weapon',
              'Besties', 'Sacrificial Specials', 'Randomized Gear']
    groupC = ['Same Random Weapon', 'Same Random Sub', 'Same Random Special', 'Same Random Weapon Class']

    # Sets a 20% chance of group C being selected
    randNum = random.randrange(1, 5)

    if randNum > 1:

        mod1 = groupA[random.randrange(0, len(groupA))]
        mod2 = groupB[random.randrange(0, len(groupB))]

        return mod1, mod2

    else:

        mod1 = groupC[random.randrange(0, len(groupC))]
        mod2 = mod1

        return mod1, mod2


# Ensures that the bot boots properly
bot.start()
