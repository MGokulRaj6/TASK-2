def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    if amount != 0:
        print("Change cannot be made with the given denominations.")
        return {}
    return result

coins = [25, 10, 5, 1]
amount = 63
change = greedy_coin_change(coins, amount)
print("Coin change:")
for coin, count in change.items():
    print(f"{coin}¢: {count}")
