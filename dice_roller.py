import random


def main():
    print('You rolled a die')
    face_up = random.randint(1, 6)
    print(f'you got {face_up}')


if __name__ == "__main__":
    main()
