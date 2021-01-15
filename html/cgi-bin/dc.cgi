#!/bin/python
import time
import datetime
import cgi
import cgitb
import cmath

cgitb.enable()

print("Content-type: text/html")
print()
print("""
<!DOCTYPE html>
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
w = form.getvalue("w")
a = form.getvalue("a")
gender = form.getvalue("gender")

try:
    float(w)
    int(a)
    possible_op = True
except:
    possible_op = False
    print("Type Error")

if possible_op:
    if int(a) <= 9 and int(a) >= 3:
        if gender == "male":
            cal = 22.7 * float(w)
            calories = cal + 495.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption: <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Males: Age 3 to 9 years = 22.7 x (Weight in kg) + 495
            <br/><br/>
            Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
        else:
            cal = 22.5 * float(w)
            calories = cal + 499.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption: <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Females: Age 3 to 9 years = 22.5 x (Weight in Kg) + 499
            <br/><br/>
            Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
    elif int(a) <= 17 and int(a) >= 10:
        if gender == "male":
            cal = 17.5 * float(w)
            calories = cal + 651.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption: <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Males: Age 10 to 17 years = 17.5 x (Weight in Kg) + 651
            <br/><br/>
            Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
        else:
            cal = 12.2 * float(w)
            calories = cal + 746.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption: <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Females: Age 10 to 17 years = 12.2 x (Weight in Kg) + 746
            <br/><br/>
            Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
    elif int(a) <= 29 and int(a) >= 18:
        if gender == "male":
            cal = 15.3 * float(w)
            calories = cal + 679.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption : <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Males: Age 18 to 29 years = 15.3 x (Weight in kg) + 679
            <br/><br/>
            Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
        else:
            cal = 14.7 * float(w)
            calories = cal + 496.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption : <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Females: Age 18 to 29 years = 14.7 x (Weight in kg) + 496
            <br/><br/>
            <p> Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
    elif int(a) <= 60 and int(a) >= 30:
        if gender == "male":
            cal = 11.6 * float(w)
            calories = cal + 879.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption : <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Males: Age 30 to 60 years = 11.6 x (Weight in kg) + 879
            <br/><br/>
            <p> Based on the World Health Organization Equation <br/><br/></p>
            </div>
            """ % {"calories": calories})
        else:
            cal = 8.7 * float(w)
            calories = cal + 829.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption : <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Females: Age 30 to 60 years = 8.7 x (Weight in kg) + 829
            <br/><br/>
            <p> Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
    elif int(a) > 60:
        if gender == "male":
            cal = 13.5 * float(w)
            calories = cal + 487.0
            print("""
            <div class="w-button">
            <p> Your average daily energy consumption : <strong>%(calories).2f
            </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> Males: Age over 60 years = 13.5 x (Weight in kg) + 487
            <br/><br/>
            <p> Based on the World Health Organization Equation <br/><br/> </p>
            </div>
            """ % {"calories": calories})
    else:
        print("""
        <div class="stylo">
        <p> Your cannot calculate the calories of someone under 3 years old!
        <br/><br/>
        Based on the World Health Organization Equation <br/><br/> </p>
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
