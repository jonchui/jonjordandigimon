# The Digimon class
## direct access: https://chat.openai.com/c/c066b581-22c7-4347-b529-bd5db9a7ad2b
class Digimon:
    def __init__(self, name, hp, attack, special, special_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack
        self.special = special
        self.special_power = special_power
        self.special_used = False

    def attack(self, opponent_digimon):
        print(f'{self.name} attacks {opponent_digimon.name}!')
        opponent_digimon.take_damage(self.attack_power)

    def take_damage(self, attack_power):
        self.hp -= attack_power  # When a Digimon takes damage, we reduce its hp
        print(f'{self.name} is left with {self.hp} hp.')

    def can_use_special(self):
        return not self.special_used  # A Digimon can use its special power if it has not been used yet


# The Player class
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck  # The deck of Digimon cards

    def play_card(self, opponent):
        my_digimon = self.deck.pop(0)  # The player plays a Digimon card
        print(f'{self.name} plays {my_digimon.name} who has {my_digimon.hp} hp, {my_digimon.attack_power} attack power.')

        opponent_digimon = opponent.deck.pop(0)  # The opponent's Digimon is revealed
        print(f'{opponent.name}\'s Digimon is {opponent_digimon.name} who has {opponent_digimon.hp} hp, {opponent_digimon.attack_power} attack power.')

        # The player's Digimon attacks the opponent's Digimon
        my_digimon.attack(opponent_digimon)

        # Check if the opponent's Digimon is defeated
        if opponent_digimon.hp <= 0:
            print(f'{opponent_digimon.name} is defeated!')
            return 1  # This player gets a point
        else:
            # The opponent's Digimon counterattacks
            opponent_digimon.attack(my_digimon)
            if my_digimon.hp <= 0:
                print(f'{my_digimon.name} is defeated!')
                return -1  # The opponent gets a point
        return 0  # No points if both Digimons survive


# The Digimon cards
deck1 = [Digimon('Trainmon', 50, 20, 40, 'Negate attacks on first turn.') for _ in range(10)]
deck2 = [Digimon('Dynamon', 60, 25, 50, 'Revive once with half HP after defeated.') for _ in range(10)]

# The players
player1 = Player('Player 1', deck1)
player2 = Player('Player 2', deck2)

# The score
score = {player1.name: 0, player2.name: 0}

# Each player plays one card per turn until they run out
for _ in range(10):
    score[player1.name] += player1.play_card(player2)
    score[player2.name] += player2.play_card(player1)

    # Print the score after each round
    print(f'The score is now {player1.name}: {score[player1.name]}, {player2.name}: {score[player2.name



