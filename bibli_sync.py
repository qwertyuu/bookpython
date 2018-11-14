from airtable import Airtable
import pydotenv
import datetime

from book import Book


def sync(airtable: Airtable, local_books):
    print('Fetching Airtable books...')
    airtable_books = airtable.get_all(view='Active')
    airtable_book_ids = [b['fields']['ID'] for b in airtable.get_all(view='Active')]
    local_book_ids = [b.id for b in local_books]

    # --- RETURN ---
    # Books that are in airtable but not in local
    returned_books = find_airtable(diff(airtable_book_ids, local_book_ids), airtable_books)
    for returned_book in returned_books:
        airtable.update(returned_book['id'], {'ReturnedAt': datetime.datetime.now().strftime('%Y-%m-%d')})
    if returned_books:
        print(f'User has {len(returned_books)} returned books')

    # --- NEW BOOKS ---
    # Books that are in local but not in airtable
    new_books = find_local(diff(local_book_ids, airtable_book_ids), local_books)
    for new_book in new_books:
        airtable.insert(airtable_book_from_local_book(new_book))
    if new_books:
        print(f'User has {len(new_books)} new books')

    # --- STILL BOOKS ---
    # Books that are in local and in airtable
    still_book_ids = intersect(local_book_ids, airtable_book_ids)
    still_airtable_books = find_airtable(still_book_ids, airtable_books)
    still_local_books = find_local(still_book_ids, local_books)
    for still_airtable_book in still_airtable_books:
        corresponding_still_local_book = find_local([still_airtable_book['fields']['ID']], still_local_books)[0]
        airtable.update(still_airtable_book['id'], airtable_book_from_local_book(corresponding_still_local_book))
    if still_book_ids:
        print(f'User has {len(still_book_ids)} still books')


def diff(a, b):
    b = set(b)
    return [x for x in a if x not in b]


def intersect(a, b):
    b = set(b)
    return [x for x in a if x in b]


def find_airtable(ids, airtable_books):
    return [b for b in airtable_books if b['fields']['ID'] in ids]


def find_local(ids, local_books):
    return [b for b in local_books if b.id in ids]


def airtable_book_from_local_book(local_book: Book):
    return {
        'ID': local_book.id,
        'Author': local_book.author,
        'Title': local_book.title,
        # TODO: Implement page amt
        'Pages': None,
        'Renewed': local_book.renewed,
        'ScheduledReturn': local_book.due_date_utc,
    }


if __name__ == "__main__":
    env = pydotenv.Environment(check_file_exists=True)
    airtable = Airtable(env.get('AIRTABLE_BASE_KEY'), 'books', api_key=env.get('AIRTABLE_API_KEY'))

    exampleBook = Book()
    exampleBook.id = 'asdf'
    exampleBook2 = Book()
    exampleBook2.id = 'ajaja'
    sync(airtable, [exampleBook2])

