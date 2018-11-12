from dotenv import load_dotenv

from bibli import Bibli

load_dotenv()


def main():
    b = Bibli()
    b.hydrate_books()
    b.close()
    pass


if __name__ == "__main__":
    main()
