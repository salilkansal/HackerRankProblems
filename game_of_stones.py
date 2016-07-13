# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_test_cases = input()


def pick_stone(num_of_stones, last_player):
    if num_of_stones < 2:
        return last_player
    if num_of_stones == 2:
        return pick_stone(num_of_stones - 2, change_player(last_player))
    if 3 <= num_of_stones < 5 or num_of_stones == 10:
        return pick_stone(num_of_stones - 3, change_player(last_player))
    return pick_stone(num_of_stones - 5, change_player(last_player))


def change_player(last_player):
    if last_player == 'First':
        return 'Second'
    else:
        return 'First'


for case_no in range(num_of_test_cases):
    stones = input()
    print '{0}) {1}', format(case_no + 1, pick_stone(stones, 'Second'))
