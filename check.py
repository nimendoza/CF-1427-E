def check(n: int, input: list[tuple[int, str, int]]) -> tuple[list[str], bool]:
    valid = True

    nums = set()
    nums.add(n)
    for line in input:
        a, operation, b = line
        if a not in nums or b not in nums:
            valid = False
            break
        else:
            if operation == '^':
                nums.add(a ^ b)
            else:
                nums.add(a + b)
    
    lines = list()
    lines.append(
        'Result: {}'.format(
            'CORRECT'
                if 1 in nums and valid
                else 'INCORRECT'
        )
    )

    return lines, (1 in nums and valid)

def main(path: str, summary_path: str) -> None:
    with open(path, 'r') as file:
        n = int(file.readline().strip())
        m = int(file.readline().strip())
        input = list()
        for i in range(m):
            a, operation, b = file.readline().split()
            input.append(
                (int(a), operation, int(b))
            )
    
    output, correct = check(n, input)
    with open(path, 'a') as file:
        for line in output:
            file.write('{}\n'.format(line))

    with open(summary_path, 'a') as file:
        file.write('{}: {}\n'.format(
            str(n).rjust(6, '0'),
            'CORRECT'
                if correct
                else 'INCORRECT'
        ))