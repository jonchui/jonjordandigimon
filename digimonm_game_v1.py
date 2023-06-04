class Digimon:
    def __init__(self, name, hp, attack, special, special_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack
        self.special = special
        self.special_power = special_power
        self.special_used = False

    def attack(self, opponent_digimon):
        print(f'{self.name} attacks {opponent_digimon.name}!')
        opponent_digimon.take_damage(self.attack_power)

    def take_damage(self, attack_power):
        self.hp -= attack_power  
        print(f'{self.name} is left with {self.hp} hp.')

    def is_defeated(self):
        return self.hp <= 0

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def play_card(self, opponent):
        my_digimon = self.deck[0] 
        print(f'{self.name} plays {my_digimon.name} who has {my_digimon.hp} hp, {my_digimon.attack_power} attack power.')

        opponent_digimon = opponent.deck[0] 
        print(f'{opponent.name}\'s Digimon is {opponent_digimon.name} who has {opponent_digimon.hp} hp, {opponent_digimon.attack_power} attack power.')

        my_digimon.attack(opponent_digimon)

        if opponent_digimon.is_defeated():
            print(f'{opponent_digimon.name} is defeated!')
            opponent.deck.remove(opponent_digimon)
            return 1 
        else:
            opponent_digimon.attack(my_digimon)
            if my_digimon.is_defeated():
                print(f'{my_digimon.name} is defeated!')
                self.deck.remove(my_digimon)
                return -1 
        return 0 

deck1 = [Digimon('Trainmon', 50, 20, 'Special Power', 'On the first turn with this player, you negate attacks to this Digimon.') for _ in range(10)]
deck2 = [Digimon('Dynamon', 60, 25, 'Special Power', 'Revive once with half HP after defeated.') for _ in range(10)]

player1 = Player('Player 1', deck1)
player2 = Player('Player 2', deck2)

score = {player1.name: 0, player2.name: 0}

while deck1 and deck2: 
    score[player1.name] += player1.play_card(player2)
    if deck2:  # Ensure deck2 still has cards after Player1's turn
        score[player2.name] += player2.play_card(player1)

print(f'Final score is {player1.name}: {score[player1.name]}, {player2.name}: {score[player2.name]}')
