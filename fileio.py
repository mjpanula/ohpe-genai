with open('large_example.txt', 'r') as file:    
    for line in file:
        print(line, end='')
        line_count += 1