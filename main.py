from token.generator import generate_token


def main():
    print("Encripted token for secure transaction:")
    print(generate_token())

if __name__ == "__main__":
    main()