def cal(v):
    for i in range(1, 18):
        v[i] = 9 * i * 10**(i - 1)


def solve():
    v = [0] * 18
    cal(v)

    query = 1
    query = int(input())
    
    for _ in range(query):
        k = int(input())
        
        sum_val = 0
        length_of_number = 0
        for i in range(18):
            sum_val += v[i]
            if sum_val <= k:
                length_of_number = i + 1
            else:
                break

        sum_val -= v[length_of_number]
        difference = k - sum_val
        starting_number = 10**(length_of_number - 1)
        distance_from_starting_number = difference // length_of_number
        actual_number = starting_number + distance_from_starting_number - 1
        remainder = difference % length_of_number

        if remainder == 0:
            print(actual_number % 10)
        else:
            actual_number += 1
            remainder = length_of_number - remainder
            for _ in range(remainder):
                actual_number //= 10
            print(actual_number % 10)


if __name__ == "__main__":
    solve()
