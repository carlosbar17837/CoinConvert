#Program to Convert USD to HNL 

usdollaramt = input ("How many US Dollars do you have?")
usdollaramt = float(usdollaramt)
usdtolempiras = 24.5806
conversion = usdollaramt * usdtolempiras
# 1400conversion = round(conversion, 2)
conversion = str(conversion)
print ("You have L." + conversion + " Lempiras")
  