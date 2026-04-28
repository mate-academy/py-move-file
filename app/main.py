import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3:
        return

    src = parts[1]
    dst = parts[2]

    if dst.endswith("/"):
        dst_dir = dst
        dst_path = os.path.join(dst, os.path.basename(src))
    else:
        dst_dir = os.path.dirname(dst)
        dst_path = dst

    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)

    shutil.copy2(src, dst_path)
    os.remove(src)


with open("file.txt", "w") as file:
    file.write("Some\nText")

print(f"Original content: {open('file.txt').read}")

move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")

print(f"Moved content: "
      f"{open('first_dir/second_dir/third_dir/file2.txt').read()}")

try:
    open("file.txt")
except FileNotFoundError:
    print("Source file successfully removed.")
