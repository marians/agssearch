# encoding: utf-8

import sys
import mechanize
from lxml import etree
from StringIO import StringIO


def submit_form(key, value):
    """
    Submits the search form and returns HTML.
    key: Name of the input field to use ("ags" or "gemeinde").
    value: search term (UTF-8)
    """
    browser = mechanize.Browser()
    browser.open('https://www.destatis.de/gv/')
    browser.select_form(name="Formular")
    browser[key] = value.decode('utf-8').encode('latin-1')
    response = browser.submit()
    html = response.get_data()
    return html


def parse_result(html):
    """
    Parses the result page and returns structured data
    """
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)
    n = -1
    items = []
    for row in tree.xpath('//tr'):
        label = None
        value = None
        for td in row.xpath('./td'):
            if label is None:
                label = td.text
                if label == 'Stand':
                    n += 1
            else:
                value = td.text.strip()
        if n >= 0:
            if len(items) < (n + 1):
                items.append({})
            if label is not None and value is not None and value != '':
                items[n][label] = value
    results = []
    for item in items:
        result = {}
        if 'Anschrift der Gemeinde' in item:
            result['name'] = item['Anschrift der Gemeinde']
        if u'Amtl.Gemeindeschl\xfcssel' in item:
            result['ags'] = item[u'Amtl.Gemeindeschl\xfcssel']
        if 'Bundesland' in item:
            result['state'] = item['Bundesland']
        if 'Einwohner gesamt' in item:
            result['population'] = int(item['Einwohner gesamt'].replace(' ', ''))
        if 'Gemeindetyp' in item:
            result['type'] = item['Gemeindetyp']
        if 'Kreisname' in item:
            result['county'] = item['Kreisname']
        if 'Regierungs-Bezirk' in item:
            result['district'] = item['Regierungs-Bezirk']
        if u'Fl\xe4che km2' in item:
            result['area'] = float(item[u'Fl\xe4che km2'].replace(' ', '').replace(',', '.'))
        results.append(result)
    return results


def search(term):
    """
    Search for a city name and return a list of matching dicts
    """
    html = submit_form('gemeinde', term)
    results = parse_result(html)
    return results


def lookup(ags):
    """
    Look up an AGS string and return the matching dict or None
    """
    html = submit_form('ags', ags)
    results = parse_result(html)
    if results == []:
        return None
    return results[0]


def is_valid_ags(string):
    """
    Check if string could be a valid AGS
    """
    if len(string) != 8:
        return False
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for letter in string:
        if letter not in digits:
            return False
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Search for a location')
    parser.add_argument('searchterm', metavar='TERM', type=str,
                   help='Name of the city, town, village OR an 8 digit Gemeindeschlüssel')
    args = parser.parse_args()

    if is_valid_ags(args.searchterm):
        r = lookup(args.searchterm)
        if r is None:
            sys.exit(1)
            print "AGS lookup for %s - no result" % args.searchterm
        else:
            print "[%s] %s, %s, %s" % (r['ags'], r['name'], r['county'], r['state'])
    else:
        res = search(args.searchterm)
        for r in res:
            print "[%s] %s, %s, %s" % (r['ags'], r['name'], r['county'], r['state'])

if __name__ == '__main__':
    main()
