import random

player_score = 0
computer_score = 0

print("---test version: War: 10 points race ---")

for i in range(10):
    if player_score < 10 and computer_score < 10:
        input("Press enter to continue...")

    print(f"---Round {i+1}---")

    suit_p = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_p = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    suit_c = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_c = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    print("your card is:", card_p, suit_p)
    print("computer card is:", card_c, suit_c)

    if card_p == 'A' : p_val = 14
    elif card_p == 'K' : p_val = 13
    elif card_p == 'Q' : p_val = 12
    elif card_p == 'J' : p_val = 11
    else: p_val = card_p

    if card_c == 'A' : c_val = 14
    elif card_c == 'K' : c_val = 13
    elif card_c == 'Q' : c_val = 12
    elif card_c == 'J' : c_val = 11
    else: c_val = card_c

    if p_val > c_val:
        player_score += 1
    elif c_val > p_val:
        computer_score += 1

    print(f"Score: Player score {player_score} | Computer score: {computer_score}")

print("test finished")
print("note: the loop stops always at round 10")


