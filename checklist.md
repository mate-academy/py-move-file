# Сheck Your Code Against the Following Points

## Code Efficiency

1. Make sure you check that the input string contains 3 elements separated by space, and has `mv` on a first place.
2. Notice that if you will try to create the directory already exists then it 
will lead to an error.

## Code Style

1. Use a consistent style of quotes in your code: either double or single, but double quotes are preferred.
2. Use descriptive and correct variable names.

Good example:

```python
source_file_name = "list_of_workers.txt"
with open(source_file_name, "r") as source_file_object:
    pass
```

Bad example:

```python
f1 = "list_of_workers.txt"
with open(f1, "r") as f_s:
    pass
```

3. Use `os.path.join` to concatenate parts of the path. 
In that case, your app will be cross-platform and will 
use either `/` or `\` depending on OS
4. Be sure that you are calling needed methods only once (e.g. `.split()`).
5. If you need to assign values from a list to individual variables, it's better to use unpacking.

Good example:

```python
values = [1, 2, 3]
first_value, second_value, third_value = values
```

Bad example:

```python
values = [1, 2, 3]
first_value = values[0]
second_value = values[1]
third_value = values[2]
```


## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.