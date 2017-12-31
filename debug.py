#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from budshome.settings import gaiding

if __name__ == "__main__":
    gaiding.config.LOGO = None
    gaiding.run(host="0.0.0.0", workers=1, port=5555, debug=True)
