import os
c =	1
d =	50
i =	1
while i <=	100:
	if (i%2)==0:
		c +=	1
		d -=	1
	a =	"#"*c
	b =	"*"*d
	os.system("clear")
	print("\n")
	if i <	100:
		n =	4
		print(f" {n}/5  : {a}{b}")
	else:
		n =	5
		print(f" {n}/5  : {a}{b}")
	i +=	1