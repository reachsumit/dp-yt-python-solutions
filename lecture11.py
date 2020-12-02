def fib(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def topDown(n, memo):
    # Solve top first (not exactly; but close) and then go down
    if n == 0 or n <= 2:
        return 1
    elif n in memo:
        return memo[n]

    memo[n] = topDown(n-1, memo) + topDown(n-2, memo)
    return memo[n]


def forward(n):
    # first find i-1 and i-2 in order to find i
    memo = {}
    memo[0], memo[1] = 0, 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


def bottomUp(n):
    # Opposite of forward; first find i and i-1 in order to find i-2
    memo = [0] * (n+2)
    memo[0], memo[1] = 0, 1

    for i in range(1, n):
        memo[i+1] += memo[i]
        memo[i+2] += memo[i]

    return memo[n]


print(fib(7))
print(topDown(170, {}))
print(forward(7))
print(bottomUp(16))
