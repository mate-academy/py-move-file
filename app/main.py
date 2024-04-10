import os


def move_file(command: str) -> bool:
    c_args = command.split()
    if command == "" or c_args[0] != "mv" or c_args[1] == c_args[2]:
        return False
    file1, file2 = c_args[1], c_args[2]
    if "/" in c_args[2]:
        splitter = []
        path = c_args[2]
        for num in range(len(path) - 1):
            if path[num] == "/":
                splitter.append(num)
                print(path[:num])
                if not os.path.isdir(path[:num]):
                    os.mkdir(path[:num])
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(c_args[1])
