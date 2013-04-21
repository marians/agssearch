# encoding: utf-8

from .. import agssearch


def test_koeln():
    result = agssearch.search('Köln')
    assert result[0]['ags'] == '05315000'


def test_bonn():
    result = agssearch.search('bonn')
    assert len(result) > 1
    assert result[0]['ags'] == '05314000'
