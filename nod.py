def mo_le(x, y):
	if x>y:
		return x, y
	else:
		return y, x

def nod(x,y):
	mo, le = mo_le(x, y)
	return le, mo % le

def main():
	x, y = list(map(int, input().split()))
	le, ost = nod(x, y)
	while ost > 0:
		le, ost = nod(le, ost)
						
	print(le)

main()	
