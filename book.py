from datetime import datetime


class Book:
    id = None
    renewed = None
    due_date = None
    author = None
    title = None

    def print(self):
        print(f'id:{self.id}\n'
              f'renewed:{self.renewed}\n'
              f'due_date:{self.due_date}\n'
              f'author:{self.author}\n'
              f'title:{self.title}')
        self.days_remaining()

    def days_remaining(self):
        decoded_due_date = datetime.strptime(self.due_date, '%d/%m/%y')
        print(decoded_due_date - datetime.now())

    @property
    def due_date_utc(self):
        return datetime.strptime(self.due_date, '%d/%m/%y').strftime('%Y-%m-%d')
