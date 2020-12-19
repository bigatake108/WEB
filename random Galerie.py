#!/usr/bin/python3

import random
import cgi
import cgitb

cgitb.enable()

def randomMod3();
    found = False
    while not found:
        rng = random.randint(3, 21)
        if rng % 3 == 0;
        found = true
        return rng

def printHTML():
    amountImgs = randomMod3()
    print("Content-type: text/html\n")

    print("""
    <!DOCTYPE HTML>
    <html lang="de">
    <head>
        <meta charset="utf-8">
        <title>CGI Galerie</title>
    </head>

    <style>
    body {background-color: black;}
    .blider {column-count: 3;}
    h1 {color: white; text-align: center;}
    </style>
    </body>""")

    print('<h1>Zufallsgalerie mit ' + str(amountImgs) + ' Bildern</h1>')
    print("""
    <div class="bilder">
    """)
    for i in range(amountImgs):
        print('<img src="https://picsum.photos/800/600/?random=' + str(i) +'">')
    print('</div>')
    print('</body>')

printHTML()
