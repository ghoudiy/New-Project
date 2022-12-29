for i in range(int(input())):
	a,b,c = sorted(map(int, input().split()))
	if c == a + b:
		print("YES")
	else:
		print("NO")
	# print(["NO", "YES"][c == a + b]) # Nice One
