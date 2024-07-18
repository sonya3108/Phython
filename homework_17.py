def result_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return {'result': result}
    return wrapper

def result(name):
    return f"Hello, {name}!"


result= result_decorator(result)

print(result("Alice"))
