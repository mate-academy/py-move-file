import os


def move_file(command: str) -> None:
    content = command.split()
    if len(content) < 3:
        return "Not enough params"
    mv, old_path, new_path = content
    if mv != "mv" or old_path == new_path:
        return
    directories = new_path.split("/")[:-1]
    os.makedirs("/".join(directories), exist_ok=True)
    # for i in range(len(directories)):
    #     if not os.path.exists("/".join(directories[:i+1])):
    #
    with open(old_path, "r") as f1, open(new_path, "w") as f2:
        f2.write(f1.read())
    os.remove(old_path)


if __name__ == '__main__':
    move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")