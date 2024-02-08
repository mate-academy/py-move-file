import os


def move_file(input_str: str) -> None:
    base_dir = os.getcwd()
    list_from_input_str = input_str.split()
    with open(list_from_input_str[1], "r") as input_file:
        text_from_input_file = input_file.read()
    os.remove(list_from_input_str[1])
    if "/" in list_from_input_str[2]:
        list_dir_and_file = list_from_input_str[2].split("/")
        output_file_name = list_dir_and_file[-1]
        for i in range(len(list_dir_and_file) - 1):
            if os.path.exists(list_dir_and_file[i]):
                os.chdir(list_dir_and_file[i])
            else:
                os.mkdir(list_dir_and_file[i])
                os.chdir(list_dir_and_file[i])
        with open(output_file_name, "w") as output_file:
            output_file.write(text_from_input_file)
        os.chdir(base_dir)
    else:
        with open(list_from_input_str[2], "w") as output_file:
            output_file.write(text_from_input_file)
