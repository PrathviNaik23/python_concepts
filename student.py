name=input('enter your name: ')
marks=[]
total=0
for i in range(5):
    mark=int(input('enter marks: '))
    marks.append(mark)
for i in marks:
    total+=marks[i]
    if total<35:
        

