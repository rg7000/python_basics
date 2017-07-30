i = 10
try:
    j = i / 0
    print(j)
except Exception as e:
    print("Error: "+str(e))
finally:
    print("In finally")
