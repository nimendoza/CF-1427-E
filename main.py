import solve
import check

if __name__ == '__main__':
    summary_path = 'output\\summary.txt'

    file_template = 'output\\test case {}.txt'
    for i in range(3, 999999 + 1, 2):
        t = str(i).rjust(6, '0')
        filepath = file_template.format(t)

        with open(filepath, 'w') as file:
            file.write('{}\n'.format(i))
        
        solve.main(filepath)

        check.main(filepath, summary_path)

        print(t)