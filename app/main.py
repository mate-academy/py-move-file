# write your code here
import os


def move_file(command: str) -> None:
    file = command.split()
    pathway_file = os.path.split(file[2])
    if os.path.exists(file[1]):
        if file[2].count("/") == 0:
            os.rename(file[1], file[2])
        else:
            if not os.path.isdir(pathway_file[0]):
                os.makedirs(pathway_file[0])
            with (open(file[1], "r") as file_in,
                  open(f"{os.path.join(file[2])}", "w") as file_out):
                file_out.write(file_in.read())
                os.remove(file[1])


#move_file(f"mv file.txt first_dir/second_dir/file2.txt")