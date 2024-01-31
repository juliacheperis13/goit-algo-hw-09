import timeit

from dynamic import find_min_coins
from greedy import find_coins_greedy


def benchmark(func, sum_, coin_):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(sum, coin)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'sum': sum_, 'coin': coin_}, number=10)


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    sum = 113
    
    # print(find_coins_greedy(sum, coins))
    print(find_min_coins(sum, coins))

    # results = []
    # for sum in [113, 2049, 10490]:
    #     time = benchmark(find_min_coins, sum, coins)
    #     results.append((find_min_coins.__name__, sum, time))
    #     time = benchmark(find_coins_greedy, sum, coins)
    #     results.append((find_coins_greedy.__name__, sum, time))

    #     title = f"{'Алгоритм':<30} | {'Сума':<30} | {'Час виконання, сек'}"

    #     print(" " * len(title))
    #     print(" " * len(title))
    #     print(title)
    #     print("-" * len(title))
    #     for result in results:
    #         print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
    #         print(" " * len(title))
