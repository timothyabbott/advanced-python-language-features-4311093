# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
# original
evens_squared = list(map (lambda even:even**2,evens)),filter(lambda even:even>4 and even<16, evens)
# simpler
evens_squared = [even**2 for even in evens if 4<even<16]
# TODO: Derive a new list of numbers frm a given list
evens_squared = [even**2 for even in evens]

# TODO: Limit the items operated on with a predicate condition
odds_sqaured = [odd**2 for odd in odds if 3<odd<17]
print(evens_squared)
print(odds_sqaured)
