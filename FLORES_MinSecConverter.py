seconds = eval(input("Enter inter seconds: "))

minutes = seconds // 60
remainder_seconds = seconds % 60

print(seconds, "seconds is equivalent to", minutes, "minutes and", remainder_seconds, "seconds")