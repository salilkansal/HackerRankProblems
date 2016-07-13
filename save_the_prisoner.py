# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = input()


def get_last_sweet(num_of_prisoners, num_of_sweets, prisoner_id):
    for x in range(num_of_sweets):
        prisoner_id = get_next_prisoner(num_of_prisoners, prisoner_id)
    return num_of_prisoners if prisoner_id == 1 else prisoner_id - 1


def get_next_prisoner(num_of_prisoners, curr_prisoner):
    return (curr_prisoner + 1) % num_of_prisoners


for case in range(0, test_cases):
    list = map(int, raw_input("Input").split())
    num_of_prisoners = list[0]
    num_of_sweets = list[1]
    prisoner_id = list[2]
    print list
    print get_last_sweet(num_of_prisoners, num_of_sweets, prisoner_id)
