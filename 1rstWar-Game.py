import random

player_score = 0
computer_score = 0

print("--- WAR: 10 points race ---")
print("(Type 'S' to surrender at any time)")

while player_score < 10 and computer_score < 10:
    action = input("\nPress Enter to shuffle the cards: ")

    if action == 'S' or action == 's':
        print("white flag! surrendering :( ...")
        break

    suit_p = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_p = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    suit_c = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_c = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])

    print(f"You: {card_p}{suit_p}  vs  CPU: {card_c}{suit_c}")

    if card_p == 'A':
        p_val = 14
    elif card_p == 'K':
        p_val = 13
    elif card_p == 'Q':
        p_val = 12
    elif card_p == 'J':
        p_val = 11
    else:
        p_val = card_p

    if card_c == 'A':
        c_val = 14
    elif card_c == 'K':
        c_val = 13
    elif card_c == 'Q':
        c_val = 12
    elif card_c == 'J':
        c_val = 11
    else:
        c_val = card_c

    if p_val > c_val:
        player_score += 1
        print("Point for you!")
    elif c_val > p_val:
        computer_score += 1
        print("Point for computer!")
    else:
        print("Draw! No points.")

    print(f"Score: Player {player_score} | Computer {computer_score}")

if player_score >= 10:
    print("\n🏆 CONGRATULATIONS! You won the war!")
elif computer_score >= 10:
    print("\n💻 GAME OVER! The computer conquered the deck.")
else:
    print("\n🏳️ Game ended by surrender.")

