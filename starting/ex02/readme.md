# Python Functions: The Core Guide

## 📖 Description

This guide provides a concise yet comprehensive overview of functions in Python, from fundamental concepts to advanced features. Functions are blocks of reusable code that perform specific tasks, crucial for organized, readable, and efficient programming.

## 📜 Table of Contents

1. [Part 1: Function Fundamentals](#part-1-function-fundamentals)

   * [1.1. Defining and Calling Functions](#11-defining-and-calling-functions)
   * [1.2. The `return` Statement](#12-the-return-statement)
   * [1.3. Why Use Functions?](#13-why-use-functions)
2. [Part 2: Essential Concepts](#part-2-essential-concepts)

   * [2.1. Parameters and Arguments (Positional & Keyword)](#21-parameters-and-arguments-positional--keyword)
   * [2.2. Default Argument Values](#22-default-argument-values)
   * [2.3. Return Values (Multiple, `None`)](#23-return-values-multiple-none)
   * [2.4. Docstrings](#24-docstrings)
   * [2.5. Variable Scope (LEGB, `global`, `nonlocal`)](#25-variable-scope-legb-global-nonlocal)
3. [Part 3: Intermediate Techniques](#part-3-intermediate-techniques)

   * [3.1. `*args` and `**kwargs`](#31-args-and-kwargs)
   * [3.2. Unpacking Arguments](#32-unpacking-arguments)
   * [3.3. Lambda (Anonymous) Functions](#33-lambda-anonymous-functions)
   * [3.4. Higher-Order Functions (`map`, `filter`, `reduce`)](#34-higher-order-functions-map-filter-reduce)
   * [3.5. Recursion](#35-recursion)
   * [3.6. Function Annotations (Type Hinting)](#36-function-annotations-type-hinting)
4. [Part 4: Advanced Concepts](#part-4-advanced-concepts)

   * [4.1. Closures](#41-closures)
   * [4.2. Decorators](#42-decorators)
   * [4.3. Generators and `yield`](#43-generators-and-yield)
   * [4.4. Generator Expressions](#44-generator-expressions)
   * [4.5. `async/await` and Coroutines](#45-asyncawait-and-coroutines)
   * [4.6. `functools.partial`](#46-functoolspartial)
   * [4.7. `callable()`](#47-callable)
5. [Part 5: Expert Insights & Internals](#part-5-expert-insights--internals)

   * [5.1. Functions as First-Class Objects & Attributes](#51-functions-as-first-class-objects--attributes)
   * [5.2. Methods vs. Functions (Bound/Unbound)](#52-methods-vs-functions-boundunbound)
   * [5.3. The Descriptor Protocol (Briefly)](#53-the-descriptor-protocol-briefly)
   * [5.4. `__call__()` Method for Instances](#54-__call__-method-for-instances)
   * [5.5. `inspect` Module Overview](#55-inspect-module-overview)
   * [5.6. Memoization with `functools.lru_cache`](#56-memoization-with-functoolslru_cache)

---

## Part 1: Function Fundamentals

### 1.1. Defining and Calling Functions

Define with `def`, name, parentheses `()`, and a colon `:`. Indented code block forms the function body. Call by name followed by `()`.

```python
def greet():
    print("Hello!")

greet()  # Output: Hello!
```

### 1.2. The `return` Statement

Functions can return a value to the caller using `return`.

```python
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8
```

If `return` is omitted or used alone, the function returns `None`.

### 1.3. Why Use Functions?

* **Organization**: Break code into logical, manageable units.
* **Reusability (DRY)**: Write once, use multiple times.
* **Readability**: Well-named functions improve code clarity.
* **Abstraction**: Hide implementation details.
* **Maintainability**: Easier to update and debug.

## Part 2: Essential Concepts

### 2.1. Parameters and Arguments (Positional & Keyword)

* **Parameters**: Variables in function definition.
* **Arguments**: Values passed during function call.

```python
def describe(name, age):
    print(f"{name} is {age} years old.")

# Positional
describe("Alice", 30)
# Keyword
describe(age=25, name="Bob")
# Mix
describe("Carol", age=22)
```

### 2.2. Default Argument Values

Provide default values for parameters.

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # 9
print(power(3, 3)) # 27
```

**Caution**: For mutable defaults, use `None` sentinel.

```python
def append_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
```

### 2.3. Return Values (Multiple, `None`)

* **Single Value**: `return value`
* **Multiple Values**: `return a, b` (tuple)

```python
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
```

Functions without explicit `return` return `None`.

### 2.4. Docstrings

String literal as first statement; use `help()` or `.__doc__`.

```python
def calculate_area(length, width):
    """
    Calculates area of a rectangle.

    Args:
        length (float): length.
        width (float): width.

    Returns:
        float: area.
    """
    return length * width
```

### 2.5. Variable Scope (LEGB, `global`, `nonlocal`)

* **Local**: Inside current function.
* **Enclosing**: Outer function for nested.
* **Global**: Top-level of module.
* **Built-in**: Python built-ins.

```python
x = "global"

def outer():
    y = "enclosing"
    def inner():
        z = "local"
        print(x, y, z)
    inner()
outer()
```

* `global` to modify globals.
* `nonlocal` to modify enclosing.

## Part 3: Intermediate Techniques

### 3.1. `*args` and `**kwargs`

```python
def func(a, *args, **kwargs):
    print(a, args, kwargs)

func(1, 2, 3, x=4)
```

### 3.2. Unpacking Arguments

```python
def add(a, b, c): return a + b + c
nums = [1,2,3]
print(add(*nums))
data = {'a':1,'b':2,'c':3}
print(add(**data))
```

### 3.3. Lambda (Anonymous) Functions

```python
mul = lambda x, y: x*y
print(mul(5,4))
```

### 3.4. Higher-Order Functions (`map`, `filter`, `reduce`)

```python
list(map(lambda x: x*x, [1,2,3]))
list(filter(lambda x: x%2==0, [1,2,3,4]))
from functools import reduce
reduce(lambda x,y: x*y, [1,2,3,4])
```

List comprehensions often preferred.

### 3.5. Recursion

```python
def fact(n):
    if n<2: return 1
    return n*fact(n-1)
```

### 3.6. Function Annotations (Type Hinting)

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
print(greet.__annotations__)
```

## Part 4: Advanced Concepts

### 4.1. Closures

```python
def make_mul(f):
    def mul(n): return n*f
    return mul

double = make_mul(2)
print(double(5))
```

### 4.2. Decorators

```python
import functools

def log(f):
    @functools.wraps(f)
    def w(*a,**k):
        print(f"Calling {f.__name__}")
        return f(*a,**k)
    return w

@log
def add(a,b): return a+b
```

### 4.3. Generators and `yield`

```python
def gen(n):
    for i in range(n): yield i
```

### 4.4. Generator Expressions

```python
(g*i for i in range(5))
```

### 4.5. `async/await` and Coroutines

```python
import asyncio
async def say(msg):
    await asyncio.sleep(1)
    print(msg)
asyncio.run(say("Hi"))
```

### 4.6. `functools.partial`

```python
from functools import partial
pow2 = partial(pow, exp=2)
```

### 4.7. `callable()`

```python
print(callable(lambda:0))
print(callable(5))
```

## Part 5: Expert Insights & Internals

### 5.1. First-Class Objects & Attributes

Functions have `__name__`, `__doc__`, `__defaults__`, `__code__`, etc.

### 5.2. Methods vs. Functions

Bound methods implicitly pass `self`.

### 5.3. Descriptor Protocol

Functions implement `__get__` to bind methods.

### 5.4. `__call__()` for Instances

```python
class C:
    def __call__(self,x): return x
c=C(); print(c(5))
```

### 5.5. `inspect` Module Overview

```python
import inspect
print(inspect.signature(add))
```

### 5.6. Memoization with `functools.lru_cache`

```python
from functools import lru_cache
@lru_cache()
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
```

