import keyboard
import time

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
operacoes = ['+', '-', '*', '/']
print('programa iniciado')

while True:

    n1 = ''
    n2 = ''
    n1f = 0
    n2f = 0
    flag_r1 = False
    flag_r2 = False
    op_flag = False
    cont_flag = False
    res = 0
    op = ''
    read = ''
    error = 0
    max_size = 0
    i = 0

    while True:

        if keyboard.read_key() == '<':
            flag_r1 = True
            flag_r2 = True

        if flag_r1 or flag_r2:
            read = keyboard.read_key()
            flag_r1 = True

        if read in numeros and flag_r1 and op_flag == False:
            n1 += read

        if read in operacoes and flag_r1:
            flag_r1 = False
            flag_r2 = True
            op_flag = True
            op = read

        if flag_r2 and op_flag:
            if read in numeros and flag_r2:
                n2 += read

        if read == '>':
            flag_r1 = False
            flag_r2 = False
            op_flag = False
            cont_flag = True
            time.sleep(0.1)

        if cont_flag:

            try:
                n1f = float(n1)
                n2f = float(n2)
            except:
                error += 1

            if op == '+':
                res = n1f + n2f

            elif op == '-':
                res = n1f - n2f

            elif op == '/':
                res = n1f / n2f

            elif op == '*':
                res = n1f * n2f

            max_size = len(n1) + len(n2) + 3

            for i in range(max_size):
                keyboard.press('backspace')
                time.sleep(0.0001)

            keyboard.write(str(res))
            break


