def loop(n):
    loop_count=0
    for i in range(1,n+1):
        print(i)
        loop_count+=1
    return loop_count

def nested_loop(n):
    inner_loop_count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,j)
            inner_loop_count+=1
    return inner_loop_count

count = loop(5)
print("For n=5 loop runs ",count," times")

count = loop(20)
print("For n=20 loop runs ",count," times")

count = nested_loop(5)
print("For n=5 nested loop runs ",count," times")

count = nested_loop(10)
print("For n=10 nested loop runs ",count," times")
