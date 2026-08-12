import os
from datetime import date


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command must be 'mv src dst'")
    _, src, dst = parts

    # If dst ends with /, use src's basename inside that directory
    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    # Create parent directories step-by-step with os.mkdir()
    parent = os.path.dirname(dst)
    if parent:
        parts_path = parent.split("/")
        current = ""
        for part in parts_path:
            current = os.path.join(current, part) if current else part
            if not os.path.exists(current):
                os.mkdir(current)

    # Copy file content then remove source (as specified)
    with open(src, "r") as f:
        content = f.read()
    with open(dst, "w") as f:
        f.write(content)
    os.remove(src)


def unlucky_days(year: int) -> int:
    return sum(
        1 for m in range(1, 13)
        if date(year, m, 13).weekday() == 4  # Friday
    )


def isomorphic_strings(first_string: str, second_string: str) -> bool:
    if len(first_string) != len(second_string):
        return False
    f2s, s2f = {}, {}
    for char_a, char_b in zip(first_string, second_string):
        if char_a in f2s and f2s[char_a] != char_b:
            return False
        if char_b in s2f and s2f[char_b] != char_a:
            return False
        f2s[char_a] = char_b
        s2f[char_b] = char_a
    return True
