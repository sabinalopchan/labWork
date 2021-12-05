# convert seconds to day, hours, minutes and seconds
s=int(input("enter the value of second:"))
day=(((s/60)/60)/24)
print(f"total day for given second:{day}")
hour=((s/60)/60)
print(f"total hour for given second:{hour}")
minutes=(s/60)
print(f"total minutes for given second:{minutes}")
