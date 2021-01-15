#!/bin/python
import time
import datetime
import cgi
import cgitb
import math
import cmath

cgitb.enable()

print("Content-type: text/html")
print()
print("""
<!DOCTYPE HTML>
<html lang="de">
<head>
<title>Quadratic Equation</title>
<meta name="viewport" content="initial-scale = 0.5">
<link rel="stylesheet" type="text/css" href="../css/theme.css">
</head>
<body>
<div class="header">
<div class="image">
<a href="https://www.th-brandenburg.de/startseite/" target="_blank">
<img class="img1-container" src="../img/THB_Logo.svg" alt="THB_Logo"
height="100">
</a>
</div>
<div class="text">
<h2><span>Quadratic Equation</span></h2>
</div>
</div>
<nav>
<ul>
<li> <a href="../index.html" class="dropbtn">Home</a>
</li>
<li class="dropdown">
<a href="../Mathematical.html" class="dropbtn">Mathematical</a>
<div class="dropdown-content">
<a href="../Quadratic_Equation.html">Quadratic Equation</a>
<a href="../Pythagoras.html">Pythagoras Theorem</a>
</div>
</li>
<li class="dropdown">
<a href="../Medical.html" class="dropbtn">Medical</a>
<div class="dropdown-content">
<a href="../Body_Mass_Index.html">Body Mass Index</a>
<a href="../Daily_Calories.html">Daily Calories</a>
</div>
</li>
</ul>
</nav>
<br/>
<br/>
""")

form = cgi.FieldStorage()
a = form.getvalue("a")
b = form.getvalue("b")
c = form.getvalue("c")

try:
    float(a)
    float(b)
    float(c)
    possible_op = True
except:
    possible_op = False
    print("Type Error")

if possible_op:
    discrim = (float(b)**2) - (4*float(a)*float(c))
    x1 = (-(float(b)) - cmath.sqrt(discrim)) / (2*float(a))
    x2 = (-(float(b)) + cmath.sqrt(discrim)) / (2*float(a))
    if not isinstance(x1, complex) and not isinstance(x2, complex):
        x3 = (-(float(b)) - math.sqrt(discrim)) / (2*float(a))
        x4 = (-(float(b)) + cmath.sqrt(discrim)) / (2*float(a))
        print("""
        <div class="w-button">
        <p> Real solution are: <br/> <strong>x1 = {0}</strong><br/>
        <strong>x2 = {1}</strong><br/>
        </p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> x = ( -b &plusmn; &radic; (b - 4 &sdot; a &sdot; c ) )
        / ( 2 &sdot; a)
        <br/><br/>
        </p>
        </div>
        """.format(x3, x4))

    else:
        print("""
        <div class="w-button">
        <p> Imaginary solution are: <br/> <strong>x1 = {0}</strong><br/>
        <strong>x2 = {1}</strong><br/>
        </p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> x = ( -b &plusmn; &radic; (b - 4 &sdot; a &sdot; c ) )
        / ( 2 &sdot; a)
        <br/><br/>
        </p>
        </div>
        """.format(x1, x2))
print("""
<br/><br/>
<footer>
<nav>
<ul>
<li> <a href="https://informatik.th-brandenburg.de/~alshaiba/" target="_blank">
Copyright &#x24B8; 2018 Wesam Al-Shaibani</a>
</li>
<li> <a href="https://pixabay.com/de/" target="_blank">
Photos are copyright free </a>
</li>
</ul>
</nav>
</footer>
</body>
</html>
""")
