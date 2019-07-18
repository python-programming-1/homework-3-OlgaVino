print("Enter number:")

num = int(input())


def collatz(num_input):
    if num_input % 2 == 0:
        result = num_input // 2
        print(result)

    elif num_input % 2 == 1:
        result = 3 * num_input + 1
        print(result)
    else:
        print("Please type a valid number")
    return result


while num != 1:
    num = collatz(num)
