height=[]
label=[]
final=[]
n=int(input("Enter the number of terms : "))
print("Enter the data set ")
for i in range(n):
    print ("Enter the data for set ",i+1)
    hei=float(input("Enter the height "))
    lab=input("Enter the label ")
    height.append(hei)
    label.append(lab)

k=int(input("Enter the value of k "))
fi=float(input("Enter the value of height "))

for x in range(n):
    height[x]=height[x]-fi
    if height[x]<0:
        height[x]=height[x]*-1

for y in range(k):
    d=height.index(min(height))
    final.append(label[d])
    del height[d]
    del label[d]

short=0
medium=0
tall=0

for z in range(k):
    if final[z] == 's':
        short=short+1
    if final[z] == 'm':
        medium=medium+1
    if final[z] == 't':
        tall=tall+1

print("The given height is under the label:")

if short>medium and short>tall:
    print("SHORT")
elif short<medium and medium>tall:
    print("MEDIUM")
else:
    print("TALL")