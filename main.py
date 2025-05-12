def hello(name="GitHub Actions"):
    if not isinstance(name, str):
        raise TypeError("Le nom doit être une chaîne")
    return f"Hello, {name}!"
