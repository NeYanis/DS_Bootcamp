import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        path = sys.argv[1]
        lines = input(path)
        converted = convert(lines)
        write_to_csv(converted)

        

def input(path):
    with open(rf'{path}', 'r', encoding='utf-8') as output:
        return output.readlines() 

def write_to_csv(data):
    with open('employees.tsv', 'w', encoding='utf-8') as output:
        output.write('Имя\tФамилия\tE-mail\n')
        for line in data:
            output.write(f"{line[0].capitalize()}\t{line[1].capitalize()}\t{line[2]}\n")

def convert(lines):
    data = []
    for line in lines:
        if '@corp.com' in line:
            name_line = line.split('@')[0]
            try:
                name, surname = name_line.split('.')
                data.append((name.capitalize(), surname.capitalize(), f'{name}.{surname}@corp.com'))
            except ValueError:
                print(f'Error email {line}')
        else:
            print(f'Error email {line}')
    return data

     
if __name__ == '__main__':
    main()