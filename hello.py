def greet(name: str = "DSH") -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
