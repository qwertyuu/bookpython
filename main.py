import pydotenv
from bibli import Bibli


def main():
    env = pydotenv.Environment(check_file_exists=True)
    b = Bibli(env.get('CARD_NUMBER'), env.get('PASSWORD'))
    b.hydrate_books()
    input()
    b.close()
    pass


if __name__ == "__main__":
    main()
