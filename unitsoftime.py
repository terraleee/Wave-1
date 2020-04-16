secondsperday = 86400
secondsperhour = 3600
secondsperminute = 60

days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

day = days * secondsperday

hour = hours * secondsperhour

minute = minutes * secondsperminute

print("This duration of time is", day + hour + minute + seconds, "seconds long.")