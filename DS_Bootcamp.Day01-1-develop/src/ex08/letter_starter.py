import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        mail = sys.argv[1]
        data = input()
        finder(mail, data)
        
def finder(mail, data):
    for line in data:
        parts = line.strip().split('\t')
        if parts[2] == mail:
            print(f"Dear {parts[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
            return
    print('Email not found')

def input():
    with open('employees.tsv', 'r', encoding='utf-8') as output:
        return output.readlines() 

if __name__ == '__main__':
    main()