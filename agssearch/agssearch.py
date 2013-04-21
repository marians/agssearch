# encoding: utf-8

import mechanize
from lxml import etree
from StringIO import StringIO


def search(term):
    browser = mechanize.Browser()
    browser.open('https://www.destatis.de/gv/')
    browser.select_form(name="Formular")
    browser["gemeinde"] = term.decode('utf-8').encode('latin-1')
    response = browser.submit()
    html = response.get_data()
    html.decode('latin-1').encode('utf-8')
    #print html
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


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Search for a location')
    parser.add_argument('location', metavar='LOCATION', type=str,
                   help='Name of the city, town, village, ...')
    args = parser.parse_args()
    res = search(args.location)
    for r in res:
        print "[%s] %s, %s, %s" % (r['ags'], r['name'], r['county'], r['state'])
