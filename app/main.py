import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        operation, source_file, destination = command.split()
        if operation == "mv":
            if not os.path.dirname(destination):
                os.replace(source_file, destination)
            else:
                target_directory = os.path.dirname(destination)
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory, exist_ok=True)
                os.replace(source_file, destination)
        else:
            print("Error: operation should be 'mv'")

    else:
        print("Error: wrong format. It should be 'mv source_file destination'")
