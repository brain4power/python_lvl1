# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    if int(number * 10**(ndigits+1)) % 10 >= 5:
        return (int(number * 10**ndigits) + 1) / (10**ndigits)
    else:
        return int(number * 10**ndigits) / 10**ndigits


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    first_sum = int(ticket_number_str[0]) + int(ticket_number_str[1]) + int(ticket_number_str[2])
    second_sum = int(ticket_number_str[3]) + int(ticket_number_str[4]) + int(ticket_number_str[5])
    if first_sum == second_sum:
        return "lucky"
    else:
        return 'Unlucky'


print(lucky_ticket(123006))
print(lucky_ticket(123212))
print(lucky_ticket(436751))
