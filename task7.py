''' Вводится массив целых чисел. Найти самую длинную подпоследовательностей
подряд идущих элементов массива, которые в сумме дают 0 (реализовать функцию,
которая будет возвращать позицию первого элемента такой подпоследовательности и
кол-во элементов). В случае нескольких таких подпоследовательностей найти вторую
слева (от начала массива). В случае, если таких подпоследовательностей не существует,
функция должна возвращать в качестве первого элемента подпоследовательности -1.
'''


def find_longest_zero_sum_subsequence(arr):
    if not arr:
        return (-1, 0)
    max_length = 0
    start_position = -1
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            # Если сумма равна 0 и длина больше текущей максимальной
            if current_sum == 0 and (j - i + 1) > max_length:
                max_length = j - i + 1
                start_position = i

    if max_length > 0:
        return (start_position, max_length)
    else:
        return (-1, 0)


if __name__ == "__main__":
    arr1 = [1, 2, -3, 4, 5, -9, 3, 1, -1]
    result1 = find_longest_zero_sum_subsequence(arr1)
    print(f"Массив: {arr1}")
    print(f"Результат: позиция={result1[0]}, длина={result1[1]}")
    if result1[0] != -1:
        subsequence = arr1[result1[0]:result1[0] + result1[1]]
        print(f"Подпоследовательность: {subsequence}, сумма={sum(subsequence)}")
    print()


