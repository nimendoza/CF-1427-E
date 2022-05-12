def solve(n: int) -> list[str]:
    output = list()

    def sum(a: int, b: int) -> int:
        output.append('{} + {}'.format(a, b))
        return a + b

    def xor(a: int, b: int) -> int:
        output.append('{} ^ {}'.format(a, b))
        return a ^ b

    if (n // 2) % 2 == 1:
        n = xor(n, sum(n, n)) 

    m = n
    for i in range(n.bit_length() - 1):
        m = sum(m, m)
    m = xor(xor(n, m), sum(n, m))
    
    while not (n == 1 or m == 1):
        if n > m:
            n, m = m, n
        min = n
        for i in range(m.bit_length() - n.bit_length()):
            n = sum(n, n)
        m = xor(n, m)
        n = min

    return output

def main(path: str) -> None:
    with open(path, 'r') as file:
        n = int(file.readline().strip())
    
    output = solve(n)
    with open(path, 'a') as file:
        file.write('{}\n'.format(len(output)))
        for line in output:
            file.write('{}\n'.format(line))
            