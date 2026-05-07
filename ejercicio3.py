def nokia(n):
    vecinos = {
        0: [0, 8], 1: [1, 2, 4], 2: [1, 2, 3, 5],
        3: [2, 3, 6], 4: [1, 4, 5, 7], 5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9], 7: [4, 7, 8],
        8: [5, 7, 8, 9, 0], 9: [6, 8, 9]
    }

    dp = [[0] * (n + 1) for _ in range(10)]

    for d in range(10):
        dp[d][1] = 1

    print("\nTabla inicial:")
    print(dp)

    for k in range(2, n + 1):
        print(f"\nCalculando longitud {k}:")
        for d in range(10):
            dp[d][k] = sum(dp[v][k - 1] for v in vecinos[d])
            print(f"DP[{d}][{k}] = {dp[d][k]}")

    total = sum(dp[d][n] for d in range(10))
    print("\nTotal:", total)
    return total

print('Ejemplo 1:\n')
nokia(2)
print('Ejemplo 2:\n')
nokia(3)
print('Ejemplo 3:\n')
nokia(4)