# write a programe that will ask for a number of days and then will show how many hours, minutesand seconds are in that number of days 
y = float(input("how many years? "))

d = y *360
h = d *24
m = h *60
s = m *60

print(y, "years is:")
print(d, "days")
print(h, "hours")
print(m, "minutes")
print(s, "second")