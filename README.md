# Intermediate Software Development Activity 2

This activity will help to reinforce learning of the Module 2 concepts of:

- Abstraction:
        - `Shape` is an abstract base class (`ABC`) with abstract methods `calculate_area()` and `calculate_perimeter()` that must be implemented by all shapes.
        - File: `shape/shape.py`

- Inheritance
        - `Triangle` and `Rectangle` inherit from `Shape` and call `super().__init__(color)` to reuse color validation.
        - Files: `shape/triangle.py`, `shape/rectangle.py`

- Polymorphism
        - Subclasses override `calculate_area()`, `calculate_perimeter()`, and `__str__()`.  
        - The client program iterates a `list[Shape]` and calls the same methods on different shape types, demonstrating a common interface with different behavior.
        - Files: `activity_02_main.py`, `shape/triangle.py`, `shape/rectangle.py`

## How to run

- **Run tests:**  
  `python -m unittest discover -s tests -p "test_*.py"`
- **Run client program:**  
  `python activity_02_main.py`


- Package Initialization
        All classes can be imported with a single statement thanks to `shape/__init__.py`:
        ```python
        from shape import *

## Author
Parneet kaur

## Additional Information
## Additional Information

- **Abstraction:** `Shape` is an abstract base class with abstract `calculate_area()` and `calculate_perimeter()` methods.
- **Inheritance:** `Triangle` and `Rectangle` inherit from `Shape` and reuse color validation via `super().__init__()`.
- **Polymorphism:** Both subclasses override `__str__`, `calculate_area`, and `calculate_perimeter`; the client iterates a `list[Shape]` and calls the same methods on different shapes.

