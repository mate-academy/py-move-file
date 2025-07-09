import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if parts[0] != "mv" or len(parts) != 3:
        raise ValueError("Invalid command format")

    src = parts[1]
    dst = parts[2]

    # Якщо шлях закінчується на слеш — це директорія
    if dst.endswith("/"):
        os.makedirs(dst, exist_ok=True)
        dst = os.path.join(dst, os.path.basename(src))
    else:
        # Якщо в шляху є проміжні директорії — створити їх
        dir_path = os.path.dirname(dst)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    shutil.move(src, dst)
