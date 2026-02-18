import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    parser.add_argument('name', help='Имя') 
    parser.add_argument('-s', '--surname', help='Фамилия')    
    args = parser.parse_args()
    parts = [] 
    parts.append(f'Hello, {args.name}')
    if args.surname is not None:
        parts.append(args.surname)
    print(*parts)
