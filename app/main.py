import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "mv": #Check if it is a command format
        source_file, new_file = split_command[1:]
        if "/" in new_file: #checkig if it is a path
            if new_file[-1] == "/":
                new_file += source_file
            path_list = new_file.split("/")
            full_path = path_list[0]
            for i in range(len(path_list) - 1):
                try:
                    os.mkdir(full_path)
                except FileExistsError:
                    continue
                finally:
                    full_path = os.path.join(full_path, path_list[i + 1])
            try:
                with (open(source_file, "r") as file_in,
                      open(full_path, "w") as file_out):
                    file_out.write(file_in.read())
                os.remove(source_file)
            except FileNotFoundError:
                pass
        else:
            os.rename(source_file, new_file)





# file_r = open("file.txt", "w")
# # file_r.write("Hello!\nI am John")
# # print(open("file.txt").read())
# move_file("mv file.txt first_dir/second_dir/third_dir/")
# # print(open("first_dir/second_dir/third_dir/file2.txt").read())