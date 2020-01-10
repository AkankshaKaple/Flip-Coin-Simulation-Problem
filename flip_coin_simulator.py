import random


def flip_coin():
    tail = []
    head = []
    for i in range(num_chances):
        if random.randrange(0, 2) == 0:
            tail.append("T")
        else:
            head.append("H")
    return {"tail": tail, "head": head}


print("Welcome to Flip coin simulator")
num_chances = 10
result = flip_coin()
print(result)
tail_percentage = (result['tail'].count("T") * num_chances) / 100
head_percentage = (result['head'].count("H") * num_chances) / 100
print("head_percentage = {} % {}tail_percentage = {} % ".format(head_percentage, '\n', tail_percentage))
