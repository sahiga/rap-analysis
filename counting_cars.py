#!/usr/bin/env python

import nltk, re, urllib2, os
from bs4 import BeautifulSoup, SoupStrainer

def clean_wikilist(filename):
    # open saved html file
    html = open(filename).read()
    
    # collect bulleted items only
    bullets = SoupStrainer("li")

    # make soup out of the bulleted items
    soup = BeautifulSoup(html, 'lxml', parse_only = bullets).prettify()

    # remove html from soup
    raw = nltk.clean_html(soup)

    # remove extra lines
    raw = re.sub(r'\n \n \n \n \n', r'\n', raw)
    raw = re.sub(r'\n \n \n', r'\n', raw)

    # create and clean tokens
    tokens = raw.split('\n')
    tokens = [re.sub(r'^\s+(?=[\S]+)', r'', token) for token in tokens]
    tokens = [token for token in tokens if not re.findall(r'\[[0-9]+\]|\([\S\s]+[\(\)]?|^\s+$|^[\s\[\]\(\)0-9]+$', token)]
    tokens = list(set(tokens))

    return tokens
    
cars = ['bmw', 'chevy', 'benz']

#    for car in cars:

def autos_ge():
    # open saved html file
    html = open('autos-ge.html').read()

    # create soup object
    soup = BeautifulSoup(html)

    # select current major manufacturers
    majors = soup.select('span.mw-headline')
    majors = [w for w in majors if w.parent.parent.previous_sibling.contents[0]['id'] == 'Current_major_manufacturers']
    major_tokens = [nltk.clean_html(str(w)) for w in majors]
    major_tokens = [re.sub(r'\[\s\S\s\]', r'', token) for token in major_tokens]

    # select current minor manufacturers
    minors = soup.select('li')
    minors = [w for w in minors if w.parent.parent.previous_sibling.contents[0]['id'] == 'Current_minor_manufacturers']
    minor_tokens = [nltk.clean_html(str(w)) for w in minors]
    minor_tokens = [re.sub(r'\s\(\S+\)', r'', token) for token in minor_tokens]

    # combine lists
    tokens = list(set(minor_tokens + major_tokens))

    return tokens   

def autos_uk():
    html = open('autos-uk.html').read()
    soup = BeautifulSoup(html)
    mfrs = soup.select('li')
    mfrs = [w for w in mfrs if w.parent.previous_sibling.previous_sibling.string == 'Current manufacturers:']
    mfrs = [nltk.clean_html(str(w)) for w in mfrs]
    mfrs = [re.sub(r'\s\([\S\s]+\)', r'', token) for token in mfrs]
    return mfrs

def autos_us():
    html = open('autos-us.html').read()
    soup = BeautifulSoup(html)
    first = soup.find('li').contents[0]
    second = first.parent.next_sibling.next_sibling.contents[0]
    third = second.parent.next_sibling.next_sibling.contents[0]
    majors = [first, second, third]
    minors = soup.select('ul li ul li')
    major_tokens = [nltk.clean_html(str(w)) for w in majors]
    minor_tokens = [nltk.clean_html(str(w)) for w in minors]
    minor_tokens = [re.sub(r'\s\([\S\s]+\)|\[\s\S\s\]|\n\s[A-Za-z]+', r'', token) for token in minor_tokens]
    tokens = list(set(major_tokens + minor_tokens))
    return tokens


def write_autos(auto_list):
    with open('autos-clean.txt', 'a') as output_file:
        for word in auto_list:
            output_file.write("%s\n" % word)

def rap_search(auto_list):
    # search for each brand name
    for brand in auto_list:
        url = 'http://research.blackyouthproject.com/raplyrics/results/?all/1989-2009/' + word

        # save the search results page
        results_html = urllib2.urlopen(url).read()

        # save it as a file named after the brand
        results = word + '.html'

        with open(results, 'w') as results_file:
            results_file.write(results_html)

def count_rap_results():
    # for all html files in current directory
    for filename in os.listdir('.'):
        if filename.endswith('html'):

            # select song titles
            html = open(filename).read()
            soup = BeautifulSoup(html)
            songs = soup.select('.title')

            # count number of song titles
            count = len(songs)
        
            # write brand names and number of songs into a text file
            with open('count_rap_autos.txt', 'a') as counter_file:
                counter_file.write('%s%15d\n' % (filename[:-5], count))
