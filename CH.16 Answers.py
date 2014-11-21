__author__ = 'Dark-Knight'


class Employee():
    pass


class Invalidsocial(ValueError):
    pass

ssn = 'please enter your social security in the format ###-##-####:'




def social(employee_class):
    try:
        aaa, gg, ssss = input(employee_class.ss).split('-')
    except ValueError:
        raise Invalidsocial
    if aaa == '078'and gg == '05' and ssss == '1120':
        raise Invalidsocial
    if len(aaa) != 3:
        raise Invalidsocial
    if len(gg) != 2:
        raise Invalidsocial
    if len(ssss) != 4:
        raise Invalidsocial
    try:
        aaa = int(aaa)
        gg = int(gg)
        ssss = int(ssss)
    except ValueError:
        raise Invalidsocial
    if str(aaa) == '000':
        raise Invalidsocial
    elif 900 <= int(aaa) <= 999:
        raise Invalidsocial
    elif int(aaa) == 666:
        raise Invalidsocial
    if str(gg) == '00':
            raise Invalidsocial

    elif str(ssss) == '0000':
        raise Invalidsocial
    else:
        return aaa, gg, ssss

def socnum():
    instance1 = Employee()
    instance1.sn = 'please enter your social security in the format ###-##-####:'
    try:
        social(instance1.sn)
    except Invalidsocial:
        socnum()


socnum()







