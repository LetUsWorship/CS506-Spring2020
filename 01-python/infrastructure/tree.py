#the parameter in this function determines how big the tree is going to be
#the return values will be a christmas tree drawn by symbols
def draw_tree(size=3):

    if size <= 0:
        return
        
    Triangle = ""
    Triangle2 = ""
    Triangle3 = ""
    for i in range (size):
        Triangle += ("*"*((i*4)+1)).center((((size+4)*4))," ")
        Triangle += "\n"
    Triangle += ("|"*((i*4)+3)).center((((size+4)*4))," ")
    print(Triangle)
    
    for i in range (1,size+2):
        Triangle2 += ("+"*((i*4)+1)).center((((size+4)*4))," ")
        Triangle2 += "\n"
    Triangle2 += ("|"*((i*4)+3)).center((((size+4)*4))," ")
    print(Triangle2)

    for i in range (2,size+4):
        Triangle3 += (":"*((i*4)+1)).center((((size+4)*4))," ")
        Triangle3 += "\n"
    print(Triangle3)

    
    return
    
