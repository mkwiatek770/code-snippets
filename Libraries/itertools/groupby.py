import itertools


def get_nation(person):
    return person['nation']

people = [
    {
        'name': 'Michał Kwiatek',
        'nation': 'PL'
    },
    {
        'name': 'Joe Doe',
        'nation': 'USA'
    },
    {
        'name': 'Alice Cooper',
        'nation': 'GB'
    },
    {
        'name': 'Julius Cesar',
        'nation': 'PL'
    },
    {
        'name': 'Robert Lewandowski',
        'nation': 'PL'
    }
]

# expects initial iterable to be already sorted by key that we want to group by!!!
for key, group in itertools.groupby(sorted(people, key=get_nation), key=get_nation):
    print(f'{key}:')
    for person in group:
        print(f'- {person["name"]}')
