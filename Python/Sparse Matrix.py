class Matrix:
# constructor
	def __init__(self,C):
		self.C=C.copy()
# __str__ method
	def __str__(self):
		n=len(self.C)
		m=len(self.C[0])
		l=""
		for i in range(n):
			for j in range(m):
# storing in l
				l=l+str(self.C[i][j])+" "
# changing line
			l= l +"\n"
		return l
# addition method
	def __add__(self,r):
		A=self.C
		B=r.C
		n=len(A)
		m=len(A[0])
# adding corresponding elements
		C=[[A[i][j]+B[i][j] for j in range(m)] for i in range(n)]
		return Matrix(C)
# subtraction method
	def __sub__(self,r):
		A=self.C
		B=r.C
		n=len(A)
		m=len(A[0])
# subtracting elements
		C=[[A[i][j]-B[i][j] for j in range(m)] for i in range(n)]
		return Matrix(C)
# multiplication method
	def __mul__(self,r):
		if isinstance(r,Matrix):
# multiplication of matrices
			A=self.C
			B=r.C
			n=len(A)
			l=len(A[0])
			m=len(B[0])
# defining C
			C=[[0 for i in range(m)] for j in range(l)]
# logic of multiplication
			for a in range(n):
				for b in range(m):
					for k in range(l):
						C[a][b]+=A[a][k]*B[k][b]
		else:
# multiplication of scalars
			A=self.C
			n=len(A)
			l=len(A[0])
			C=[[A[i][j]*r for j in range(l)] for i in range(n)]
		return Matrix(C)
# toSparse method
	def toSparse(self):
		ans=[]
		c=[]
		s=self.C.copy()
		n=len(s)
		m=len(s[0])
# eliminating the 0 elements and adding rest element to c as tuples 
		for i in range(n):
			c=[]
			for j in range(m):
				if s[i][j]!=0:
					q=(j,s[i][j])
					c=c+[q]
# appending c to ans
			ans=ans+[c]
		return SparseMatrix(ans,n,m)

class SparseMatrix:
# constructor
	def __init__(self,sparse_matrix,nrows,ncols):
		self.sparse_matrix=sparse_matrix.copy()
		self.nrows=nrows
		self.ncols=ncols
# __str__ method
	def __str__(self):
		s=self.sparse_matrix.copy()
		n=self.nrows
		m=self.ncols
		ans=""
		for i in range(n):
			x=s[i]
			a=len(x)
			b=1
			k=0
			for j in range(m):
				if b<=a:
					(c1,c2)=x[k]
					if c1==j:
# storing value of second element of tuple
						ans=ans+str(c2)+" "
						k+=1
						b+=1
# storing 0
					else:
						ans=ans+str(0)+ " "

				else:
# storing 0
					ans=ans+str(0) +" "
# changing line
			ans=ans+"\n"
		return ans
# addition
	def __add__(self,r):
		a1=self.sparse_matrix.copy()
		a2=r.sparse_matrix.copy()
		n=r.nrows
		m=r.ncols
		ans=[]
		c=[]
		for i in range(n):
# extracting rows of both matrices
			x=a1[i]
			y=a2[i]
			l1=len(x)
			l2=len(y)
			k1=0
			c=[]
# if anyone of the row is empty then sum is the value of other row
			if l1==0:
				c=y
			elif l2==0:
				c=x
			else:
# finding the corresdponding elements and adding them
				for j in range(m):
					if (k1+1)<=l1:
						(d1,d2)=x[k1]
						d4=0
						match=False
						if d1==j:
							k1+=1
							for u in range(l2):
								(d3,d4)=y[u]
								if d1==d3:
									match=True
									break
						else:
							for u in range(l2):
								(d3,d4)=y[u]
								if d3==j:
									d2=0
									d1=d3
									match=True
									break
						d5=d2+d4
						if d5 != 0:
							if match:
								q=(d1,d5)
								c=c+[q]
							else:
								q=(d1,d2)
								c=c+[q]
								
								
					else:
						match=False
						for u in range(l2):
								(d3,d4)=y[u]
								if d3==j:
									match=True
									break
						if match:
							q=(d3,d4)
							c=c+[q]
#appending c to ans					
			ans=ans+[c]
		
		return SparseMatrix(ans,n,m)
# subtraction
	def __sub__(self,r):
# multiplication by -1 and then addition
		z=r*(-1)
		a=self+z
		return a
# multipliacation					
	def __mul__(self,r):
		s1=self.sparse_matrix.copy()
		n=self.nrows
		l=self.ncols
		ans=[]
		c=[]
		if isinstance(r,SparseMatrix):
# multiplication of matrices
			s2=r.sparse_matrix.copy()
			m=r.ncols
			k1=0
# extracting the row and then finding and multiplying corresponding column elements to get c
			for k in range(n):
				x=s1[k]
				l0=len(x)
				c=[]
				for i in range(m):
					k1=0
					f=0
					for j in range(l):
						if k1<l0:
							(d1,d2)=x[k1]
							y=s2[d1]
							if len(y)!= 0:
								for o in y:
									(d3,d4)=o
									if d3==i:
										f=f+d2*d4
										break
							k1+=1
						else:
							break
					if f!=0:
						q=(i,f)
						c=c+[q]
					else:
						c=[]
# appending c to ans
				ans=ans+[c]
			return SparseMatrix(ans,n,m)

				
		else:
# multiplication by scalar
			for i in range(n):
				c=[]
				x=s1[i]
				for j in range(len(x)):
					(d1,d2)=x[j]
					q=(d1,d2*(r))
					c=c+[q]
				ans=ans+[c]
			return SparseMatrix(ans,n,l)
# toDense method				
	def toDense(self):
		s=self.sparse_matrix
		n=self.nrows
		m=self.ncols
		print(s,n,m)
		ans=[]
		c=[]
# checking for elements and replacing empty spaaces with 0 to get the dense matrix
		for i in range(n):
			x=s[i]
			k=0
			c=[]
			l=len(x)	
			for j in range(m):
				if k<l:
					(d1,d2)=x[k]
					if d1==j:
						c=c+[d2]
						k+=1
					else:
						c=c+[0]
				else:
					c=c+[0]	
			ans=ans+[c]
		return Matrix(ans)

 


