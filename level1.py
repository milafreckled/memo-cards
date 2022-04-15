def level1(N):
    result = ''
    # N = int(input('How many lines?'))
    for i in range(N):
        line = input('Next line: ')  
        if 'start' in line:
            # idx = line.find('start ')
            line = line[len('start '):]
        if 'end' in line:
            idx = line.find(' end')
            line = line[:idx] 
        splitted_line = line.split('print')
        for word in splitted_line:
            word = word.strip()
        result += ('').join(splitted_line)
    return result

if __name__ == '__main__':
    N = int(input('How many lines?'))
    print(level1(N))