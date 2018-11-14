import pydotenv
from airtable import Airtable
import bibli_sync

from bibli import Bibli


def main():
    my_bibli.hydrate_books()
    my_bibli.close()
    bibli_sync.sync(airtable, my_bibli.book_objects)


env = pydotenv.Environment(check_file_exists=True)
airtable = Airtable(env.get('AIRTABLE_BASE_KEY'), 'books', api_key=env.get('AIRTABLE_API_KEY'))
my_bibli = Bibli(env.get('CARD_NUMBER'), env.get('PASSWORD'))


if __name__ == "__main__":
    main()
