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
h = form.getvalue("h")
a = form.getvalue("a")
gender = form.getvalue("gender")

try:
    float(w)
    float(h)
    int(a)
    possible_op = True
except:
    possible_op = False
    print("Type Error")

if possible_op:
    cal = float(h) / 100.0
    cal2 = cal * cal
    bmi = float(w)/cal2

    if int(a) <= 5 and int(a) >= 1:
        print("""
        <div class="w-button">
        <p> Your BMI is: <strong>%(bmi).2f </strong></p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
        Preschoolers(1-5): Normal-BMI lies between 13 and 17 <br/><br/>
        </p>
        </div>
        """ % {"bmi": bmi})
    elif int(a) <= 11 and int(a) >= 6:
        print("""
        <div class="w-button">
        <p> Your BMI is: <strong>%(bmi).2f </strong></p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
        Gradeschoolers(6-11): Normal-BMI lies between 14 and 19 <br/><br/>
        </p>
        """ % {"bmi": bmi})
    elif int(a) <= 18 and int(a) >= 12:
        print("""
        <div class="w-button">
        <p> Your BMI is: <strong>%(bmi).2f </strong></p>
        </div>
        <br/><br/>
        <div class="stylo">
        <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
        Teens(12-18): Normal-BMI lies between 16 and 24 <br/<br/>
        </p>
        </div>
        """ % {"bmi": bmi})
    elif int(a) <= 64 and int(a) >= 19:
        if gender == "male":
            print("""
            <div class="w-button">
            <p> Your BMI is: <strong>%(bmi).2f </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
            Young Males(19-64): Normal-BMI lies between 20 and 25
            <br/><br/>
            </p>
            </div>
            """ % {"bmi": bmi})
        else:
            print("""
            <div class="w-button">
            <p> Your BMI is: <strong>%(bmi).2f </strong></p>
            </div>
            <br/><br/>
            <div class="stylo">
            <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
            Young Females(19-64): Normal-BMI lies between 19 and 24
            <br/><br/>
            </p>
            </div>
            """ % {"bmi": bmi})
    elif int(a) >= 65:
        print("""
        <div class="w-button">
        <p>Your BMI is: <strong>%(bmi).1f </strong></p>
        </div>
        <br/>
        <div class="stylo">
        <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
        Elders(>64): Normal-BMI lies between 19 and 29 <br/><br/>
        </p>
        </div>
        """ % {"bmi": bmi})
    else:
        print("""
        <div class="stylo">
        <p> BMI = (Weight in Kg) / (Length in meters)<sup>2</sup><br/><br/>
        You cannot calculate the BMI of someone who isn't born yet!
        <br/><br/>
        </p>
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
