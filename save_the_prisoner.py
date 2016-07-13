# Enter your code here. Read input from STDIN. Print output to STDOUT


def get_last_sweet(num_of_prisoners, num_of_sweets, prisoner_id):
    num_of_sweets %= num_of_prisoners
    prisoner_id = (prisoner_id + num_of_sweets - 1) % num_of_prisoners
    return num_of_prisoners if prisoner_id == 0 else prisoner_id


for case in range(input()):
    n, s, p = map(int, raw_input().split())
    print get_last_sweet(n, s, p)
