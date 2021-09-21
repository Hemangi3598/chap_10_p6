# wapp to read two integers
# and find ans = n1 / n2

print("welcome")
try:
	n1 = int(input(" enter first integer "))
	n2 = int(input(" enter second integer "))
	ans = n1 / n2
	print("ans = ", ans)
except ValueError:
	print("integers only ")
except ZeroDivisionError:
	print(" 2nd interger should not be 0 ")
else:
	print("ans = ", ans)
print("bye")

# try with multiple except
# except + else