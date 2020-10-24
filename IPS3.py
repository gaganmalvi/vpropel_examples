balance_end=float(input())
gndr=str(input())
gender=gndr.capitalize()
bonusforall=float(balance_end*0.02)
if gender == "M" :
    balance_start=float(bonusforall+balance_end)
elif gender == "F" :
    if balance_end > 5000:
        ext_bonus=float(balance_end*0.05)
        balance_start=float(ext_bonus+balance_end)
    else:
        balance_start=float(bonusforall+balance_end)
else:
    print ("Wrong input")
print(format(balance_start,'.2f'))
