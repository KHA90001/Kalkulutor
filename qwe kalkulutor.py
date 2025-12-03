q = input()
r = 0
while ('НЕТ' or 'НЕт' or 'Нет' or 'нЕТ' or 'нЕт' or 'неТ' or 'НеТ' or 'нет' or 'Not' or 'Not' or 'NOt' or 'NoT' or 'nOt' or 'nOT' or 'noT') not in q:
    if q == '-':
        w = int(input())
        e = int(input())
        print(w - e)
    if q == '+':
        w = int(input())
        e = int(input())
        print(w + e)
    if q == '*':
        w = int(input())
        e = int(input())
        print(w * e)
    if q == '//':
        w = int(input())
        e = int(input())
        if e == 0:
            r += 1
            if '.' not in str(r / 2):
                print('Мистер Пропер запрещяет делить на ноль, а также вытирать пыль влажными руками')
            else:
                print('омашние тапочки запрещают делить на ноль и ходить в уличной обуви дома ')
        else:
            print(w  // e)
    if q == '/':
        w = int(input())
        e = int(input())
        if
        print(w / e)
    if q == '%':
        w = int(input())
        e = int(input())
        print(w % e)
    if q == '**':
        w = int(input())
        e = int(input())
        print(w ** e)
    q = input()
print('Досвидания')
