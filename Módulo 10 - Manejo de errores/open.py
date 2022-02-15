# def main():
#     try:
#         open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     #open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()

#CONTROLANDO LAS EXCEPCIONES
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()