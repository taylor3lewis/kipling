from six.pattern_searcher import find_names
from six.pattern_searcher import find_dates
from six.pattern_searcher import find_places

file_name = 'texts/not4.txt'

f = open(file_name, 'r')
content = f.readlines()
f.close()

print ''
print "- NAMES ".ljust(75, '-')
for n in find_names(content):
    print n

print ''
print "- DATES ".ljust(75, '-')
for d in find_dates(content):
    print d

print ''
print "- PLACES ".ljust(75, '-')
for p in find_places(content):
    print p

