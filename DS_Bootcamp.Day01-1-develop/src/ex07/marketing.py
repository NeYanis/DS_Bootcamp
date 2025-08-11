import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        data(sys.argv[1])
        
def data(line):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if line == "call_center":
        print(call_center(clients, recipients))
    elif line == "potential_clients":
        print(potential_clients(participants, clients))
    elif line == "loyalty_program":
        print(loyalty_program(clients, participants))
    else:
        raise ValueError("Invalid task name")

def call_center(clients, recipients):
    return list(set(clients) - set(recipients))

def potential_clients(participants, clients):
    return list(set(participants) - set(clients))

def loyalty_program(clients, participants):
    return list(set(clients) - set(participants))

if __name__ == '__main__':
    main()