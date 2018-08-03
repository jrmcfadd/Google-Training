import random


class Robot:

    def __init__(self, name, say_hello, give_name, dance, slogan):
        self.name = name
        self.tricks = {'say_hello': say_hello, 'give_name': give_name, 'dance': dance, 'slogan': slogan}

    def evolve(self, trick_name, trick):
        self.tricks.update({trick_name : trick})

    def introduceSelf(self):
        print(self.tricks['say_hello'])

    def insults(self):
        insult = self.tricks['insult'][random.randint(0,4)]
        print(insult)

    def get_tricks(self):
        print(self.tricks)


bot1 = Robot('Negan','Are we pissin our pants yet?','Hi... I\'m Negan...', '*Cracks you over the head with Lucille :)*', 'Little Pig, Little Pig!!! Let! Me! In!' )
bot2 = Robot('Rick','Rick... Rick Grimes...And you?','Howdy... I\'m Rick...', '*Does the Hokie Pokie*', 'Caaaaaarrrllll!' )

bot1.introduceSelf()
bot1.evolve('insult', 'Idiot...')

print(bot1.tricks)