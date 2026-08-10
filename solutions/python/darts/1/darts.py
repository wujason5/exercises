def score(x, y):
    #  out = 10
    # mid = 5
    # inner = 1
    # range = (x/y)/2 
    scored = (x**2 + y**2) ** 0.5

    if scored <= 1:
        return 10
    elif scored <= 5:
        return 5
    elif scored <= 10:
        return 1
    else:
        return 0
        
