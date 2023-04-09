#Initial Inputs + Fancy error handling
try:
  layers = int(input("How many layers: "))
  pTime = int(input("How much prep time: "))
  cTime = int(input("How much cooldown time: "))
except ValueError:
      print("Oops! Make sure you type a whole minute!\n(The error below this is intended)")
      quit() 

#Time maths (Probably how you wanted this?)
finalPTime = pTime * layers
finalTime = finalPTime + cTime
finalTimeSimpl = finalTime

#General maths 
price = (layers / 2) * 20
LPH = 60 / finalTimeSimpl 
PPY = (price * LPH) * 8760

#Outputs
print()
print("Lasagna per hour is: " + str(int(LPH)))
print("Price per day is: $" + str(int(PPY)))
