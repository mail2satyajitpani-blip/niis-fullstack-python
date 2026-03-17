"""wap take a string from keyboard count no of (char,alphabet,lower,upper,vowel,consonant,digit,space,sy,word)"""
print("Enter a string")
s=input()
c,alp,lw,up,v,co,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i in s:
	c=c+1
	if i.isalpha():
		alp=alp+1
		if i.islower():
			lw=lw+1
		else:
			up=up+1
		if i in "aeiouAEIOU":
			v=v+1
		else:
			co=co+1
	elif i.isdigit():
		dg=dg+1
	elif i.isspace():
		sp=sp+1
	else:
		sy=sy+1
wd=sp+1
print("no of char=",c)
print("no of alphabet=",alp)
print("no of vowel=",v)
print("no of consonant=",co)
print("no of lower case=",lw)
print("no of upper case=",up)
print("no of space=",sp)
print("no of digit=",dg)
print("no of special symbol=",sy)
print("no of wd=",wd)