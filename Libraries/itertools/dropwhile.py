from itertools import dropwhile


def fetch_all_useful_data(name='/etc/passwd'):
    """
    example output:
    nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0:System Administrator:/var/root:/bin/sh
    """
    with open(name) as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')
