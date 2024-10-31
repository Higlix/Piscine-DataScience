def ft_tqdm(lst: range) -> None:
    """
    A simplified tqdm-like progress bar implemented as a generator function.

    Args:
    - lst (range): The range over which to iterate.

    Yields:
    - str: Progress bar representation for each iteration.
    """
    total = len(lst)
    scale = 50
    bar = ""
    for i in range(total + 1):
        progress = i / total
        percentage = int(progress * 100)

        bar = f"{percentage}%|{'█' * int(progress * scale)}\
            {' ' * (scale - int(progress * scale))}| {i}/{total}"
        print(f"{bar}\r", end='', flush=True)
        yield i
