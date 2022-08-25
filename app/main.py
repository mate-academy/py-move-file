import os


def move_file(command):
    list_command = command.split()
    if len(list_command) == 3:
        os.renames(list_command[1], list_command[2])
    else:
        del list_command[0:2]
        temp_str = list_command[0]
        list_command = temp_str.split("/")
        del list_command[-1]
        for i in range(len(list_command)):
            os.mkdir("/".join(list_command[:i + 1]))
        temp_str_2 = "/".join(list_command[:])
        temp_command_end = command.split("/")
        with open(f"{list_command[1]}", "r") as file_in, \
                open(f"{temp_str_2}/{temp_command_end[-1]}", "w") as file_out:
            file_out.write(f"{file_in.read()}")
            os.remove(f"{list_command[1]}")
