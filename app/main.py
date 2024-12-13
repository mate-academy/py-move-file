import os


def move_file(command: str):
    """
    example:
    move_file("mv test.txt tests1/tests2/test1.txt")
    move_file("mv test.txt tests1/tests2/")
    """
    parse_list_parameters = command.split(" ")
    if len(parse_list_parameters) != 3:
        raise Exception("Invalid command string. "
                        "Expected: mv path_from path_to")
    if parse_list_parameters[1] == parse_list_parameters[2]:
        raise Exception("Invalid command string. "
                        "path_from and path_to have same names")
    list_path_from = parse_list_parameters[1].split("/")
    list_path_to = parse_list_parameters[2].split("/")
    if list_path_to[-1] == "":
        list_path_to[-1] = list_path_from[-1]
    current_path = ""
    for ind in range(len(list_path_to) - 1):
        current_path += list_path_to[ind]
        if not os.path.exists(current_path):
            os.mkdir(current_path)
        current_path += "/"
    os.rename(parse_list_parameters[1], "/".join(list_path_to))
