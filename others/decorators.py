def decorator(func):
    def wrapper(*args, **kwargs):
        print("This is the decorator")
        func(*args, **kwargs)
        print("After executing the decorator")
    return wrapper


@decorator
def main():
    print("Hola como estas")

main()
