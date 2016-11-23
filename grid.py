#Character Picture Grid

"""
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x1 =0
y1 =0
x2= 0
y2= 8
newGrid=[]

for slot in grid:
	newGrid[x2][y2] = grid[x1][y1]
	x1+=1
	y2-=8
	for slot in grid:
		newGrid[x2][y2] = grid[x1][y1]
		x2+=1
		y1+=1

print newGrid
"""



"""Say you have a list of lists where each value in the inner lists is a one-character 
string, like this:


grid[0,0]=grid[0,9]  grid[x1,y1]=grid[x2,y2]  
grid[0,1]=grid[1,9]
grid[0,2]=grid[2,9]

grid[1,0]=grid[0,8]
grid[1,1]=grid[1,8]

grid[2,0]=grid[0,7]
grid[2,1]=grid[1,7]

grid[3,0]=grid[0,6]
grid[3,1]=grid[1,6]

"""





"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



rows =8
columns= 5
mylist = [[0 for x in range(columns)] for x in range(rows)]
for i in range(rows):
    for j in range(columns):
        mylist[i][j] = '%s,%s'%(i,j)
print mylist

"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
x1 =0
y1 =0
x2= 0
y2= 0
rows =8
columns= 5
newGrid=[]
i=1

for i in range(len(grid)):
	x1 =0
	y2=len(grid)-i
	y1=y1+1
	print ('y1-' + str(y2-1))
	for j in range(len(grid[1])):
		x1=x1+1
		x2=j
		
		print ('x1-' + str(x1-1))
		##newGrid[x2][y2-1] =grid[x1-1][y1]
		#newGrid[x2][y2] = grid[x1][y1]
		##print grid[x1-1][y1]
	
	
#print grid