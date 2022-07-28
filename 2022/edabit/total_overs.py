

print(type(5.16) == type(float()))

def total_overs(balls):
    overs = str(round(balls/6, 1))
    over1 = overs.split(".")[0]
    over2 = overs.split(".")[1]
    if over2 != "0":
        print("FLOAT")
        return(over1+ " overs and " + over2 + " balls were bowled by the bowler.")
    return float(overs) 


print(total_overs(76))
print(total_overs(2400))
        
