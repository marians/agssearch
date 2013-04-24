agssearch
=========

Python client for the German Destatis [Gemeindeverzeichnis](https://www.destatis.de/gv/). Allows you to find the "Amtlicher Gemeindeschlüssel" for a location.

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

## Use as client

    python -m agssearch.agssearch Bonn
    [05314000] Stadt Bonn, Bonn, Stadt, Nordrhein-Westfalen
    [08337022] VVG der Stadt Bonndorf im Schwarzwald, Waldshut, Baden-Württemberg
    [08337022] Stadt Bonndorf im Schwarzwald, Waldshut, Baden-Württemberg

    python -m agssearch.agssearch 05314000
    [05314000] Stadt Bonn, Bonn, Stadt, Nordrhein-Westfalen
