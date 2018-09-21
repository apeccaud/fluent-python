haystack = {
    'a@a.com',
    'b@b.com',
    'c@c.com',
    'a@a.com'
}

needles = {
    'c@c.com',
    'd@d.com',
    'a@a.com'
}

intersection = len(needles & haystack)  # Count intersection between needles and haystack
union = len(needles | haystack)  # Count union between needles and haystack
difference = len(needles - haystack)  # Count difference between needles and haystack

print(intersection, union, difference)
# Output : 2 4 1
