# FILE I/O in Python

In Python, File Input/Output (I/O) is a core concept. It allows you to read and write data to and from files. Python provides several built-in functions for performing I/O operations on files. In this guide, we'll explore how to work with files in Python.

# Opening a file
Before you can read or write to a file, you must first open it. To open a file in Python, you can use the built-in `open()` function. The `pen()` function takes two arguments: the filename and the mode in which you want to open the file.

The mode can be one of the following:

- `r: read mode (default)`
- `w: write mode`
- `a: append mode`
- `x: exclusive creation mode (file must not exist)`
- `b: binary mode`
- `t: text mode (default)`

Here is an example of how to open a file in read mode:

```python
file = open('example.txt', 'r')
```

# Reading a file
Once you have opened a file, you can read its contents. There are several methods you can use to read from a file in Python.

# Reading the entire file at once
The simplest way to read a file is to read the entire file at once. You can do this using the `read()` method.

```python
file = open('example.txt', 'r')
contents = file.read()
print(contents)
```

# Reading line by line
You can also read a file line by line using a loop. Here is an example:

```python
file = open('example.txt', 'r')
for line in file:
    print(line)
```

# Closing a file
When you are finished reading a file, you should close it using the close() method.

```python
file = open('example.txt', 'r')
contents = file.read()
file.close()
```

# Writing to a file
To write to a file, you must open it in write mode using the open() function. You can then write to the file using the write() method.

```python
file = open('example.txt', 'w')
file.write('Hello, world!')
file.close()
```

If the file you are writing to does not exist, it will be created.

# Appending to a file
To append to an existing file, you must open it in append mode using the open() function. You can then write to the file using the write() method.

```python
file = open('example.txt', 'a')
file.write('Hello again, world!')
file.close()
```

# Conclusion
Python's built-in file I/O functions make it easy to read from and write to files. By mastering these functions, you can manipulate data in files and automate data processing tasks. Remember to always close your files when you are finished working with them!
