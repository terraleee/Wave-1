secondsperday = 86400
secondsperhour = 3600
secondsperminute = 60

seconds = int(input("Enter the number of seconds: "))

days = seconds // secondsperday
seconds = seconds % secondsperday

hours = seconds // secondsperhour
seconds = seconds % secondsperhour

minutes = seconds // secondsperminute
seconds = seconds % secondsperminute

print("The equivalent amount of time is ", days,":",hours,":",minutes,":",seconds, sep="")