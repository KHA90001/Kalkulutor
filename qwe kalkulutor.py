q = input()
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
        print(w  // e)
    if q == '/':
        w = int(input())
        e = int(input())
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
