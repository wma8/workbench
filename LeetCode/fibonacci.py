container = [0, 0, 1]


def fibonacci(n):
    if n is 0:
        return 0
    if n is 1:
        return 1
    
    for i in range(1, n):
        container[0] = container[1]
        container[1] = container[2]
        container[2] = container[0] + container[1]
    return container[2]

if __name__ == '__main__':
    print(fibonacci(10))
