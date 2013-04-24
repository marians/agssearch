# encoding: utf-8

from .. import agssearch


def test_is_valid_ags():
    assert agssearch.is_valid_ags('01234567') == True


def test_is_valid_ags2():
    assert agssearch.is_valid_ags('0123_567') == False


def test_is_valid_ags3():
    assert agssearch.is_valid_ags('0123456') == False


def test_koeln():
    result = agssearch.search('Köln')
    assert result[0]['ags'] == '05315000'


def test_bonn():
    result = agssearch.search('bonn')
    assert len(result) > 1
    assert result[0]['ags'] == '05314000'


def test_bonn_ags():
    result = agssearch.lookup('05314000')
    assert type(result) == dict
    assert 'Bonn' in result['name']
