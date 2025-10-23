# Move file

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Write a function `move_file` that will move a file from one location to another. 
Function takes `command`, this is very similar to Linux mv command: 
`mv file.txt some_dir/new_file.txt` 
(this will create `new_file.txt` in `some_dir/` and remove the source file).

If name in destination path ends with / it must be considered as a directory.
The app must support only moving of files, and no additional options (flags).
Examples:
- `mv file.txt file2.txt` simply renames the file.
- `mv file.txt first_dir/second_dir/file2.txt` create directory `first_dir`
inside current directory, then create directory `first_dir/second_dir`,
create file2.txt inside and remove the source file.

```python
print(open("tests/file.txt").read())
# Some
# Text
move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
print(open("first_dir/second_dir/third_dir/file2.txt").read())
# Some
# Text
open("tests/file.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
```

**Note**: You can create directory by `os.mkdir("first")` from module `os`.
But to create `os.mkdir("first/second")`, `first` directory needs to exist.
Function should work with different directory depth.
Use `os.remove()` to remove the file.


### Note: Check your code using this [checklist](checklist.md) before pushing your solution.