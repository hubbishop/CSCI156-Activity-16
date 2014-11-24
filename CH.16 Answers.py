__author__ = 'Dark-Knight'


class Employee():
    pass


class Invalidsocial(ValueError):
    pass


def social(employee_class):
    try:
        aaa, gg, ssss = input('please enter your social security in the format ###-##-####:').split('-')
    except ValueError:
        raise Invalidsocial
    if aaa == '078' and gg == '05' and ssss == '1120':
        raise Invalidsocial
    if len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
        raise Invalidsocial
    if str(aaa) == '000' or str(gg) == '00' or str(ssss) == '0000':
        raise Invalidsocial
    try:
        aaa = int(aaa)
        gg = int(gg)
        ssss = int(ssss)
    except ValueError:
        raise Invalidsocial
    if 900 <= int(aaa) <= 999:
        raise Invalidsocial
    elif int(aaa) == 666:
        raise Invalidsocial
    else:
        employee_class.ss = aaa, gg, ssss


def socnum(employee_class):
    try:
        social(employee_class)
    except Invalidsocial:
        socnum(employee_class)

employee1 = Employee()
socnum(employee1)
print(employee1.ss)