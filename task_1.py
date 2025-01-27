import heapq

# Функція для мінімізації витрат на з'єднання кабелів
def min_connection_cost(cables):
    # Перетворюємо список у мінімальну купу
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо найменший кабель
        first = heapq.heappop(cables)
        # Витягуємо другий найменший кабель
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        # Додаємо новий кабель у купу
        heapq.heappush(cables, cost)

    return total_cost

# Функція для об'єднання k відсортованих списків
def merge_k_lists(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        for num in lst:
            heapq.heappush(min_heap, num)
    
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))
    
    return result

# Тестування об'єднання кабелів
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_connection_cost(cables))

# Тестування об'єднання відсортованих списків
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
