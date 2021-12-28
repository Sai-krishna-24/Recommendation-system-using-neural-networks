#implementing a* search alogrithm for maze solving problem in least cost
from pyamaze import maze,agent,textLabel
from queue import PriorityQueue

#here heuristic function we used is manhattan distance which helps as additional information makes efficient and useful for calcuation f(n) and it is the distance between goal tto present

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
        #location of start state
    #initialize g scores (distances to cells from start) to infinity for all cells
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    #f_scores is sum of gscore and heuristic value
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))
    #creating a priority queue open which have the cells to travel from
    open=PriorityQueue()
    #adding first node to open
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    #create a dictionary apath to store the path we go
    aPath={}
    while not open.empty():
        #while loop runs until reaches (1,1) goal cell
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                #for each cell only one direction can be true
                #finding next reachable child cell
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))
                #adding next reachable child cell to queue
                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    #creating maze
    m=maze(6,6)
    m.CreateMaze()

    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    m.run()
