def dominant_probability(k: int, m: int, n: int) -> float:
    """Считает вероятность доминантного фенотипа через обратное событие.

    Args:
        k: количество гомозиготных доминантных (AA).
        m: количество гетерозиготных (Aa).
        n: количество гомозиготных рецессивных (aa).

    Returns:
        Вероятность появления потомка с доминантным фенотипом.
    """
    total = k + m + n
    total_pairs = total * (total - 1)

    # Варианты, дающие рецессивное потомство (aa):
    # 1) пара aa x aa (всегда даёт aa)
    ways_nn = n * (n - 1) * 1.0

    # 2) пары Aa x aa и aa x Aa (дают aa с вероятностью 50%)
    ways_mn = (m * n + n * m) * 0.5

    # 3) пара Aa x Aa (даёт aa с вероятностью 25%)
    ways_mm = m * (m - 1) * 0.25

    prob_recessive = (ways_nn + ways_mn + ways_mm) / total_pairs
    return 1.0 - prob_recessive


def main() -> None:
    """Читает k, m, n из Mendels_law.txt и печатает вероятность с 5 знаками.
    """
    with open("Mendels_law.txt", "r") as f:
        k, m, n = map(int, f.read().split())

    ans = dominant_probability(k, m, n)
    print(f"{ans:.5f}")


if __name__ == "__main__":
    main()
