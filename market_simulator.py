import random

pizza = 100
sauce = 40
dough = 60
n = 100
i = 0
cap = 10000
t = 0

def p_change():
    if pizza < 100:
        return 1 * random.randint(0, 10)
    if pizza > 200:
        return -1 * random.randint(0, 10)
    if random.random() < 0.5:
        return 1 * random.randint(0, 10)
    else:
        return -1 * random.randint(0, 10)


def s_change():
    if sauce > 100:
        return -1 * random.randint(0, 10)
    if sauce < 50:
        return 1 * random.randint(0, 10)
    if random.random() < 0.5:
        return 1 * random.randint(0, 10)
    else:
        return -1 * random.randint(0, 10)


def d_change():
    if dough > 100:
        return -1 * random.randint(0, 10)
    if dough < 50:
        return 1 * random.randint(0, 10)
    if random.random() < 0.5:
        return 1 * random.randint(0, 10)
    else:
        return -1 * random.randint(0, 10)


while i < n:
    pizza += 2 * p_change()
    sauce += s_change()
    dough += d_change()
    print(f"Pizza price: {pizza} \tSauce price: {sauce} \tDough price: {dough} \tCap:{cap}")
    if pizza > sauce + dough:
        cost = sauce + dough
        buy_num = cap // cost
        if buy_num >= 100: #limit
            buy_num = 100
        cap = cap - buy_num * cost + pizza * buy_num
        print(f"trade executed, {buy_num} pizza sold")
        t += 1
    print()
    i += 1

print(f"final return is {cap/100}" + f"%, {t} trades executed")