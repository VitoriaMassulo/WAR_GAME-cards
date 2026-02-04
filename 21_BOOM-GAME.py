import random

print("--- Welcome to 21 Boom! 🃏 ---")


p1_total = 0
print("--- FIRST PLAYER'S TURN ---")

for _ in range(2):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    if card == 'A': val = 1
    elif card == 'J' or card == 'Q' or card == 'K': val = 10
    else:
        val = card

    p1_total += val
    print("Your card is:", card, suit)

print("Total:", p1_total)

for _ in range(10):
    choice = input("0 = STOP, 1 = CONTINUE: ")
    if choice == '0':
        break

    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    if card == 'A': val = 1
    elif card == 'J' or card == 'Q' or card == 'K': val = 10
    else:
        val = card

    p1_total += val
    print("Your card is:", card, suit)
    print("Total:", p1_total)

    if p1_total >= 21:
        break

p2_total = 0
print("--- SECOND PLAYER'S TURN ---")
for _ in range(2):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    if card == 'A': val = 1
    elif card == 'J' or card == 'Q' or card == 'K': val = 10
    else:
        val = card

    p2_total += val
    print("Your card is:", card, suit)

print("Total:", p2_total)

for _ in range(10):
    choice = input("0 = STOP, 1 = CONTINUE: ")
    if choice == '0':
        break

    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    if card == 'A': val = 1
    elif card == 'J' or card == 'Q' or card == 'K': val = 10
    else:
        val = card

    p2_total += val
    print("Your card is:", card, suit)
    print("Total:", p2_total)

    if p2_total >= 21:
        break

print("--- FINAL SCORE ---")
print(f"P1: {p1_total} | P2: {p2_total}")

if p1_total > 21 and p2_total > 21:
    print("Both Disqualified!")
elif p1_total > 21:
    print("P2 Wins!")
elif p2_total > 21:
    print("P1 Wins!")
elif p1_total > p2_total:
    print("P1 Wins!")
elif p2_total > p1_total:
    print("P2 Wins!")
else:
    print("Draw!")
