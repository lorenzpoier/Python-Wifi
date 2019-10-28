'''
Test File für funktionen
test files enden immer mit "_test" damit die Files übersichtlich zu den zugehörigen Funktionen gespeichert sind
pip install pytest installiert die bibliothek
'''

import pytest
import funktionen

#funktionen die testen müssen mit "test_" beginnen
def test_add():
    assert funktionen.addiere(3,4) == 7
    a = [
            [2,3,5],
            [-1002,3, -999],
            ]
            
    for c in a:
        assert funktionen.addiere(c[0], c[1]) == c[2]



