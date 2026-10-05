# Python Generators

This folder contains my practice and notes on **generator expressions, iterators, `next()`, and `yield`** in Python.

## 1. Generator Expression

A generator expression looks similar to a list comprehension, but it uses parentheses `()` instead of square brackets `[]`.

```python
numbers = [1, 2, 3, 4, 5]

result = (num * 2 for num in numbers)
```

A generator does not create all the results at once. It produces values one at a time when they are needed.

## 2. `next()`

The `next()` function gets the next value from a generator or iterator.

```python
print(next(result))
print(next(result))
```

Output:

```text
2
4
```

When there are no more values, Python raises `StopIteration`.

## 3. `iter()`

The `iter()` function converts an iterable, such as a list, into an iterator.

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

Output:

```text
1
2
```

A list is an **iterable**, while the object returned by `iter()` is an **iterator**.

## 4. Generator Functions and `yield`

A generator function uses the `yield` keyword to produce values one at a time.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

We can get the values using `next()`:

```python
result = numbers()

print(next(result))
print(next(result))
print(next(result))
```

Output:

```text
1
2
3
```

Unlike `return`, `yield` does not completely end the function. It pauses the function and continues from where it stopped when `next()` is called again.

## 5. Generator with a Loop

Generators can also be created using loops.

```python
def even_numbers():
    for num in range(2, 11, 2):
        yield num
```

We can process the values using a `for` loop:

```python
result = even_numbers()

for num in result:
    print(num)
```

Output:

```text
2
4
6
8
10
```

## 6. Why Use Generators?

Generators are useful when working with large amounts of data because they produce values **when needed** instead of creating all the values in memory at once.

For example:

```python
numbers = (num * 2 for num in range(10_000_000))
```

The generator does not immediately create a list containing 10 million values.

### Simple way to remember

```text
List comprehension → creates the values immediately
Generator expression → produces values when needed

iter() → creates an iterator
next() → gets the next value
yield → produces a value and pauses the generator
```

## What I Learned

* Generator expressions
* `iter()`
* `next()`
* Iterables and iterators
* `yield`
* Generator functions
* `StopIteration`
* Using generators with `for` loops
* Why generators can save memory
