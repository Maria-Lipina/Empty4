from prime_test import prime

def factors(num: int):
    """Определяет простые множители числа и их количество
    Принимает: целое число num
    Возвращает: словарь, в котором ключ - простой множитель, значение по ключу - количество повторений данного множителя в числе num 
    """

    res = {}
    while num > 1:
        if prime.test(num):
            res |= {num: 1}
            return res
        else:
            divide = 2
            while num > 1:
                if not (num % divide):
                    if divide in res: 
                        res[divide] += 1
                        num = num // divide
                    else: 
                        res |= {divide: 1}
                        num = num // divide
                else: divide +=1
    return res