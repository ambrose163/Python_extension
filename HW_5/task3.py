"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


def quit():
    return "Выходим из банкомата"


def add_money(summ_add, count_add, summ):
    if summ_add % 50 == 0:
        summ += summ_add
        count_add += 1
        if count_add % 3 == 0:
            summ *= 1.03
        operations_list.append("+" + str(summ_add))
    else:
        print("Введена некорректная сумма (не кратна 50)")
    return summ


def out_summ(summ_out, count_out, summ):
    comission = summ_out * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600

    if summ_out + comission > summ:
        print("Недостаточно средств")

    else:
        if summ_out % 50 == 0:
            summ -= summ_out + comission

            count_out += 1
            if count_out % 3 == 0:
                summ *= 1.03
            operations_list.append("-" + str(summ_out))
        else:
            print("Введена некорректная сумма")
    return summ


summ = 0
count_add = 0
count_out = 0
operations_list = []

while True:

    if summ > 5_000_000:
        print("С вас сняли налог на богатство", summ * 0.1)
        summ -= summ * 0.1

    action = input("\nДействие: ")

    if action == "q":
        print(quit())
        print(f"Сумма: {summ}\nСписок операций: {operations_list}")
        break
    elif action == "a":
        summ = add_money(int(input("Сумма пополнения: ")), count_add, summ)
    elif action == "o":
        summ = out_summ(int(input("Сумма снятия: ")), count_out, summ)

    print(f"Сумма: {summ}\nСписок операций: {operations_list}")