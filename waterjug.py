from collections import defaultdict
jug1,jug2,aim=4,3,2
visited = defaultdict(lambda : False)
def water_jug(amt1,amt2):
    if (amt1==0 and amt2==aim) or (amt1==aim and amt2==0):
        print(amt1,amt2)
        return True
    if visited[(amt1,amt2)]==False:
        print(amt1,amt2)
        visited[(amt1,amt2)]=True
        return (
            water_jug(0,amt2) or 
            water_jug(amt1,0) or
            water_jug(jug1,amt2) or 
            water_jug(amt1,jug2) or 
            water_jug(amt1+min(amt2,(jug1-amt1)),amt2-min(amt2,(jug1-amt1))) or 
            water_jug(amt1-min(amt2-min(jug2-amt2)),amt2+min(jug2-amt2))
        )
    else:
        return False
print("Steps")
print("A","B")
water_jug(0,0)
