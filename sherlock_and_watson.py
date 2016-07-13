# Enter your code here. Read input from STDIN. Print output to STDOUT
def shift(seq, n):
    n %= len(seq)
    return array[-n:] + array[:-n]

n, k, q = map(int, raw_input().split())
array = map(int, raw_input().split())
array = shift(array, k)
for _ in range(q):
    print array[int(input())]