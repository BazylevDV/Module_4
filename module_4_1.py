from fake_math import divide as fake_divide#импорт функций из др модулей с одновременным переименованием
from true_math import divide as true_divide

result1 = fake_divide(699, 3)# Запуск функций с аргументами
result2 = fake_divide(33, 0)
result3 = true_divide(329, 7)
result4 = true_divide(119, 0)


print(result1)# Вывод результатов на экран
print(result2)
print(result3)
print(result4)
