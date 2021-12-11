class Student:
# constructor of class Student
	def __init__(self,entryNo,A):
		self.entryNo=entryNo
		self._A=A.copy()
# attempt method
	def attempt(self, courseCode, quizTitle, attemptedAnswers):
		x=self._A.copy()
# matching coursecode
		for course in x:
			if course.courseCode==courseCode:
				y=course
				break
		x=y._B.copy()
# finding required quiz
		for quiz in x:
			if quiz.title==quizTitle:
				z=quiz
				break
# checking whether it is first attempt or not
		if z.attempt==0:
			z.attempt=1
			a=z._C
			for i in range(len(attemptedAnswers)):
# calculating score
				if attemptedAnswers[i]==a[i]:
					z.score+=1
# getUnattemptedQuizzes method
	def getUnattemptedQuizzes(self):
		l=[]		
		x=self._A.copy()
# checking each quiz of every course
		for course in x:
			y=course._B.copy()
			for quiz in y:
# if attribute attempt=0 then quiz is unattempted
				if quiz.attempt==0:					
					b=(course.courseCode,quiz.title)
					f=[b]
					l=l+f						
		return l
# getAverageScore method
	def getAverageScore(self, courseCode):
		x=self._A.copy()
# finding the matching course
		for course in x:
			if course.courseCode==courseCode:
				y=course
				break
		n=0
		s=0
		z=y._B.copy()
# calculating total score in quiz of course
		for quiz in z:
			if quiz.attempt==1:
				n+=1
				s=s+quiz.score
# calculating error
		if n==0:
			return 0
		else:
			return s/n
# creating class Course
class Course:
	def __init__(self,courseCode,B):
		self.courseCode=courseCode
		self._B=B.copy()
# creating class Quiz
class Quiz:
	def __init__(self,title,C):
		self.title=title
		self._C=C.copy()
		self.attempt=0
		self.score=0




