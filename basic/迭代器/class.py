#!/usr/bin/python3

class MyNumber:
    def _iter_(self):
        self.a = 1
        return self

    def _nex_(self):
        x = self.a
        self.a += 1
        return x
