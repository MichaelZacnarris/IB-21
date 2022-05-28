class listbooks:


    def __init__(self, name, author, year, number, id):
        self.name = name
        self.author = author
        self.year = year
        self.number = number
        self.id = id

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_number(self):
        return self.number

    def get_id(self):
        return self.id

    def set_name(self, new_name):
        self.name = new_name

    def set_author(self, new_author):
        self.author = new_author

    def set_year(self, new_year):
        self.year = new_year

    def set_number(self, new_number):
        self.number = new_number