#!/usr/bin/python3
# -*- coding: utf-8 -*-

def baseHTML(title,body):
    content=("""<!DOCTYPE html>
<html>
        <head>
                <title>"""+ title +"""</title>
                <meta charset="UTF-8">
                <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>"""+ body +"""</body>
</html>

            """)
    return content
