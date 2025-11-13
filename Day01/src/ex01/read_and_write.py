def read():
    with open('ds.csv', 'r',encoding='utf-8') as output:
        return output.readlines()
def replace(lines):
    result=[]
    flag = True
    for line in lines:
        new_line=[]
        for let in line:
            if (let =='"'):
                flag=not flag
                new_line.append(let)
            elif (flag and let==',' or let==';'):
                new_line.append('\t')
            else:
                new_line.append(let)
        result.append(''.join(new_line))
    return result
def write(lines):
    with open('ds.tsv','w',encoding='utf-8') as output:
        output.writelines(lines)
def main():
    lines = read()
    replaced_lines = replace(lines)
    write(replaced_lines)
                
if __name__ == '__main__':
    main()
