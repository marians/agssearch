agssearch
=========

Python client for the official German directory of cities by DeStatis, called "[Gemeindeverzeichnis](https://www.destatis.de/gv/)". Allows you to look up the official city key ("Amtlicher Gemeindeschluessel", in brief: AGS) for a city name and vice versa.

Note that the AGS is still in common use, but to be replaced by the "Regionalschluessel" (RS). Read more in the German Wikipedia page [Amtlicher Gemeindeschluessel](http://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel).

## Install

    pip install agssearch

## Use in your code

### Finding the AGS for a city:

```python
>>> import agssearch.agssearch as ags
>>> result = ags.search("Bonn")
>>> for r in result:
>>>     print r['ags'], r['name']

05314000 Stadt Bonn
08337022 VVG der Stadt Bonndorf im Schwarzwald
08337022 Stadt Bonndorf im Schwarzwald
```

### Look up an AGS:

```python
>>> import agssearch.agssearch as ags
>>> result = ags.lookup("05314000")
>>> if result is not None:
>>>     print result['ags'], result['name']

05314000 Stadt Bonn
```

## Use as command line client

    $ agssearch Bonn
    [05314000] Stadt Bonn, Bonn, Stadt, Nordrhein-Westfalen
    [08337022] VVG der Stadt Bonndorf im Schwarzwald, Waldshut, Baden-Wuerttemberg
    [08337022] Stadt Bonndorf im Schwarzwald, Waldshut, Baden-Wuerttemberg

    $ agssearch 05314000
    [05314000] Stadt Bonn, Bonn, Stadt, Nordrhein-Westfalen

## Like agssearch?

Feel free to [tip me](https://www.gittip.com/marians/)!
