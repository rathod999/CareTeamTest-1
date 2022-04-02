class Node:
	#Initializing nodes with the data , level , and the final level
	def __init__(self,data,level,fval):
		self.data=data
		self.level=level
		self.fval=fval

	def generate_child(self):
		#moving of the blank space to achieve the final state i.e left,right,down,bottom
		x,y=self.find(self.data,'_')

	#moving the val_list to the left,right,down,bottom
		children = []
		val_list= [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
		for i in val_list:
			child=self.shuffle(self.data,x,y,i[0],i[1])
			if child is not None:
				child_node = Node(child,self.level+1,0)
				children.append(child_node)

		return children
	
	def shuffle(self,puz,x1,y1,x2,y2):
		#moving the blank space in the given direction and if position value is not in the limits return None
		if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
			temp_puz= []
			temp_puz= self.copy(puz)
			temp =temp_puz[x2][y2]
			temp_puz[x2][y2]= temp_puz[x1][y1]
			temp_puz[x1][y1]=temp
			return temp_puz

		else:
			return None

	def copy(self,root):
		#copy the fn to create similiar type of matrix
		temp=[]
		for i in root:
			t = []
			for j in i:
				t.append(j)
			temp.append(t)
		return temp
	def find(self,puz,x):
		#find the position of blank space
		for i in range(0,len(self.data)):
			for j in range(0,len(self.data)):
				if puz[i][j] == x:
					return i,j
class Puzzle:
	def __init__(self,size):
		#puzzle for declaring size,open,close
			
		self.n=size
		self.open=[]
		self.closed=[]

		
	def accept(self):
		#accepts the puzzle from user
		puz=[]
		for i in range(0,self.n):
			temp=input().split(" ")
			puz.append(temp)
		return puz

	def f(self,start,goal):
			# heuristic fn for calc og f(x)=h(n)+g(n)
		return self.h(start.data,goal)+start.level
	def h(self,start,goal):
		#difference btw 2 puzzles
		temp=0
		for i in range(0,self.n):
			for j in range(0,self.n):	
				if start[i][j] !=goal[i][j] and start[i][j]!='_':
					temp +=1
		return temp

	def process(self):
		#accepting the start and goal puzzle state
		print("Enter the start State matrix \n")
		start =self.accept()
		print("Enter the goal state matrix \n")
		goal = self.accept()

		start =Node(start,0,0)
		start.fval =self.f(start,goal)
		#putting start node in the open list
		self.open.append(start)
		print("\n\n")
		while True:
			cur = self.open[0]
			print("")
			print(" | ")
			print(" | ")
			print("\\\'/\n")
			for i in cur.data:
				for j in i:
					print(j,end=" ")
				print("")

			#state of curr node is 0 we have reached the goal node
			if(self.h(cur.data,goal) == 0):

				break
			for i in cur.generate_child():
				i.fval = self.f(i,goal)
				self.open.append(i)
			self.closed.append(cur)
			del self.open[0]
			# sort the opened list based on f value
			self.open.sort(key = lambda x:x.fval,reverse=False)
puz =Puzzle(3)
puz.process()

			
