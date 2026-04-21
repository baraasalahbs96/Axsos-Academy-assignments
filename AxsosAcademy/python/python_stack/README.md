# Zoo Management System: Inheritance & Polymorphism

A Python-based simulation of a Zoo ecosystem that demonstrates advanced Object-Oriented Programming (OOP) principles, specifically Inheritance, Method Overriding, and Composition.

## 🚀 Features

- **Inheritance Hierarchy:** A base `Animal` class provides shared attributes (`health`, `happiness`) and methods to various specific animal types.
- **Method Overriding (Polymorphism):** Specific subclasses (like `Walrus`) override default behaviors (like `feed`) to reflect unique species characteristics.
- **Composition-Based Management:** A `Zoo` class acts as a container, managing a collection of diverse animal objects and providing centralized reporting.
- **Factory Pattern Logic:** The `Zoo` class provides specialized methods to instantiate and categorize different animal types.

## 🛠️ Technical Concepts

- **`super().__init__`**: Correctly calling the parent constructor to initialize shared data while adding subclass-specific attributes (e.g., `tail_length`, `is_swimmer`).
- **Encapsulation:** Protecting animal stats and exposing them through controlled methods like `display_info()`.
- **Iterative Interaction:** Leveraging Python loops to interact with a list of polymorphic objects (calling `.feed()` on any animal regardless of its specific type).

## 📋 Zoo Structure

1. **Animal (Base):** Shared properties and default `feed()` logic.
2. **Lion:** Adds `tail_length` attribute.
3. **Walrus:** Overrides `feed()` with custom logic and specific console feedback.
4. **Monkey:** Adds `favorite_fruit` attribute.
5. **Zoo:** The controller class that handles the `animals` list.

## 💻 How to Run
```bash to correct path 
python main.py