from operator import itemgetter
import csv
FNAME = 'static/Most-Recent-Cohorts-Scorecard-Elements.csv'
#ZIPLOOKUP_FNAME = './static/data/districts.csv'


def get_schools():
    # Return list of dicts
    with open(FNAME, 'r', encoding="latin1") as f:
        newrows = []
        for row in csv.DictReader(f):
            newrows.append(row)
        return newrows


def filter_by_smallest(datarows):
    matches = []
    for c in datarows:
        if c['NPT4_PUB']!="NULL":
        	if int(c['NPT4_PUB']) < 5000:
        		matches.append(c)
    return matches



def filter_by_middle(datarows = ""):
    matches = []
    for c in datarows:
        # find all house members
        # that match given z['district'] and z['state']
        if c['NPT4_PUB']!="NULL":
        	if int(c['NPT4_PUB']) >= 5000 and int(c['NPT4_PUB']) < 10000:
        		matches.append(c)
    return matches

def filter_by_largest(datarows = ""):
    matches = []
    for c in datarows:
        if c['NPT4_PUB']!="NULL":
        	if int(c['NPT4_PUB']) >= 10000:
        		matches.append(c)
    return matches

