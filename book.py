class Book:
    id = None
    renewed = None
    due_date = None
    author = None
    title = None

    def print(self):
        print(f'id:{self.id}\nrenewed:{self.renewed}\ndue_date:{self.due_date}\nauthor:{self.author}\ntitle:{self.title}')
