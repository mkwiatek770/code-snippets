import itertools
import string


numbers = (0, 1)


def guess_password(real):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return f'password is {guess}. found in {attempts} guesses.'
            # uncomment to display attempts, though will be slower
            #print(guess, attempts)



if __name__ == '__main__':
    print(guess_password('abc'))

    # combination - order does not matter
    comb = itertools.combinations(numbers, 2)
    print(f'Combinations: {list(comb)}')
    # permutation - order matters (n! of elements)
    perm = itertools.permutations(numbers, 2)
    print(f'Permutations: {list(perm)}')
    # cartesian product
    prod = itertools.product(numbers, repeat=2)
    print(f'Product: {list(prod)}')
