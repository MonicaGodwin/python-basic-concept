# Python Comprehensions

This folder contains my practice and notes on **list, dictionary, and set comprehensions** in Python.

Comprehensions provide a shorter and cleaner way to create collections from existing iterables.

## 1. List Comprehension

A list comprehension is used to create a new list.

### Basic syntax

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = [num * 2 for num in numbers]

print(result)
```

Output:

```text
[2, 4, 6, 8, 10]
```

### List comprehension with a condition

We can filter values using `if`.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [num for num in numbers if num % 2 == 0]

print(result)
```

Output:

```text
[2, 4, 6]
```

### Transforming and filtering

We can also transform a value while filtering it.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [num * num for num in numbers if num % 2 == 0]

print(result)
```

Output:

```text
[4, 16, 36]
```

## 2. Dictionary Comprehension

Dictionary comprehensions are used to create dictionaries.

### Basic syntax

```python
{key: value for item in iterable}
```

Example:

```python
numbers = [1, 2, 3, 4]

result = {num: num * 2 for num in numbers}

print(result)
```

Output:

```text
{1: 2, 2: 4, 3: 6, 4: 8}
```

### Using a dictionary comprehension with `.items()`

```python
students = {
    "Monica": 85,
    "John": 72,
    "Alex": 91,
    "David": 65,
    "Lucy": 88
}

result = {
    name: score
    for name, score in students.items()
    if score >= 80
}

print(result)
```

Output:

```text
{'Monica': 85, 'Alex': 91, 'Lucy': 88}
```

## 3. Set Comprehension

A set comprehension creates a set.

### Basic syntax

```python
{expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 2, 3, 3, 4, 5]

result = {num * 2 for num in numbers}

print(result)
```

Output:

```text
{2, 4, 6, 8, 10}
```

Sets automatically remove duplicate values.

### Set comprehension with a condition

```python
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]

result = {num * num for num in numbers if num % 2 == 0}

print(result)
```

Output:

```text
{4, 16, 36}
```

## 4. Generator Expression

A generator expression looks similar to a list comprehension, but uses parentheses.

```python
numbers = [1, 2, 3, 4, 5]

result = (num * 2 for num in numbers)
```

Unlike a list comprehension, the generator does not create all the values immediately. It produces them when needed.

```python
print(next(result))
print(next(result))
```

Output:

```text
2
4
```

Generator expressions are useful when working with large amounts of data.

## 5. Comparing Comprehensions

### List

```python
[num * 2 for num in numbers]
```

Creates a **list**.

### Dictionary

```python
{num: num * 2 for num in numbers}
```

Creates a **dictionary**.

### Set

```python
{num * 2 for num in numbers}
```

Creates a **set**.

### Generator

```python
(num * 2 for num in numbers)
```

Creates a **generator**.

## 6. Easy Way to Remember

```text
[ ]       → List comprehension

{key: value} → Dictionary comprehension

{value}   → Set comprehension

( )       → Generator expression
```

The general idea is:

> Go through a collection, optionally filter the values, transform them, and create a new collection.

## What I Learned

* List comprehensions
* Dictionary comprehensions
* Set comprehensions
* Generator expressions
* Filtering with `if`
* Transforming values
* Combining filtering and transformation
* Using `.items()` with dictionary comprehensions
* Sets automatically remove duplicates
* Generators produce values when needed
