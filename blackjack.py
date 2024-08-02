import random
from art import logo
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    global CARDS
    return random.choice(CARDS)


def calculate_score(cards):
    """Calculates the score of a blackjack hand."""
    total = sum(cards)
    # Check for blackjack immediately
    if total == 21 and len(cards) == 2:
        return 0  # Blackjack!
    # Adjust for aces if necessary
    if 11 in cards and total > 21:
        total -= 10
    return total


def compare(user_score, computer_score):
    """Compares scores in a Blackjack game and returns the outcome."""

    if user_score > 21:
        return "You went over. You lose :("  # Handle user bust first
    if computer_score > 21:
        return "Opponent went over. You win 😁" # Then handle computer bust
    if user_score == computer_score:
        return "Draw"
    # Blackjack checks after bust checks
    if computer_score == 0:
        return "Lose, opponent has Blackjack"
    if user_score == 0:
        return "Win with a Blackjack"

    # Determine the winner based on remaining scenarios
    return "You win 😃" if user_score > computer_score else "You lose 😤"


def play_game():
    os.system('clear')
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = 0
        computer_score = 0
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}. current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type Y to get another card, type N to pass:")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()
