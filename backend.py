#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "MH 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Aditya Jain
    License No : 12345677362
    Make / Model : AUDI / Q7
    Registration Date : 1/12/2019
    Registering Authority : AGRA , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1234732
    Chassis No : HMSURVWHFSSDE
    Insurance Upto : 5/13/2025
    Fitness Upto : 4/8/2040
    </pre>''')
    print("</body>")

elif plate_no == "UP 82 AB 0612":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Aditya Jain
    License No : 098363357292
    Make / Model : SUZUKI / BALENO
    Registration Date : 1/12/2014
    Registering Authority : AGRA, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1733721
    Chassis No : HMSURVWVIWQNQ
    Insurance Upto : 5/13/2025
    Fitness Upto : 4/8/2045
    </pre>''')
    print("</body>")

elif plate_no == "MH 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Ramesh Pal
    License No : 735382528936
    Make / Model : MARUTI SUZUKI / ALTO800
    Registration Date : 1/12/2014
    Registering Authority : BIHAR, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
