amount =int(input("enter your amount"))
notes500 = amount//500
amount =amount%500
notes200=amount//200
amount=amount%200
notes100=amount//100
print("500 notes =",notes500," ","200 notes =",notes200," ","100 notes =",notes100)