from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
from statistics import mode, StatisticsError
import random
import itertools

DICE_ROLL_RESPONSES = [
    "The dice says {number}",
    "You rolled a {number}",
    "It's a {number}"
]


COIN_FLIP_RESPONSES = [
    "It landed on {result}",
    "You got {result}",
    "It's {result}"
]

MODE_EXISTS = """
    <p>You rolled the following: {list}</p>
    <p>The average is {average} The mode is {mode}</p>
    <p>The minimum value was: {min} and the maximum value was: {max}</p>
    """
MODE_DNE = """
    <p>You rolled the following: {list}</p>
    <p>The average is {average} There is no unique mode</p>
    <p>The minimum value was: {min} and the maximum value was: {max}</p>
    """

class RandomSkill(skill):
    @match_regex(r'roll a dice', case_sensitive=False)
    async def roll_a_dice(opsdroid, config, message):
        """
        Rolls a single dice and replies with the result.
        Usage: roll a dice
        """
        number = random.randint(1, 6)
        text = random.choice(DICE_ROLL_RESPONSES).format(number=number)
        await message.respond(text)


    @match_regex(r'roll a(n)? ([1-9][0-9]*) sided dice$', case_sensitive=False)
    async def roll_a_n_sided_dice(opsdroid, config, message):
        """
        Rolls a single dice of given sides and replies with the result.
        Usage: roll a(n) (#sides) sided dice
        """
        sides = int(message.regex.group(2))
        if sides == 2:
            result = random.choice(["heads", "tails"])
            text = random.choice(COIN_FLIP_RESPONSES).format(result=result)
            await message.respond(text)
        else:
            number = random.randint(1, sides)
            text = random.choice(DICE_ROLL_RESPONSES).format(number=number)
            await message.respond(text)


    @match_regex(r'roll ([1-9][0-9]*) ([1-9][0-9]*) sided dice$',
                case_sensitive=False)
    async def roll_many_dice(opsdroid, config, message):
        """
        Rolls a given number of dice of given sides and replies with the results.
        Also gives some basic stats about the dice rolled.
        Usage: roll (#dice) (#sides) sided dice
        """
        dice = int(message.regex.group(1))
        sides = int(message.regex.group(2))
        if sides == 2 and 1 <= dice <= 1024:
            await message.respond("You only get one.")
            result = random.choice(["heads", "tails"])
            text = random.choice(COIN_FLIP_RESPONSES).format(result=result)
            await message.respond(text)
        elif 1 <= dice <= 1024 and sides != 2:
            res = []
            for j in range(dice):
                res.append(random.randint(1, sides))
            average = round(sum(res) / len(res))
            minimum_roll = str(min(res))
            maximum_roll = str(max(res))
            rolls = str(res).strip('[]')
            try:
                unique_mode = str(mode(res))
                await message.respond(MODE_EXISTS.format(list=rolls,
                                    average=average, mode=unique_mode,
                                    min=minimum_roll, max=maximum_roll))
            except StatisticsError:
                await message.respond(MODE_DNE.format(list=rolls,
                                    average=average, min=minimum_roll,
                                    max=maximum_roll))
        else:
            await message.respond('Try between 1 and 1024 dice')


    @match_regex(r'roll a(n)? d([1-9][0-9]*)$', case_sensitive=False)
    async def roll_dx(opsdroid, config, message):
        """
        Rolls a dice of given sides and replies with the results.
        Usage: roll a(n) d(#sides)
        """
        sides = int(message.regex.group(2))
        if sides == 2:
            result = random.choice(["heads", "tails"])
            text = random.choice(COIN_FLIP_RESPONSES).format(result=result)
            await message.respond(text)
        else:
            number = random.randint(1, sides)
            text = random.choice(DICE_ROLL_RESPONSES).format(number=number)
            await message.respond(text)


    @match_regex(r'roll ([1-9][0-9]*) d([1-9][0-9]*)$', case_sensitive=False)
    async def roll_many_dx(opsdroid, config, message):
        """
        Rolls a given number of dice of given sides and replies with the results.
        Also gives some basic stats about the dice rolled.
        Usage: roll (#dice) d(#sides)
        """
        dice = int(message.regex.group(1))
        sides = int(message.regex.group(2))
        if sides == 2 and 1 <= dice <= 1024:
            await message.respond("You only get one.")
            result = random.choice(["heads", "tails"])
            text = random.choice(COIN_FLIP_RESPONSES).format(result=result)
            await message.respond(text)
        elif 1 <= dice <= 1024 and sides != 2:
            res = []
            for j in range(dice):
                res.append(random.randint(1, sides))
            average = round(sum(res) / len(res))
            minimum_roll = str(min(res))
            maximum_roll = str(max(res))
            rolls = str(res).strip('[]')
            try:
                unique_mode = str(mode(res))
                await message.respond(MODE_EXISTS.format(list=rolls,
                                    average=average, mode=unique_mode,
                                    min=minimum_roll, max=maximum_roll))
            except StatisticsError:
                await message.respond(MODE_DNE.format(list=rolls, average=average,
                                                    min=minimum_roll,
                                                    max=maximum_roll))
        else:
            await message.respond('Try between 1 and 1024 dice')


    @match_regex(r'flip a coin', case_sensitive=False)
    async def flip_a_coin(opsdroid, config, message):
        """
        Replies with heads or tails.
        Usage: flip a coin
        """
        result = random.choice(["heads", "tails"])
        text = random.choice(COIN_FLIP_RESPONSES).format(result=result)
        await message.respond(text)
