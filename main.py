def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = list(map(int, input().split()))
    return numbers

def insertOne(numbers, value):
    """
    ########################################
    Code Your Program here
    Do not use 'sort' keyword
    ########################################
    """
    index = 0
    while index < len(numbers) and numbers[index] < value:
        index += 1
    numbers.insert(index, value)


def main():
    numbers = getInput()    # test input: 10 15 25 30 35
    value = 20
    insertOne(numbers, value)   # insert value 20
    print(numbers)         # list value after insertion


if __name__ == '__main__':
    main()
