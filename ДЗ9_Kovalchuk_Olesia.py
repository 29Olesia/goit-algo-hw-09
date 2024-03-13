import time  

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        num_coins = amount // coin
        if num_coins > 0:
            change[coin] = num_coins
            amount -= num_coins * coin
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    change = {}
    i = amount
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                if coin in change:
                    change[coin] += 1
                else:
                    change[coin] = 1
                i -= coin
                break
    return change

amount = 113


start_time_greedy = time.time()  
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time_greedy 
print("Результат жадібного алгоритму:", greedy_result)
print("Час виконання жадібного алгоритму:", greedy_time)


start_time_dynamic = time.time()  
dynamic_result = find_min_coins(amount)
dynamic_time = time.time() - start_time_dynamic  
print("Результат алгоритму динамічного програмування:", dynamic_result)
print("Час виконання алгоритму динамічного програмування:", dynamic_time)
