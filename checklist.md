# Сheck Your Code Against the Following Points

## Code Efficiency

1. Make sure you check that the `mv` input command is correct.
2. Notice that if you will try to create the directory already exists then it 
will lead to an error.

## Code Style

1. Use one style of quotes in your code. Double quotes are preferable.
2. Use descriptive and correct variable names.

Good example:

```python
with open("list_of_workers.txt", "r") as source:
    pass
```

Bad example:

```python
with open("list_of_workers.txt", "r") as f:
    pass
```

3. Use `os.path.join` to concatenate parts of the path. 
In that case, your app will be cross-platform and will 
use either `/` or `\` depending on OS

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.