password = input('Введите пароль: ')

try:
    l = 1/len(password)
    l = int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except:
    print('Требования к паролю соблюдены')
