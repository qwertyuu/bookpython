import pydotenv
from airtable import Airtable

from bibli import Bibli


def main():
    env = pydotenv.Environment(check_file_exists=True)
    airtable = Airtable(env.get('AIRTABLE_BASE_KEY'), 'books', api_key=env.get('AIRTABLE_API_KEY'))
    b = Bibli(env.get('CARD_NUMBER'), env.get('PASSWORD'))
    b.hydrate_books()
    b.close()
    pass


if __name__ == "__main__":
    main()
