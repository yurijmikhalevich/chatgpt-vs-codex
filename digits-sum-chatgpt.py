def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def interesting_numbers(n):
    count = 0
    for i in range(1, n+1):
        if sum_of_digits(i+1) < sum_of_digits(i):
            count += 1
    return count

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(interesting_numbers(n))

