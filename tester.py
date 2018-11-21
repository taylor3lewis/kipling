# coding: utf-8
# from six.pattern_searcher import find_names, find_dates, find_places, find_why, find_how
from six.pattern_searcher import find_names
from six.pattern_searcher import find_dates
from six.pattern_searcher import find_places
from six.pattern_searcher import find_why
from six.pattern_searcher import find_how

file_name = 'texts/not1.txt'

f = open(file_name, 'r')
content = f.readlines()
f.close()

print ''
print "- WHO ".ljust(75, '-')
for e in find_names(content):
    print e
print ''

print "- WHEN ".ljust(75, '-')
for e in find_dates(content):
    print e
print ''

print "- WHERE ".ljust(75, '-')
for e in find_places(content):
    print e
print ''

print "- WHYS ".ljust(75, '-')
for e in find_why(content):
    print e
print ''

print "- HOW ".ljust(75, '-')
for e in find_how(content):
    print e
