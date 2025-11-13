def create_dict():
    list_of_tuples = [
            ('Russia', '25'),
            ('France', '132'),
            ('Germany', '132'),
            ('Spain', '178'),
            ('Italy', '162'),
            ('Portugal', '17'),
            ('Finland', '3'),
            ('Hungary', '2'),
            ('The Netherlands', '28'),
            ('The USA', '610'),
            ('The United Kingdom', '95'),
            ('China', '83'),
            ('Iran', '76'),
            ('Turkey', '65'),
            ('Belgium', '34'),
            ('Canada', '28'),
            ('Switzerland', '26'),
            ('Brazil', '25'),
            ('Austria', '14'),
            ('Israel', '12')
            ]

    result = {}
    for t in list_of_tuples:
        result[t[0]] = int(t[1])
    return result

def sort(inp):
    sorted_list = sorted(inp.keys(), key=lambda x: (-inp[x], x))
    return sorted_list

def print_list(result):
    for country in result:
        print(country)

def main():
    dict = create_dict()
    s_list = sort(dict)
    print_list(s_list)
    
if __name__ == '__main__':
    main()