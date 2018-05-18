#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

if __name__ == '__main__':
    app.run(host='10.55.169.10', port=80, debug=True)
