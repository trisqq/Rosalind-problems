def find_majority(arr: list[int], n: int) -> int:
    """Определяет элемент, встречающийся строго чаще n / 2 раз.

    Args:
        arr: массив целых чисел.
        n: длина массива.

    Returns:
        Мажоритарный элемент или -1, если такого нет.
    """
    counts: dict[int, int] = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    threshold = n // 2
    for num, count in counts.items():
        if count > threshold:
            return num

    return -1


def main() -> None:
    """Читает k массивов из Elements.txt и печатает по элементу для каждого.
    """
    with open("Elements.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    k, n = map(int, lines[0].split())
    results: list[str] = []

    for i in range(1, k + 1):
        arr = list(map(int, lines[i].split()))
        majority_element = find_majority(arr, n)
        results.append(str(majority_element))

    print(" ".join(results))


if __name__ == "__main__":
    main()
