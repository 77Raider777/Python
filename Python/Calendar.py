def month(a,d):
		t=1
		a1=0
		if (a+d)%7==0:
			r1=(a+d)//7
		else:
			r1=(a+d)//7 +1
			
		m1=[["  " for i in range(7)] for j in range(7)]
		m1[0][0]="M"
		m1[0][1]="T"
		m1[0][2]="W"
		m1[0][3]="T"
		m1[0][4]="F"
		m1[0][5]="S"
		m1[0][6]="S"
		for i in range(1,r1+1):
			j=0
			while j<=6:
				if a!=0:
					m1[i][j]="  "
					a-=1
				elif t>d:
					m1[i][j]="  "
					a1+=1
				else:
					m1[i][j]=t
					t+=1
				j+=1
		a=7-a1
		return (m1,a)

def printc(m1,m2,m3):
		
		for i in range(len(m1)):
			for j in range(len(m1[0])):
				if j==6:
					if i==0:
						f=open("calender.txt","at")
						print(m1[i][j],end="        ",file=f)
						f.close()
					elif (type(m1[i][j])==int) and m1[i][j]<10:
						f=open("calender.txt","at")
						print(	m1[i][j],end="        ",file=f)
						f.close()
					else:
						f=open("calender.txt","at")
						print(m1[i][j],end="       ",file=f)
						f.close()
				elif i==0:
					f=open("calender.txt","at")	
					print(m1[i][j],end="  ",file=f)
					f.close()
				elif (type(m1[i][j])==int) and m1[i][j]<10:
					f=open("calender.txt","at")
					print(	m1[i][j],end="  ",file=f)
					f.close()
				else:
					f=open("calender.txt","at")
					print(m1[i][j],end=" ",file=f)
					f.close()
			for j in range(len(m1[0])):
				if j==6:
					if i==0:
						f=open("calender.txt","at")
						print(m2[i][j],end="        ",file=f)
						f.close()
					elif (type(m2[i][j])==int) and m2[i][j]<10:
						f=open("calender.txt","at")
						print(	m2[i][j],end="        ",file=f)
						f.close()
					else:
						f=open("calender.txt","at")
						print(m2[i][j],end="       ",file=f)
						f.close()
				elif i==0:
					f=open("calender.txt","at")	
					print(m2[i][j],end="  ",file=f)
					f.close()
				elif (type(m2[i][j])==int) and m2[i][j]<10:
					f=open("calender.txt","at")
					print(	m2[i][j],end="  ",file=f)
					f.close()
				else:
					f=open("calender.txt","at")
					print(m2[i][j],end=" ",file=f)
					f.close()
			for j in range(len(m1[0])):
				if i==0:
					f=open("calender.txt","at")
					print(m3[i][j],end="  ",file=f)
					f.close()
				elif (type(m3[i][j])==int) and m3[i][j]<10:
					f=open("calender.txt","at")
					print(	m3[i][j],end="  ",file=f)
					f.close()
				else:
					f=open("calender.txt","at")
					print(m3[i][j],end=" ",file=f)
					f.close()
			f=open("calender.txt","at")
			print("\n",file=f)
			f.close()
			
	

def printCalender(year):
	
		l=0
		f=False
		for i in range(1753,year):
			if i%4==0 and i%100 !=0:
				l+=2
			elif i%4 ==0 and i%400 ==0:
				l+=2
			else:
				l+=1
		a=l%7
		if year%4==0 and year%100 !=0:
			f=True
		elif year%4 ==0 and year%400 ==0:
			f=True
	
		(m1,a1)=month(a,31)
		if f==False:
			(m2,a2)=month(a1%7,28)
		else:
			(m2,a2)=month(a1%7,29)
		(m3,a3)=month(a2%7,31)
		(m4,a4)=month(a3%7,30)
		(m5,a5)=month(a4%7,31)
		(m6,a6)=month(a5%7,30)
		(m7,a7)=month(a6%7,31)
		(m8,a8)=month(a7%7,31)
		(m9,a9)=month(a8%7,30)
		(m10,a10)=month(a9%7,31)
		(m11,a11)=month(a10%7,30)
		(m12,a12)=month(a11%7,31)
		f=open("calender.txt","at")
		print("                                 " , year,file=f)
		f.close()
		j="-JANUARY-"
		j=j.center(21)
		f="-FEBRUARY-"
		f=f.center(21)
		m="-MARCH-"
		m=m.center(21)
		d=j + "   " + f + "       " + m + "      "
		f=open("calender.txt","at")
		print(d,file=f)
		f.close()
		printc(m1,m2,m3)
		j="-APRIL-"
		j=j.center(21)
		f="-MAY-"
		f=f.center(21)
		m="-JUNE-"
		m=m.center(21)
		e=j + "   " + f + "       " + m + "      "
		f=open("calender.txt","at")
		print(e,file=f)
		f.close()
		printc(m4,m5,m6)
		j="-JULY-"
		j=j.center(21)
		f="-AUGUST-"
		f=f.center(21)
		m="-SEPTEMBER-"
		m=m.center(21)
		i=j + "   " + f + "       " + m + "      "
		f=open("calender.txt","at")
		print(i,file=f)
		f.close()
		printc(m7,m8,m9)
		j="-OCTOBER-"
		j=j.center(21)
		f="-NOVEMBER-"
		f=f.center(21)
		m="-DECEMBER-"
		m=m.center(21)
		k=j + "   " + f + "       " + m + "      "
		f=open("calender.txt","at")
		print(k,file=f)
		f.close()
		printc(m10,m11,m12)


		

