import numpy as np
import matplotlib.pyplot as plt

# 1. СОЗДАНИЕ ГИСТОГРАММЫ СЛУЧАЙНЫХ ДАННЫХ

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

# Добавление заголовков и меток осей
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Показать график
plt.show()

# 2. СОЗДАНИЕ ДИАГРАММЫ РАССЕЯНИЯ

# Генерация двух массивов из 5 случайных чисел
x = np.random.rand(5)
y = np.random.rand(5)

# Вывод массивов для проверки
print("Массив x:", x)
print("Массив y:", y)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()