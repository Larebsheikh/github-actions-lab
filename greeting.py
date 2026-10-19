def generate_greeting(name):
    if not name or not name.strip():
        return "Hello, Guest!"
    return f"Hello, {name.strip()}!"
