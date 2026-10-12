"""簡單統計工具（沙盒用）。"""


def mean(xs):
    xs = list(xs)
    if not xs:
        raise ValueError("mean() 不接受空序列")
    return sum(xs) / len(xs)


def median(xs):
    xs = sorted(xs)
    if not xs:
        raise ValueError("median() 不接受空序列")
    mid = len(xs) // 2
    if len(xs) % 2:
        return xs[mid]
    return (xs[mid - 1] + xs[mid]) / 2
