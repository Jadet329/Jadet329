def main():
    camel_case = input("Enter a variable name in camelCase: ")

    snake_case = ""

    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    print(snake_case)

if __name__ == "__main__":
    main()
