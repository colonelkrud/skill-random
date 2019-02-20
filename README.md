# opsdroid skill random

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to perform random events like flipping a coin or rolling a dice.

## Requirements

None.

## Configuration

None.

## Usage

#### `flip a coin`

Flips a coin.

> user: flip a coin
>
> opsdroid: It landed on heads

#### `roll a dice`

Rolls a dice.

> user: roll a dice
>
> opsdroid: You rolled a 4

#### `roll a(n) n sided dice`

Rolls a single dice of given sides and replies with the result.

>user: roll a 10 sided dice
>
>opsdroid: You rolled a 9


#### `roll x n sided dice`

Rolls a given number of dice of given sides and replies with the results.
Also gives some basic stats about the dice rolled.

>user: roll 5 10 sided dice
>
>opsdroid: You rolled the following: 4, 5, 4, 10, 3
>The average is 5 The mode is 4
>The minimum value was: 3 and the maximum value was: 10


#### `roll a dn`

Rolls a single dice of given sides and replies with the result.

>user: roll a d20
>
>opsdroid: You rolled a 9


#### `roll x dn`

Rolls a given number of dice of given sides and replies with the results.
Also gives some basic stats about the dice rolled.

>user: roll 5 d10
>
>opsdroid: You rolled the following: 4, 5, 4, 10, 3
>The average is 5 The mode is 4
>The minimum value was: 3 and the maximum value was: 10
