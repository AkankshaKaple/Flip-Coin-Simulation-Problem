import random


class FlipCoinSimulator:
    def flip_coin(self):
        if random.randrange(0, 2) == 0:
            side = "T"
        else:
            side = "H"
        return side


print("Welcome to Flip coin simulator")
fc = FlipCoinSimulator()
output_side = fc.flip_coin()
print(output_side)



