# coding: utf-8
import re
from custom_libs.toth.acutes_filter import strip_non_text
from custom_libs.toth.toth import check_str_integrity
from six.who import NAMES
from six.who import SURNAMES
from six.when import SEMANA
from six.when import MESES
from six.where import ESTADOS
from six.where import MUNICIPIOS
from six.where import SIGLAS
from custom_libs.toth.stop_words.preposicoes import PREPOSICOES
from custom_libs.toth.stop_words.contracoes import CONTRACOES

REGEX_PHRASAL_PATTERN = r"[.,;:?!]"


def remove_extra_space(text):
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text


def clean_line(raw_line):
    line = unicode(raw_line.strip('\n').lower(), 'utf-8')
    line = remove_extra_space(line)
    return line


def find_relevant_sentences(text, context, strip_non_text_chars=True, break_phrases=False):
    sentences_found = []
    for raw_line in text:
        # Clean Line ----------------------------------------
        line = clean_line(raw_line)

        # Check if line still has text
        if line:
            if strip_non_text_chars:
                line = strip_non_text(line)
                line = remove_extra_space(line)

            line_splitter = line.lower().split()

            # Tokenize line ---------------------------------------------
            tokens = [token for token in line_splitter if check_str_integrity(token)]

            # Checking if it's not empty -------------------
            check = [t for t in tokens if t in context]

            if check:
                if break_phrases:
                    for p in re.split(REGEX_PHRASAL_PATTERN, raw_line.strip('\n')):
                        if [f for f in p]:
                            sentences_found.append(p.strip('\n'))
                else:
                    sentences_found.append(raw_line.strip('\n'))

    return sentences_found


def find_names(file_content):
    names_found = find_relevant_sentences(file_content, NAMES)

    # process sentences
    names_matched = []
    for sentence in names_found:

        # Breaking into phrases phrases
        for phrase in re.split(REGEX_PHRASAL_PATTERN, sentence):

            # Clean Up
            phrase = phrase.replace('\n', ' ')
            phrase = phrase.replace('\r', ' ')
            phrase_unicode = unicode(phrase.strip('\n').lower(), 'utf-8')

            # Checking relevance
            check = [t for t in phrase_unicode.split() if t in NAMES]
            if check:

                # Tokenizing
                tokens = [w for w in phrase_unicode.strip().lower().split()
                          if w in NAMES or w in SURNAMES]

                # Acceptance Logic
                while tokens and (tokens[0] in PREPOSICOES or tokens[0] in CONTRACOES or tokens[0] == "e"):
                    tokens = tokens[1:]
                while tokens and (tokens[-1] in PREPOSICOES or tokens[-1] in CONTRACOES or tokens[-1] == "e"):
                    tokens = tokens[:-1]

                # Checking if is not empty
                if len(tokens) > 1:
                    names_matched.append(tokens)

    # data is ready
    names_matched_sorted = [" ".join(names) for names in names_matched]
    names_matched_sorted = list(set(names_matched_sorted))
    names_matched_sorted.sort(key=lambda s: len(s))
    return names_matched_sorted


def generic_clean(text):
    clean_text = text.replace("""\\n""", '')
    lines = re.split(REGEX_PHRASAL_PATTERN, clean_text)
    lines = [w.lower().split(' ') for w in lines]
    return lines


def match_dates_and_hours(line):
    return (re.match(r".+?[0-9]+?[/h:]([0-9]+?)?.+?", unicode(line, 'utf-8')) is not None
            or re.match(r".+?[0-9]+?([/][0-9]+?)+.+?", unicode(line, 'utf-8')) is not None)


def find_dates(content):
    date_context = SEMANA.copy()
    date_context.update(MESES)
    sentences = find_relevant_sentences(content, date_context, strip_non_text_chars=False)

    # find hours and dates with regex
    for line in content:
        for phrase in re.split(REGEX_PHRASAL_PATTERN, line):
            if match_dates_and_hours(phrase):
                sentences.append(phrase)

    found_date_frags = set()
    for sentence in sentences:
        for phrase in re.split(REGEX_PHRASAL_PATTERN, sentence.lower()):
            if [f for f in phrase.strip('\n').split() if f in date_context or match_dates_and_hours(f)]:
                found_date_frags.add(phrase.strip('\n').strip())

    found_date_frags = list(found_date_frags)
    found_date_frags.sort(key=lambda s: len(s))
    return found_date_frags


def find_places(content):
    places_context = ESTADOS.copy()
    places_context.update(MUNICIPIOS)
    places_context.update(ESTADOS)

    places = set()
    for s in content:
        s = s.lower()
        place_found = []
        for k in places_context.keys():
            if re.search(r"\b"+k+r"\b", unicode(s, 'utf-8'), re.UNICODE) is not None:
                place_found.append(k)
        if place_found:
            place_found.sort(key=lambda i: len(i))
            places.add(place_found[-1])
    places = list(places)
    places.sort(key=lambda i: len(i))
    return places
