from bs4 import BeautifulSoup
import requests


def give_me_soup(url):
    cooked_soup = ''  # the finished html soup
    r = requests.get(url)  # get raw html file
    # start the soup, this first soup is no good because of bad flavor
    uncooked_soup = BeautifulSoup(r.text, 'html.parser')
    # for every character in the html file, disregard 'bad' characters
    for char in uncooked_soup.prettify():
        if char == '\u2212':
            continue
        elif char == '\u2013':
            continue
        elif char == '\xa9':
            continue
        elif char == '\U0001f602':
            continue
        elif char == '\U0001f913':
            continue
        elif char == '\U0001f30a':
            continue
        elif char == '\ufffd':
            continue
        else:
            cooked_soup += char
    # save the cooked soup
    f = open(url[-9:]+'.html', 'w')
    f.write(cooked_soup)
    f.close()
    f = open(url[-9:]+'.html', 'r')
    # reload the soup for return
    cooked_soup = BeautifulSoup(f, 'html.parser')
    f.close()
    return cooked_soup


# parse web-pages from start to end
def mass_parser(base, soup_list, header, start, end, digits):
    # helps line up the urls, numbers need correct amnt of leading zeros
    digit_format_string = '{:0' + str(digits) + 'd}'
    for i in range(end-start+1):
        url = base + header + digit_format_string.format(start+i)
        soup_list.append(give_me_soup(url))


def main():
    soups = []
    url_base = "http://www.bbc.com/news/politics/constituencies/"

    wales = "W070000"
    wales_start = 41
    wales_end = 80
    scotland = "S140000"
    scotland_start = 1
    scotland_end = 59
    england = "E1400"
    england_start = 530
    england_end = 1062
    ni = "N060000"
    ni_start = 1
    ni_end = 18

    mass_parser(url_base, soups, wales, wales_start, wales_end, 2)
    mass_parser(url_base, soups, scotland, scotland_start,
                scotland_end, 2)
    mass_parser(url_base, soups, ni, ni_start, ni_end, 2)
    mass_parser(url_base, soups, england, england_start, england_end, 4)

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main())
