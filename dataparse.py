from bs4 import BeautifulSoup
import os
import simplejson


def parse_it(filename):
    f = open(filename, 'r')
    soup = BeautifulSoup(f, 'html.parser')

    constituency = soup.find_all('h1')[0].string.strip()

    candidates_raw = []

    for child in soup.find_all('tbody')[1].children:
        if child.name:
            candidates_raw.append(child)

    party_names = []
    candidate_names = []
    votes = []
    share = []
    percent_change = []

    for candidate in candidates_raw:
        party_names.append(candidate.find_all('p')[1].string.strip())
        candidate_names.append(
            candidate.find_all('span')[3].string.strip())
        votes.append(candidate.find_all('span')[5].string.strip())
        share.append(candidate.find_all('span')[7].string.strip())
        percent_change.append(
            candidate.find_all('span')[9].string.strip())

    turnout_raw = soup.find_all('div')[88]
    turnout = turnout_raw.find_all('span')[3].string.strip()

    # print(constituency)
    # print(turnout)
    # print(party_names)
    # print(candidate_names)
    # print(votes)
    # print(share)
    # print(percent_change)
    f.close()

    return (constituency, turnout, party_names, candidate_names, votes,
            share, percent_change)


def main():
    directoryname = 'C:/Users/Robert/PycharmProjects/ukelection2017'
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(directoryname):
        for filename in filenames:
            if filename.endswith('.html'):
                list_of_files[filename] = os.sep.join(
                    [dirpath, filename])

    dataset = []
    for i, file in enumerate(list_of_files):
        dataset.append(parse_it(file))

    outputfile = open('dataset.text', 'w')
    simplejson.dump(dataset, outputfile, indent='')
    outputfile.close()

if __name__ == '__main__':
    import sys

    sys.exit(main())
