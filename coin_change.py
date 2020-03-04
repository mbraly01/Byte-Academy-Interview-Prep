#NAPSACK PROBLEM
def coin_change(number, array, count = 1):
    if len(array) > 1:
        for i in range(0,(number//array[0])):
            count = coin_change(number-(i * array[0]), array[1:], count)
    else:
        if number % array[0] == 0:
            return count + 1
    return count

print(coin_change(100,[2,5,25]))