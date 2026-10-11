def fibonacci(a: int):
    fib_list = [0] * a
    fib_list[0] = 1
    fib_list[1] = 1
    result = 0
    for i in range(2, a): 
        result += fib_list[i - 1] + fib_list[i - 2]

    return result
