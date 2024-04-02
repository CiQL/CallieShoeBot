# Imports required libraries
import interactions
from interactions.ext import prefixed_commands
# libraries included with Python
import os
import random
#from typing import Union
# ctx: Union[interactions.SlashContext, prefixed_commands.PrefixedContext]

# Constants & global variables
_COLOR = 0x83eeff
_COLOR_ERROR = 0xff0000




embed = interactions.Embed(title='Empty', color=_COLOR_ERROR, description=f'Empty embed. Something has gone wrong.')


# Initializes the bot
bot = interactions.Client(token=os.environ.get('BOT_TOKEN'))
prefixed_commands.setup(bot)

@bot.event
async def on_ready():
    print('Bot started successfully.')


# Defines the args and name of the 'spin' command
@interactions.slash_command(name='spin', description='Spin the Wheel.')
async def spin(ctx: interactions.SlashContext):
    await ctx.send(embeds=modifier_function())


@prefixed_commands.prefixed_command(name='spin')
async def spin_prefix(ctx: prefixed_commands.PrefixedContext):
    await ctx.send(embeds=modifier_function())


# Defines the args and name of the 'roll' command
@interactions.slash_command(name='roll', description='Rolls a die with the specified amount of sides.')
@interactions.slash_option(opt_type=interactions.OptionType.INTEGER, name='value', description='number of sides of a die')
async def roll(ctx: interactions.SlashContext, value: int):
    await ctx.send(f'You rolled a {random.randint(1, value)}.')


@prefixed_commands.prefixed_command(name='roll')
async def roll_prefix(ctx: prefixed_commands.PrefixedContext, value: int):
    await ctx.send(f'You rolled a {random.randint(1, value)}.')


# Defines the args and name of the 'flip' command
@interactions.slash_command(name='flip', description='Heads or Tails?')
async def flip(ctx: interactions.SlashContext):
    await ctx.send(random.choice(['Heads', 'Tails']))


@prefixed_commands.prefixed_command(name='flip')
async def flip_prefix(ctx: prefixed_commands.PrefixedContext):
    await ctx.send(random.choice(['Heads', 'Tails']))


# Defines the args and name of the 'weapons' command
@interactions.slash_command(name='weapons', description='Selects random weapon(s)')
@interactions.slash_option(opt_type=interactions.OptionType.INTEGER, name="amount",
                     description="Choose the amount of weapons to generate.", required=True)
async def weapons(ctx: interactions.SlashContext, amount: int):
    if amount <= 12:
        embed = interactions.Embed(title='Weapons List', color=_COLOR,
                               description='\n'.join([randomWeapon() for _ in range(amount)]))
        await ctx.send(embeds=embed)
    else:
        await ctx.send('There is a limit of 12 weapons that can be generated at once, please lower the amount specified.')


@prefixed_commands.prefixed_command(name='weapons')
async def weapons_prefix(ctx: prefixed_commands.PrefixedContext, amount: int):
    if amount <= 12:
        embed = interactions.Embed(title='Weapons List', color=_COLOR,
                               description='\n'.join([randomWeapon() for _ in range(amount)]))
        await ctx.send(embeds=embed)
    else:
        await ctx.send('There is a limit of 12 weapons that can be generated at once, please lower the amount specified.')


# Defines the args and name of the 'sub' command
@interactions.slash_command(name='sub', description='Generates a random subweapon')
async def sub(ctx: interactions.SlashContext):
    embed = interactions.Embed(title='Random Sub:', color=_COLOR, description=f'{randomSub()}')
    await ctx.send(embeds=embed)


@prefixed_commands.prefixed_command(name='sub')
async def sub_prefix(ctx: prefixed_commands.PrefixedContext):
    embed = interactions.Embed(title='Random Sub:', color=_COLOR, description=f'{randomSub()}')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'class' command
@interactions.slash_command(name='class', description='Generates a random weapon class')
async def Class(ctx: interactions.SlashContext):
    embed = interactions.Embed(title='Random Class:', color=_COLOR, description=f'{randomClass()}')
    await ctx.send(embeds=embed)


@prefixed_commands.prefixed_command(name='class')
async def Class_prefix(ctx: prefixed_commands.PrefixedContext):
    embed = interactions.Embed(title='Random Class:', color=_COLOR, description=f'{randomClass()}')
    await ctx.send(embeds=embed)


# Defines the args and name of the 'special' command
@interactions.slash_command(name='special', description='Generates a random special.')
async def special(ctx: interactions.SlashContext):
    embed = interactions.Embed(title='Random Special:', color=_COLOR, description=f'{randomSpecial()}')
    await ctx.send(embeds=embed)


@prefixed_commands.prefixed_command(name='special')
async def special_prefix(ctx: prefixed_commands.PrefixedContext):
    embed = interactions.Embed(title='Random Special:', color=_COLOR, description=f'{randomSpecial()}')
    await ctx.send(embeds=embed)

# Defines the args and name of the 'maplist' command
@interactions.slash_command(name='maplist', description='Generates [num] random map(s).')
@interactions.slash_option(name='amount', description='The amount of maps you would like to generate.', opt_type=interactions.OptionType.INTEGER,
                     required=True)
async def maplist(ctx: interactions.SlashContext, amount: int):
    await ctx.send(embeds=maplist_function(amount))


@prefixed_commands.prefixed_command(name='maplist')
async def maplist_prefix(ctx: prefixed_commands.PrefixedContext, amount: int):
    await ctx.send(embeds=maplist_function(amount))


# Defines the args and name of the 'doubledown' command
@interactions.slash_command(name='doubledown', description='Generates 2 random modifier_pool.')
async def doubledown(ctx: interactions.SlashContext):
    await ctx.send(embed=doubledown_function())


@prefixed_commands.prefixed_command(name='doubledown')
async def doubledown_prefix(ctx: prefixed_commands.PrefixedContext):
    await ctx.send(embed=doubledown_function())


# Defines the args and name of the 'help' command
@interactions.slash_command(name='help', description='Explains the various commands this bot can execute.')
async def Help(ctx: interactions.SlashContext):
    embed = interactions.Embed(title='Commands', color=_COLOR)
    embed.add_field(name='/spin', value='Selects a random game modifier')
    embed.add_field(name='/weapons [num]', value='Generates a specified amount of random weapons')
    embed.add_field(name='/sub', value='Selects a random sub weapon')
    embed.add_field(name='/special', value='Selects a random special')
    embed.add_field(name='/class', value='Selects a random weapon class')
    embed.add_field(name='/maplist [x]', value='Selects [x] random maps and game modes')
    embed.add_field(name='/doubledown', value='The wheel has spoken')
    embed.set_footer(text='')
    await ctx.send(embeds=embed)


@prefixed_commands.prefixed_command(name='help')
async def Help_prefix(ctx: prefixed_commands.PrefixedContext):
    embed = interactions.Embed(title='Commands', color=_COLOR)
    embed.add_field(name='/spin', value='Selects a random game modifier')
    embed.add_field(name='/weapons [num]', value='Generates a specified amount of random weapons')
    embed.add_field(name='/sub', value='Selects a random sub weapon')
    embed.add_field(name='/special', value='Selects a random special')
    embed.add_field(name='/class', value='Selects a random weapon class')
    embed.add_field(name='/maplist [x]', value='Selects [x] random maps and game modes')
    embed.add_field(name='/doubledown', value='The wheel has spoken')
    embed.set_footer(text='')
    await ctx.send(embeds=embed)



# HELPER FUNCTIONS
def ensure_two_different(randomFunction):
    one = randomFunction()
    two = randomFunction()
    while two == one:
        two = randomFunction()
    return (one, two)

def maplist_function(amount: int):
    maps = [
        'Scorch Gorge',
        'Eeltail Alley',
        'Hagglefish Market',
        'Undertow Spillway',
        'Mincemeat Metalworks',
        'Hammerhead Bridge',
        'Museum D\'Alfonsino',
        'Mahi-Mahi Resort',
        'Inkblot Art Academy',
        'Sturgeon Shipyard',
        'MakoMart',
        'Wahoo World',
        'Brinewater Springs',
        'Flounder Heights',
        'Um\'ami Ruins',
        'Manta Maria',
        'Barnacle & Dime',
        'Humpback Pump Track',
        'Crableg Capital',
        'Shipshape Cargo Co.',
        'Robo ROM-en',
        'Bluefin Depot',
        'Marlin Airport'
        ]
    game_modes = ['Splat Zones', 'Tower Control', 'Rainmaker', 'Clam Blitz']

    if int(amount) <= 0:
        return interactions.Embed(title='Error', color=_COLOR_ERROR, description='Invalid Input: Input a positive number')
    if int(amount) > 50:
        return interactions.Embed(title='Error', color=_COLOR_ERROR, description='Invalid Input: Cannot send over 50 maps!')

    msg = [f'{random.choice(maps)} - {random.choice(game_modes)}' for _ in range(amount)]
    embed = interactions.Embed(title='Maps:', color=_COLOR, description='\n'.join(msg))
    return embed


def modifier_function(mod: str = ''):
    if mod == '':
        mod = randomModifier()
    match mod:
        # Randomized Weapons (Boosted Odds)
        case 'Randomized Weapons':
            embed = interactions.Embed(title='Randomized Weapons', color=_COLOR,
                                        description=f'Each player in the lobby must use the weapon corresponding with their slot in the team menu.')
            teams = ['Alpha', 'Bravo']
            for team_name in teams:
                weapons = [randomWeapon() for _ in range(4)]
                msg =  '\n'.join(weapons)
                embed.add_field(name=f'Team {team_name}:', value=msg, inline=True)

        # Same Random Weapon (Boosted Odds)
        case 'Same Random Weapon':
            embed = interactions.Embed(title='Same Random Weapon', color=_COLOR,
                                   description=f'All players must use the __**{randomWeapon()}**__ for this game.')

        # Two Random Weapons (Boosted Odds)
        case 'Two Random Weapons':
            weapon1, weapon2 = ensure_two_different(randomWeapon)
            embed = interactions.Embed(title='Two Random Weapons', color=_COLOR,
                                    description=f'Every player may select between __**{weapon1}**__ or __**{weapon2}**__. There must be at least one of each weapon on both teams.')

        # Random Weapon Mirror (Boosted Odds)
        case 'Random Weapon Mirror':
            weapons = [f'**__{randomWeapon()}__**' for _ in range(4)]
            embed = interactions.Embed(title='Random Weapon Mirror', color=_COLOR,
                                    description=f'Each team must select which team member uses each of the following weapons:\n\n' + "\n".join(weapons))

        # Same Random Sub (Boosted Odds)
        case 'Same Random Sub':
            embed = interactions.Embed(title='Same Random Sub', color=_COLOR,
                                   description=f'All players must use a weapon with __**{randomSub()}**__ for this game.')

        # Same Random Special (Boosted Odds)
        case 'Same Random Special':
            embed = interactions.Embed(title='Same Random Special', color=_COLOR,
                                   description=f'All players must use a weapon with __**{randomSpecial()}**__ for this game.')

        # Same Random Weapon Class (Boosted Odds)
        case 'Same Random Weapon Class':
            embed = interactions.Embed(title='Same Random Weapon Class', color=_COLOR,
                                   description=f'All players must use a weapon that is part of the __**{randomClass()}**__ class for this game. No duplicate weapons are allowed.')

                # Process group C mods (implies both mod1 and mod2 are equivalent)
        case 'Same Random Weapon (DD)':
            weapon1, weapon2 = ensure_two_different(randomWeapon)
            embed = interactions.Embed(title='Same Random Weapon', color=_COLOR,
                                   description=f'All players must use the __**{weapon1}**__ or __**{weapon2}**__ for this game.')

        case 'Same Random Sub (DD)':
            sub1, sub2 = ensure_two_different(randomSub)
            embed = interactions.Embed(title='Same Random Sub', color=_COLOR,
                                   description=f'All players must use a weapon with __**{sub1}**__ or __**{sub2}**__ for this game.')

        case 'Same Random Special (DD)':
            special1, special2 = ensure_two_different(randomSpecial)
            embed = interactions.Embed(title='Same Random Special', color=_COLOR,
                                   description=f'All players must use the __**{special1}**__ or __**{special2}**__ for this game.')

        case 'Same Random Weapon Class (DD)':
            class1, class2 = ensure_two_different(randomClass)
            embed = interactions.Embed(title='Same Random Weapon Class', color=_COLOR,
                                   description=f'All players must use a weapon that is part of the __**{class1}**__ class or __**{class2}**__ class for this game. No duplicate weapons are allowed.')

        # Trade Enemy Weapons (Normal Odds)
        case 'Enemy Comp Swap':
            embed = interactions.Embed(title='Enemy Comp Swap', color=_COLOR,
                                   description=f'Both teams must use the enemy’s weapons from the previous game.\n\n*If this is game 1, roll a new modifier. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.*')

        # Trade Team Weapons (Normal Odds)
        case 'Team Comp Swap':
            embed = interactions.Embed(title='Team Comp Swap', color=_COLOR,
                                   description=f'Both teams must use the same weapons from the previous game, but they must swap which player uses each weapon.\n\n*If this is game 1, roll a new modifier. If you roll this after “Trade a Player,” team comps are based on the scoreboard, not the traded players.*')

        # Force at Gunpoint (Normal Odds)
        case 'Force at Gunpoint':
            embed = interactions.Embed(title='Force at Gunpoint', color=_COLOR,
                                   description=f'Each team must select two specific players on the opposite team. Those players must use the weapons that the other team told them to use.')

        # Turf War (Normal Odds)
        case 'Turf War':
            embed = interactions.Embed(title='Turf War', color=_COLOR,
                                   description=f'The upcoming game mode is Turf War. *Play Turf War instead of the mode listed on the maplist.*')

        # Trade a Player (Normal Odds)
        case 'Trade a Player':
            embed = interactions.Embed(title='Trade a Player', color=_COLOR,
                                   description=f'Both teams must trade one of their players to the other team. *Your team will choose which teammate to send. The traded teammate can sabotage the enemy team and relay information over VC. Idling is not allowed. Return teammates after the game.*')

        # Deathmatch (Normal Odds)
        case 'Deathmatch':
            embed = interactions.Embed(title='Deathmatch', color=_COLOR,
                                   description=f'Select Turf War on the current round’s map. The team with the most total kills+assists will win the match.')

        # Rubberband Map Pick (Normal Odds)
        case 'Rubberband Map Pick':
            embed = interactions.Embed(title='Rubberband Map Pick', color=_COLOR,
                                   description=f'The team with less points changes the current map/mode to one of their choosing.\n\n*If both teams are tied, roll a new modifier.*')

        # Rubberband Modifier Pick (Normal Odds)
        case 'Rubberband Modifier Pick':
            embed = interactions.Embed(title='Rubberband Modifier Pick', color=_COLOR,
                                   description=f'The team with less points chooses the modifier for this round.\n\n*If both teams are tied, roll a new modifier. You cannot select Double Down.*')

        # Permanent Random Weapon (Normal Odds)
        case 'Permanent Random Weapon':
            ordinals = ['first', 'second', 'third', 'fourth']
            embed = interactions.Embed(title='Permanent Random Weapon', color=_COLOR,
                                   description=f'The **{random.choice(ordinals)}** player on each team will roll a random weapon separately. They must use this weapon for the rest of the set, regardless of what other modifiers say.\n\n*This overrides all other modifiers.*')

        # Death (Normal Odds)
        case 'Death':
            embed = interactions.Embed(title='Death', color=_COLOR,
                                   description=f'Determine the player with the highest kill count on both teams. Those players will be eliminated from the round. This game will be played as a 3v3.')

        # Sacrificial Specials (Normal Odds)
        case 'Sacrificial Specials':
            embed = interactions.Embed(title='Sacrificial Specials', color=_COLOR,
                                   description=f'If a player uses a special during this game, they must jump off the map after the user’s role in using said special is complete.')

        # Randomized Gear (Normal Odds)
        case 'Randomized Gear':
            embed = interactions.Embed(title='Randomized Gear', color=_COLOR,
                                   description=f'The main abilities of your gear must match:\nHeadgear - __**{randomHeadgearAbility()}**__\nClothing - __**{randomClothingAbility()}**\n__Shoes - __**{randomShoesAbility()}**__')

        # Besties (Normal Odds)
        case 'Besties':
            embed = interactions.Embed(title='Besties', color=_COLOR,
                                   description=f'Every player on your team must wear the same gear pieces. There are no restrictions on gear abilities.')

        # Killer Wail Kerfuffle (Normal Odds)
        case 'Killer Wail Kerfuffle':
            embed = interactions.Embed(title='Killer Wail Kerfuffle', color=_COLOR,
                                   description=f'All players must use either the vanilla Splattershot Nova or vanilla Inkbrush. This game will be played on Eeltail Alley Tower Control.')

        # Secret Agents (Normal Odds)
        case 'Secret Agents':
            embed = interactions.Embed(title='Secret Agents', color=_COLOR,
                                   description=f'Every player must select an Undercover Brella. This game will be played on Wahoo World Splat Zones.')

        # Bubble Bath (Normal Odds)
        case 'Bubble Bath':
            embed = interactions.Embed(title='Bubble Bath', color=_COLOR,
                                   description=f'Every player must select vanilla Bloblobber, except for one player on each team who may select Bloblobber Deco. This game will be played on Inkblot Art Academy Rainmaker.')

        # Double Down (Boosted Odds)
        case 'Double Down':
            embed = doubledown_function()

        # One For All (Normal Odds)
        case 'One For All':
            embed = interactions.Embed(title='One For All', color=_COLOR,
                                       description=f'Each player on each team selects the following gear item for their team based on their lobby position. All players on the team must use the same gear. You may use any gear ability you like.')
            gear_slot = ['Weapon', 'Headgear', 'Clothing', 'Shoes']
            teams = ['Alpha', 'Bravo']
            for team_name in teams:
                msg = '\n'.join(gear_slot)
                embed.add_field(name=f'Team {team_name}:', value=msg, inline=True)

        # Indicates that something has gone wrong
        case _:
            embed = interactions.Embed(title='ERROR: INVALID ROLL', color=_COLOR_ERROR,
                                   description=f'Something has gone wrong. Please try again. If the error persists, ping a TO.')

    embed.set_author(name='DOUBLE DOWN' if mod == 'Double Down' else 'THE WHEEL HAS SPOKEN')
    embed.set_footer(text='')
    return embed


def doubledown_function():
    mod1, mod2 = '',''
    # Defines the groups that double down may select from
    groupA = ['Randomized Weapons', 'Same Random Weapon', 'Two Random Weapons', 'Random Weapon Mirror', 'Same Random Sub', 'Same Random Special', 'Same Random Weapon Class', 'Enemy Comp Swap', 'Team Comp Swap', 'One For All']
    groupB = ['Turf War', 'Trade a Player', 'Deathmatch', 'Rubberband Map Pick', 'Death', 'Permanent Random Weapon', 'Besties', 'Sacrificial Specials', 'Randomized Gear']
    groupC = ['Same Random Weapon (DD)', 'Same Random Sub (DD)', 'Same Random Special (DD)', 'Same Random Weapon Class (DD)']

    # Sets a 20% chance of group C being selected
    chance = random.randint(1, 5)

    if chance > 1:
        mod1 = random.choice(groupA)
        mod2 = random.choice(groupB)
    else:
        mod1 = random.choice(groupC)
        mod2 = mod1

    embed = interactions.Embed(title='Double Down', color=_COLOR, description='')

    # Checks if mod selection is in group C
    if mod1 != mod2:
        # If mod selection is not in group C, process both mods
        embed.add_field(name=mod1, value=getattr(modifier_function(mod1), 'description'))
        embed.add_field(name=mod2, value=getattr(modifier_function(mod2), 'description'))

    else:
        embed.add_field(name=mod1, value=getattr(modifier_function(mod1), 'description'))
    return embed


# RANDOM FUNCTIONS

def randomModifier():
    # Creates list containing the game modifier_pool
    modifier_pool = [
    'Randomized Weapons', 'Randomized Weapons',
    'Same Random Weapon', 'Same Random Weapon',
    'Two Random Weapons', 'Two Random Weapons',
    'Random Weapon Mirror', 'Random Weapon Mirror',
    'Same Random Sub', 'Same Random Sub',
    'Same Random Special', 'Same Random Special',
    'Same Random Weapon Class', 'Same Random Weapon Class',
    'Enemy Comp Swap', 'Team Comp Swap',
    'Force at Gunpoint',
    'Turf War',
    'Trade a Player',
    'Deathmatch',
    'Rubberband Map Pick',
    'Rubberband Modifier Pick',
    'Permanent Random Weapon',
    'Death',
    'Sacrificial Specials',
    'Randomized Gear',
    'Besties',
    'Killer Wail Kerfuffle',
    'Secret Agents',
    'Bubble Bath',
    'Double Down', 'Double Down',
    'One For All'
    ]
    return random.choice(modifier_pool)


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
              'Z+F Splat Charger', 'Z+F Splatterscope', 'Zink Mini Splatling',
              'Douser Dualies FF', 'Recycled Brella 24 Mk I', '.52 Gal Deco', 'Custom E-liter 4K', 'Custom E-liter 4K Scope', 
              'Custom Explosher', 'Dread Wringer D', 'Foil Flingza Roller', 'Glooga Dualies Deco', 'Nautilus 79', 'New Squiffer']
    return random.choice(weapon)


def randomSub():
    subs = ['Splat Bomb', 'Suction Bomb', 'Burst Bomb', 'Curling Bomb', 'Autobomb', 'Ink Mine', 'Toxic Mist',
            'Point Sensor', 'Splash Wall', 'Sprinkler', 'Squid Beakon', 'Fizzy Bomb', 'Torpedo', 'Angle Shooter']
    return random.choice(subs)


def randomSpecial():
    specials = ['Inkjet', 'Ink Storm', 'Booyah Bomb', 'Ultra Stamp', 'Trizooka', 'Big Bubbler', 'Zipcaster',
                'Wavebreaker', 'Ink Vac', 'Killer Wail 5.1', 'Crab Tank', 'Reefslider', 'Tacticooler',
                'Triple Inkstrike', 'Kraken Royale', #'Splattercolor Screen',
                'Triple Splashdown']
    return random.choice(specials)


def randomClass():
    classes = ['Shooter', 'Roller', 'Charger', 'Dualies', 'Brella', 'Splatling', 'Blaster', 'Brush', 'Stringer',
               'Splatana']
    return random.choice(classes)


def randomHeadgearAbility():
    headgearAbility = ['Ink Saver (Main)', 'Ink Saver (Sub)', 'Ink Recovery Up', 'Run Speed Up', 'Swim Speed Up',
                       'Special Charge Up', 'Special Saver', 'Special Power Up', 'Quick Respawn', 'Quick Super Jump',
                       'Sub Power Up', 'Ink Resistance Up', 'Sub Resistance Up', 'Intensify Action', 'Opening Gambit',
                       'Last-Ditch Effort', 'Tenacity', 'Comeback']
    return random.choice(headgearAbility)


def randomClothingAbility():
    clothingAbility = ['Ink Saver (Main)', 'Ink Saver (Sub)', 'Ink Recovery Up', 'Run Speed Up', 'Swim Speed Up',
                       'Special Charge Up', 'Special Saver', 'Special Power Up', 'Quick Respawn', 'Quick Super Jump',
                       'Sub Power Up', 'Ink Resistance Up', 'Sub Resistance Up', 'Intensify Action', 'Ninja Squid',
                       'Haunt', 'Thermal Ink', 'Respawn Punisher']
    return random.choice(clothingAbility)


def randomShoesAbility():
    shoesAbility = ['Ink Saver (Main)', 'Ink Saver (Sub)', 'Ink Recovery Up', 'Run Speed Up', 'Swim Speed Up',
                    'Special Charge Up', 'Special Saver', 'Special Power Up', 'Quick Respawn', 'Quick Super Jump',
                    'Sub Power Up', 'Ink Resistance Up', 'Sub Resistance Up', 'Intensify Action', 'Stealth Jump',
                    'Object Shredder', 'Drop Roller']
    return random.choice(shoesAbility)


# Ensures that the bot boots properly
bot.start()
