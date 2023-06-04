import random
from colorama import Fore, Style

class Card:
    def __init__(self, name, hp, attack, special, special_ability):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.special = special
        self.special_ability = special_ability

    def attack_opponent(self, opponent_card):
        opponent_card.hp -= self.attack

    def is_alive(self):
        return self.hp > 0

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.deck = create_deck(digimon_list)

    def play_card(self, opponent):
        card = self.deck.pop(0)
        print(f"{self.color}{self.name} plays {card.name} who has {card.hp} hp, {card.attack} attack power.{Style.RESET_ALL}")
        card.attack_opponent(opponent.deck[0])
        if not opponent.deck[0].is_alive():
            print(f"{self.color}{opponent.name}'s {opponent.deck[0].name} is defeated!{Style.RESET_ALL}")
            opponent.deck.pop(0)
            return 1
        return 0

def create_deck(digimon_list):
    return random.sample(digimon_list, 10)

# Define the list of all Digimon cards
digimon_list = [
    Card('Trainmon', 50, 20, 40, 'Negate attacks on the first turn.'),
    Card('Dinomon', 60, 30, 50, 'Double attack power on the first turn.'),
    Card('Beamon', 70, 25, 45, 'Heals 20 HP after each turn.'),
    Card('Platimon', 75, 35, 40, 'Increases defense by 20 after each attack.'),
    Card('Tigermon', 80, 50, 50, 'Does a counter attack with half damage.'),
    Card('Shellmon', 90, 25, 60, 'Blocks the first attack.'),
    Card('Flymon', 65, 35, 45, 'Dodges every third attack.'),
    Card('Blademon', 70, 60, 30, 'Can attack twice every third turn.'),
    Card('Stonemon', 100, 40, 50, 'Reduces received damage by 20.'),
    Card('WindyMon', 60, 40, 70, 'Increases attack power by 15 after each successful attack.'),
    Card('Sparkmon', 55, 70, 35, 'Paralyzes opponent every fifth turn.'),
    Card('BunnyMon', 70, 30, 45, 'Heals 10 HP every turn.'),
    Card('Flowermon', 60, 40, 50, 'Reduces opponent\'s attack by 15 every fourth turn.'),
    Card('Cloudmon', 70, 50, 40, 'Doubles HP once when HP drops below 20.'),
    Card('Spheremon', 75, 55, 50, 'Reflects half of received damage back to the opponent.'),
    Card('Knightmon', 80, 65, 45, 'Blocks every second attack.'),
    Card('MirrorMon', 60, 60, 60, 'Mirrors opponent\'s attack once every game.'),
    Card('Shadowmon', 65, 70, 55, 'Becomes invulnerable every fifth turn.')
]

player1 = Player("Player 1", Fore.RED)
player2 = Player("Player 2", Fore.GREEN)

# Play until someone runs out of cards
while player1.deck and player2.deck:
    player1_score = player1.play_card(player2)
    player2_score = 0
    if player2.deck:  # If Player 2 still has cards left
        player2_score = player2.play_card(player1)
    print(f"{Fore.CYAN}Score after this round: Player 1 - {player1_score}, Player 2 - {player2_score}{Style.RESET_ALL}\n")
