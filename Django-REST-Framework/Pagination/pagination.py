
from collections import namedtuple

Person = namedtuple('person', ['first_name', 'last_name', 'age'])

DATA = [
    Person('Jessica', 'Vega', 77),
    Person('Tamara', 'Garcia', 43),
    Person('Frank', 'Landry', 37),
    Person('Kimberly', 'Bell', 56),
    Person('Melissa', 'Roberts', 63),
    Person('Douglas', 'Murphy', 40),
    Person('Mary', 'Hart', 33),
    Person('Michael', 'Jennings', 76),
    Person('Haley', 'Schaefer', 62),
    Person('Melissa', 'Cortez', 61),
    Person('Nicole', 'Ellison', 67),
    Person('Mark', 'Jordan', 20),
    Person('Matthew', 'Dudley', 67),
    Person('Joshua', 'Austin', 47),
    Person('Caleb', 'Jones', 72),
    Person('Latoya', 'Dickson', 65),
    Person('Michelle', 'Garcia', 36),
    Person('Brad', 'Oconnell', 24),
    Person('Joshua', 'Austin', 47),
    Person('Caleb', 'Jones', 72),

]


class Pagination:

    PAGE_SIZE = 2
    ENDPOINT_NAME = 'http://mysite.com/people'

    def paginate_queryset(self, queryset, page_number):

        self.count = len(queryset)
        self.page_number = page_number
        self.max_page_number = (self.count // self.PAGE_SIZE) + 1

        last_index = page_number*self.PAGE_SIZE
        first_index = last_index - self.PAGE_SIZE

        return self.get_paginated_response(queryset[first_index:last_index])

    def get_paginated_response(self, data):
        return {
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        }

    def get_next_link(self):
        return None

    def get_previous_link(self):
        return None


p = Pagination()

print(p.paginate_queryset(DATA, 10))
