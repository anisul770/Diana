def readfile(file):
    try:
        with open(file, 'r') as infile:
            for i in range(4):
                line = infile.readline().strip()
            code_list = []
            while line != '':
                line = list(line)
                code_list.append(line)
                line = infile.readline().strip()
            return code_list
    except IOError:
        print(f'{file} does not exist')
        exit()


def hidden_code(code_list):
    binary_code = []
    k = 0
    l = 0
    for i in range(0, len(code_list)):
        for j in range(k, len(code_list[i]), 2):
            k = j
            if code_list[i][k] == ':':
                k -= 2
                l = 1
                break
            else:
                if l == 1 and code_list[i][k+2] == ':':
                    binary_code.append(0)
                    l = 0
                elif l == 1 and code_list[i][k+2] != ':':
                    binary_code.append(0)
                    l = 0
                else:
                    binary_code.append(1)
    return binary_code


if __name__ == '__main__':
    code_list = readfile('AncientMessage.txt')
    binary_code = hidden_code(code_list)
    for i in range(len(binary_code)):
        binary_code[i] = str(binary_code[i])
    s = ''.join(binary_code)
    with open('One.txt','w') as infile:
        for i in range(len(binary_code)//8):
            infile.write(chr(int(s[i*8:i*8+8], 2)))
            print(s[i*8:i*8+8], end=' ')
            print(int(s[i*8:i*8+8], 2), end=' ')
            print(chr(int(s[i*5:i*5+5], 2)))
