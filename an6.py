
import os


sp1 =	" "*19
sp2 =	" "*16
full =	"*"*59
msg =	f'''

{full}


{sp1}All Process Are Done
 {sp2}Please Restart Your Termux


{full}


Press Enter To Continue :
'''

new =	""
for i in msg:
	new =	new+i
	os.system("clear")
	print(new)
	
ex =	input("")
os.system("clear")