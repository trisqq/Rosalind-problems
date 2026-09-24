def read_graph(file_path: str) -> tuple[int, list[list[int]]]:
    """Считывает количество вершин и строит список смежности.

    Args:
        file_path: путь к файлу, первая строка — n и m, далее m рёбер.

    Returns:
        Кортеж (n, adj), где adj — список смежности.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()

    n, m = map(int, lines[0].split())
    adj: list[list[int]] = [[] for _ in range(n + 1)]

    for line in lines[1 : m + 1]:
        if not line.strip():
            continue
        u, v = map(int, line.split())
        adj[u].append(v)
        adj[v].append(u)

    return n, adj


def compute_double_degrees(n: int, adj: list[list[int]]) -> list[int]:
    """Для каждой вершины суммирует количество рёбер у её соседей.

    Args:
        n: количество вершин.
        adj: список смежности.

    Returns:
        Список из n значений double-degree.
    """
    results: list[int] = []
    for i in range(1, n + 1):
        neighbor_sum = 0
        for neighbor in adj[i]:
            neighbor_sum += len(adj[neighbor])
        results.append(neighbor_sum)
    return results


def main() -> None:
    """Читает граф из double_degree.txt и печатает double-degree всех вершин через пробел.
    """
    n, adj = read_graph("double_degree.txt")
    ddeg_list = compute_double_degrees(n, adj)
    print(" ".join(map(str, ddeg_list)))


if __name__ == "__main__":
    main()
