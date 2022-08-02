import os


def move_file(command):
    s_list = command.split(" ")
    dao_str = s_list[2]
    file_in = s_list[1]
    file_out = dao_str[-dao_str.index('/'):]
    dao = dao_str[:-dao_str.index('/')]

    with open(file_in, 'r') as f1:
        cont = f1.read()
        os.makedirs(dao)

    os.remove(file_in)
    os.chdir(dao)

    with open(file_out, 'w') as f2:
        f2.write(cont)
