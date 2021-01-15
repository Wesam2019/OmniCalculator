#!/bin/python
import time
import datetime
import cgi
import cgitb
from math import sqrt

cgitb.enable()

print("Content-type: text/html")
print()
print("""
<!DOCTYPE html>
<html lang="de">
<head>
<title>Pythagoras</title>
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
unknown = form.getvalue("unknown")
side1 = form.getvalue("side1")
side2 = form.getvalue("side2")

try:
    float(side1)
    float(side2)
    possible_op = True
except:
    possible_op = False
    print("Type Error")

if possible_op:
    if unknown == "a":
        sideb = float(side1)
        sidec = float(side2)
        sidea = sqrt((sidec * sidec) - (sideb * sideb))
        print("""
        <div class="w-button">
        <p> Side a = : <strong>{0:.2f}</strong></p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> a<sup>2</sup> = c<sup>2</sup> - b<sup>2</sup>
        <br/><br/>
        </p>
        </div>
        """.format(sidea))
    elif unknown == "b":
        sidea = float(side1)
        sidec = float(side2)
        sideb = sqrt((sidec * sidec) - (sidea * sidea))
        print("""
        <div class="w-button">
        <p> Side b = : <strong>{0:.2f}</strong></p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> b<sup>2</sup> = c<sup>2</sup> - a<sup>2</sup>
        <br/><br/>
        </p>
        </div>
        """.format(sideb))

    elif unknown == "c":
        sidea = float(side1)
        sideb = float(side2)
        sidec = sqrt((sidea * sidea) + (sideb * sideb))
        print("""
        <div class="w-button">
        <p> Side c = : <strong>{0:.2f}</strong></p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> c<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup>
        <br/><br/>
        </p>
        </div>
        """.format(sidec))
    else:
        print("""
        <div class="stylo">
        <p> You are a genius, you got past the html5 <br/>
        required attribute, but nothing can be calculalted
        <br/><br/> </p>
        </div>
        """)
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
