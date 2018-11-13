import re
from custom_libs.toth.acutes_filter import strip_non_text
from custom_libs.toth.toth import check_str_integrity
from six.who import NAMES
from six.who import SURNAMES
from custom_libs.toth.stop_words.preposicoes import PREPOSICOES
from custom_libs.toth.stop_words.contracoes import CONTRACOES

file_name = 'texts/not4.txt'

f = open(file_name, 'r')
names_found = []

# found sentences
for raw_line in f.readlines():
    line = unicode(raw_line.strip('\n').lower(), 'utf-8')
    while '  ' in line:
        line = line.replace('  ', ' ')
    if line:
        line = strip_non_text(line)
        while '  ' in line:
            line = line.replace('  ', ' ')
        x = strip_non_text(line.strip()).lower().split()
        tokens = [token for token in x if check_str_integrity(token)]
        check = [t for t in tokens if t in NAMES]
        if check:
            names_found.append(raw_line.strip('\n'))

# process sentences
names_matched = []
for sentence in names_found:
    # phrases
    for phrase in re.split(r"[,!;:]", sentence):
        phrase = phrase.replace('\n', ' ')
        phrase = phrase.replace('\r', ' ')

        phrase_unicode = unicode(phrase.strip('\n').lower(), 'utf-8')
        check = [t for t in phrase_unicode.split() if t in NAMES]

        if check:
            full_names = []
            in_name = False
            names_count = -1

            tokens = [w for w in phrase_unicode.strip().lower().split()
                      if w in NAMES or w in SURNAMES]

            while tokens and (tokens[0] in PREPOSICOES or tokens[0] in CONTRACOES or tokens[0] == "e"):
                tokens = tokens[1:]
            while tokens and (tokens[-1] in PREPOSICOES or tokens[-1] in CONTRACOES or tokens[-1] == "e"):
                tokens = tokens[:-1]

            if len(tokens) > 1:
                names_matched.append(tokens)
                # print phrase
                # print tokens
                # print '-' * 100


# READY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
names_matched_sorted = [" ".join(names) for names in names_matched]
names_matched_sorted.sort(key=lambda s: len(s))

frags1 = set()
for name in names_matched_sorted:
    for name2 in names_matched_sorted:
        if name != name2:
            if name in name2 and name not in frags1:
                frags1.add(name)
                continue
            frags1.add(name)

frags2 = set()
for name in names_matched_sorted:
    for name_frag1 in frags1:
        if name_frag1 in name:
            continue
        else:
            frags2.add(name)

all_frags = list(frags1 | frags2)
all_frags.sort(key=lambda s: len(s))

print '+'*100
for name in all_frags:
    print name
