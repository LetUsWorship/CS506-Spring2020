def draw_road(length=10,axis = "horizontal"):
    
    VALID = ["horizontal","vertical"]
    
    if axis not in VALID:
        raise ValueError("incorrect axis")

    if length < 0:
        raise ValueError("incorrect length")
    
    if axis == "horizontal":
        return draw_H(length)

    else:
        return draw_V(length)

    return

def draw_H(length):
    for i in range(length):
        print("=", end ="")
    print()
    return

def draw_V(length):
    for i in range(length):
        print("||")
    return
