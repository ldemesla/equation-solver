import sys
import math

def valid_sign(sign):
    valid_signs = ['+', '*', '-', '=', ' ', '^', '.', 'X']
    valid = False
    for i in range(len(valid_signs)):
        if(sign == valid_signs[i]):
            valid = True
            break
    if (valid == False and sign.isdigit()):
        valid = True
    return valid

def parse_equation(eq):
    last = None
    equal = None
    polynomial = 0
    last_p = False
    last_s = True
    for i in range(len(eq)):
        if (valid_sign(eq[i]) == False):
            return False
        elif ((last == 'X' and eq[i] == ' ') or (eq[i] == 'X' and len(eq) == i + 1)):
            polynomial = 1
        elif (last and last.isdigit() and last_s and eq[i].isdigit()):
            return False
        elif (last == '^' and eq[i].isdigit() == False):
            return False
        elif (last and last.isdigit() and eq[i] == 'X') or (last == 'X' and eq[i].isdigit()):
            return False
        elif ((last_s and last_p == True) or (last == 'X')) and eq[i] == '*':
            return False
        elif (last_s and last_p == True):
            last_p = False
        elif (last_p == True and eq[i] != ' '):
            return False
        elif (last == '^'):
            last_p = True
            if (int(eq[i]) > polynomial):
                polynomial = int(eq[i])
        elif (last != None and eq[i] != ' ' and last.isdigit() == False and last != 'X' and eq[i].isdigit() == False and eq[i] != 'X' and last != '='):
            return False
        if (eq[i] == '='):
            if (equal == None and last != None):
                equal = True
            else:
                return False
        if (eq[i] != ' '):
            last = eq[i]
            last_s = False
        else:
            last_s = True
    if (equal == None or last == '=' or (last.isdigit() == False and last != 'X')):
        return False
    return polynomial

def equation_to_array(eq_str):
    eq = []
    q = str()
    after_equal = False
    last_was_egal = False
    for i in range(len(eq_str)):
        if ((i == 0 or last_was_egal) and eq_str[i] != ' '):
            if eq_str[i] == '-':
                q = '-'
            elif eq_str[i] == '+':
                q = '+'
            else:
                q = '+' + eq_str[i]
            last_was_egal = False
        elif (eq_str[i] == '+' or eq_str[i] == '-'):
            if after_equal and last_was_egal == False:
                if q[0] == '-':
                    q = '+' + q[1:]
                else:
                    q = '-' + q[1:]
            if i != 0 and last_was_egal == False:
                eq.append(q)
                q = eq_str[i]
        elif eq_str[i] == '=':
                after_equal = True
                last_was_egal = True
                eq.append(q)
        elif (eq_str[i] != ' ' and eq_str[i]):
                q += eq_str[i]
    if after_equal and last_was_egal == False:
        if q[0] == '-':
            q = '+' + q[1:]
        else:
            q = '-' + q[1:]
    eq.append(q)
    return eq

def str_int_float(s):
    if s.is_integer():
        return str(int(s))
    else:
        return str(s)

def remove_x(s):
    new_str = str()
    i = 0
    x = False
    while i < len(s):
        if (s[i] == 'X'):
            x = True
        elif x == True:
            if (s[i] == ' ' or s[i] == '*'):
                x = False
        elif s[i] != '*':
            new_str += s[i]
        i += 1
    if (len(new_str) == 1):
        new_str += '1'
    return new_str

def sort_polynomial(eq):
    j = 0
    new_eq = []
    for i in range(len(eq)):
        if(eq[i].find('X') == -1):
            if len(new_eq) > j:
                s = float(eq[i]) + float(new_eq[j])
                del new_eq[j]
            else:
                s = float(eq[i])
            new_eq.append(str_int_float(s))
    for i in range(len(eq)):
        index = eq[i].find('X')
        if index != -1 and len(eq[i]) > index + 2 and eq[i][index + 2] == '0':
            if len(new_eq) > j:
                s = float(remove_x(eq[i])) + float(new_eq[j])
                del new_eq[j]
            else:
                s = float(remove_x(eq[i]))
            if (s > 0):
                new_eq.append('+' + str_int_float(s))
            else:
                new_eq.append(str_int_float(s))
    j += 1
    if len(new_eq) != j:
        new_eq.append('0')
    for i in range(len(eq)):
        index = eq[i].find('X')
        if (index != -1 and (len(eq[i]) == index + 1 or eq[i][index + 1] != '^')):
            if len(new_eq) > j:
                s = float(remove_x(eq[i])) + float(new_eq[j])
                del new_eq[j]
            else:
                s = float(remove_x(eq[i]))
                if (s > 0):
                    new_eq.append('+' + str_int_float(s))
                else:
                    new_eq.append(str_int_float(s))
    for i in range(len(eq)):
        index = eq[i].find('X')
        if index != -1 and len(eq[i]) > index + 2 and eq[i][index + 2] == '1':
            if len(new_eq) > j:
                s = float(remove_x(eq[i])) + float(new_eq[j])
                del new_eq[j]
            else:
                s = float(remove_x(eq[i]))
            if (s > 0):
                new_eq.append('+' + str_int_float(s))
            else:
                new_eq.append(str_int_float(s))
    j += 1
    if len(new_eq) != j:
        new_eq.append('0')
    for i in range(len(eq)):
        index = eq[i].find('X')
        if index != -1 and len(eq[i]) > index + 2 and eq[i][index + 2] == '2':
            if len(new_eq) > j:
                s = float(remove_x(eq[i])) + float(new_eq[j])
                del new_eq[j]
            else:
                s = float(remove_x(eq[i]))
            if (s > 0):
                new_eq.append('+' + str_int_float(s))
            else:
                new_eq.append(str_int_float(s))
    return new_eq

def solve_fdegre_eq(eq):
    print('polynomial degree: 1')
    res = float(eq[0]) / float(eq[1])
    print('the solution is: {}'.format(res * -1))

def print_reduced_form(eq):
    x = ['X', 'X^2']
    print('reduced form : ', end='')
    for i in range(len(eq)):
        if i == 0 and eq[i][0] == '-':
            print('-', end='')
        elif eq[i][0] == '-' and i != 0:
            print(' - ', end='')
        elif i != 0:
            print(' + ', end='')
        if (len(eq[i]) != 2 or eq[i][1] != '1' or i == 0):
            print(eq[i][1:], end='')
            if i != 0:
                print(' * ', end='')
        if i != 0:
            print('{}'.format(x[i - 1]), end='')
    print(' = 0')

def solve_sdegre_eq(eq):
    print('polynomial degree: 2')
    d = (float(eq[1])       ** 2) - (4*float(eq[2])*float(eq[0]))
    if (d > 0):
        a = (-float(eq[1]) + math.sqrt(d)) / (2 * float(eq[2]))
        b = (-float(eq[1]) - math.sqrt(d)) / (2 * float(eq[2]))
        print('discriminant is stricly positive, the two solutions are:')
        print(a)
        print(b)
    elif (d == 0):
        print('discriminant is equal to 0, the only solution is:')
        print((-float(eq[1])) / (2 * float(eq[2])))
    else:
        print('discriminant is stricly negative, there is two complexe solutions:')
        if (float(eq[1]) != 0):
            print('{} - '.format(-1 * float(eq[1])), end='')
        else:
            print('-', end='')
        print('i√{} / {}'.format(str(-d), str((2*float(eq[2])))))
        if (float(eq[1]) != 0):
            print('{} + '.format(-1 * float(eq[1])), end='')
        print('i√{} / {}'.format(str(-d), str((2*float(eq[2])))))

def main(argv):
    if (len(argv) == 2):
        degre = parse_equation(argv[1])
        if degre is False:
            print('error: incorrect equation')
            return
        else:
            if (degre > 2):
                print('error: this program only solve polynomial with a coefficient inferior to 3')
                return
            else:
                eq = equation_to_array(argv[1])
                eq = sort_polynomial(eq)
                all_real = True
                for i in range(len(eq)):
                    if (eq[i] != '0'):
                        all_real = False
                if (all_real == True):
                    print('There is an infinite number of solutions')
                    return
                elif degre == 0:
                    print('There is no solutions to this equation')
                else:
                    print_reduced_form(eq)
                    if degre == 1:
                        solve_fdegre_eq(eq)
                    else:
                        solve_sdegre_eq(eq)
    else:
        print("Wrong number of arguments")

if __name__ == "__main__":
    main(sys.argv)
