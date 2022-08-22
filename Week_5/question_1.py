l = []
print("Enter a number (0 to exit):")
while True:
	n = int(input())
	if n == 0:
		break
	l.append(n)
l = sorted(l)
print(l)