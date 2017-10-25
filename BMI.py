import sys
if len (sys.argv) !=3:
    print ("Zła liczna argumentów, podaj 2 argumenty")
else:
    a=int(sys.argv[1]) #masa ciała w kg
    b=int(sys.argv[2]) #wzros w cm
    c=a/(b**2)
    print ("BMI wynosi %.1f" % c)
