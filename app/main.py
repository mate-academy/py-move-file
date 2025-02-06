import os

# write your code here
def move_file(command: str):
    command_list = command.split()
    if len(command_list) != 3:
        return "The command should be: mv source destination"
    source = command_list[1]
    destination = command_list[2]
    destination_list = destination.split("/")
    destination_str = "/".join(destination_list[0:-1])
    if len(destination_list) > 1:
        if not os.path.exists(destination_str):
            if destination[-1] != "/":
                os.makedirs(destination_str, exist_ok=True)
            else:
                os.makedirs(destination, exist_ok=True)
    try:
        with open(source, "r") as f, open(destination, "w") as file:
            file.write(f.read())
        os.remove(source)
    except FileNotFoundError:
        return "Check source file"
# write your code here
