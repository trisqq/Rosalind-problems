def merge_sorted(arr1: list[int], arr2: list[int]) -> list[int]:
    """Объединяет два отсортированных списка в один общий с помощью двух указателей.

    Args:
        arr1: первый отсортированный список.
        arr2: второй отсортированный список.

    Returns:
        Объединённый отсортированный список.
    """
    merged: list[int] = []
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)

    while i < len1 and j < len2:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Запись оставшихся элементов из незавершённого списка
    while i < len1:
        merged.append(arr1[i])
        i += 1

    while j < len2:
        merged.append(arr2[j])
        j += 1

    return merged


def main() -> None:
    """Читает два массива из Arrays.txt, сливает их и печатает результат.
    """
    with open("Arrays.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Пропускаем чтение размеров, забирая сразу строки с массивами
    a = list(map(int, lines[1].split()))
    b = list(map(int, lines[3].split()))

    result = merge_sorted(a, b)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
