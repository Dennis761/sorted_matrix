your_matrix = [[8, 2, 3, 7, 2],
               [6, 0, 8, 2, 11],
               [11, 15, 16, 10, 15],
               [1, 6, 3, 8, 5],
               [10, 5, 8, 9, 1]]

def average(row):
    return sum(row) / len(row)

sorted_matrix = sorted(your_matrix, key=average)

print(sorted_matrix)

#1. За допомогою функції average ми находимо середнє значення кожного рядка
#2. За допомогою функції sorted ми сортуємо масив your_matrix за середнім значенням кожного рядка,
# і створюємо нову змінну sorted_matrix куди і присвоюємо відсортований масив
#3. Виводим відсортований масив за допомогою функції print