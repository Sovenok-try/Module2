import time


# Объявляем переменные для хранения слайдов
slide1 = '(^_^)'
slide2 = '(^_~)'
slide3 = '(^_^)'
slide4 = '(o_O)'
slide5 = '(O_O)'
slide6 = 'Hello, World!'

# Ждем 1 секунду перед выводом нового слайда
time.sleep(1)
# Выводим слайд и оставляем каретку на той же строке
print(slide1, end='\r')
# Повторяем аналогичное действие для остальных слайдов

# time.sleep(1)
# print(slide2, end='\r')
# time.sleep(1)
# print(slide3, end='\r')
# time.sleep(1)
# print(slide4, end='\r')
# time.sleep(1)
# print(slide5, end='\r')
# time.sleep(1)
# print(slide6, end='\r')
