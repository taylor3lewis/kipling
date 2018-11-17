from six.pattern_searcher import find_names
from six.pattern_searcher import find_dates
file_name = 'texts/not4.txt'

print ''
print "- NAMES ".ljust(75, '-')
for n in find_names(file_name):
    print n

print ''
print "- DATES ".ljust(75, '-')
for d in find_dates(file_name):
    print d


