'''
import random


MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PER_QUICK_PICK = 6


define main():
    get num_quick_picks
    quick_picks = generate_all_quick_picks(num_quick_picks)
    print_formatted_result(quick_picks)


define print_formatted_result(quick_picks):
    for quick_pick in quick_picks:
        formatted_quick_pick = " ".join("{:2}".format(number) for number in quick_pick)
        print(formatted_quick_pick)


def generate_quick_pick():
    all_numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))
    quick_pick = []

    while len(quick_pick) < NUM_PER_QUICK_PICK:
        number = random.choice(all_numbers)
        all_numbers.remove(number)
        quick_pick.append(number)

    return sorted(quick_pick)


def generate_all_quick_picks(num_picks):
    return [generate_quick_pick() for i in range(num_picks)]


main()

'''
import random


MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PER_QUICK_PICK = 6


def main():
    num_quick_picks = int(input("How many quick picks?"))
    quick_picks = generate_all_quick_picks(num_quick_picks)
    print_result(quick_picks)


def print_result(quick_picks):
    for quick_pick in quick_picks:
        formatted_quick_pick = " ".join(["{:2}".format(number) for number in quick_pick])
        print(formatted_quick_pick)


def generate_quick_pick():
    all_numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))
    quick_pick = []

    while len(quick_pick) < NUM_PER_QUICK_PICK:
        number = random.choice(all_numbers)
        all_numbers.remove(number)
        quick_pick.append(number)

    return sorted(quick_pick)


def generate_all_quick_picks(num_picks):
    return [generate_quick_pick() for i in range(num_picks)]


main()
