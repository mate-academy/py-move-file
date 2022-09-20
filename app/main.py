import os


def move_file(values: str):
    values = values.split()
    path_ = values[2].split("/")
    with open(values[1], "r") as file_in:
        content = file_in.read()
    os.remove(values[1])

    path_1 = ""
    for i in path_:
        if i == path_[-1]:
            path_1 += os.path.join(i)
        path_1 += os.path.join(i + "/")
        os.mkdir(path_1)

    with open(values[2], "w") as file_out:
        file_out.write(content)


move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
