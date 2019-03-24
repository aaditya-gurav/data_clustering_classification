import xlrd
from collections import Counter
loc=("TSET.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0) 
fl=[]
col=sheet.ncols
row=sheet.nrows
for i in range(col):
    fl.append([])

i=2
j=0
for j in range(row):
    for i in range(col):
        fl[i].append(sheet.cell_value(j,i))

#print(fl)
lcond=[]
lcount=[]
lpara=[]
for x in range(col):
        lcond.append(fl[x][0])
        del(fl[x][0])
        lcount.append(Counter(fl[x]))        

del(lcount[0])
del(lcond[0])
del fl[0]

for y in range(col-1):
        lpara.append(list(lcount[y]))

mpro=[]

i=0
for k in range(len(lcount[col-2])):
        var=lpara[col-2][k]
        num=lcount[col-2][var]
        tot=row-1
        mpro.append((var,num/tot))

mainl=[]
final_list=[]
val=0
ct=0
cindex=0

for outer in range(len(lpara)-1):
        for inner in range(len(lpara[outer])):
                var=lpara[outer][inner]
                #print(var)
                mval=0
                mainl.append([])
                for mval  in lpara[col-2]:
                        index=0
                        #print(mval)
                        for index in range(len(fl[0])):
                              if (fl[outer][index]==var):
                                      mainl[val].append(index)
                datacount=0        
                for ct in mainl[cindex]:
                        if(fl[col-2][ct]==mval):
                                datacount=datacount+1
                datacount=datacount/2
                final_list.append((var,mval,datacount))
                cindex=cindex+1
                val=val+1

#print("COUNT:",lcount)
#print("CONDITIONS:",lcond)
#print("PARAMETERS:",lpara)
#print(fl)
#print(mainl)
#print(mpro)
#print(final_list)
inp=[]
values=[]
inp.append((input("Enter the parameters:").split(" ")))
#print(inp)
for dt in range(len(final_list)):
        for par in inp:
                if(final_list[dt][0]==par[0]):
                        values.append(final_list[dt][2])
                elif(final_list[dt][0]==par[1]):
                        values.append(final_list[dt][2])

#print(values)
result=1
result2=1
for t in range(len(values)):
        par=inp[0][t]
        print(par)
        v=lcount[t][par]
        result=result*values[t]/v
        result2=result2*(v-values[t])/v

result=result*mpro[1][1]
result2=result2*mpro[0][1]
#print(result)

if(result>result2):
        print("Under those parameters the car will be stolen")
else:
        print("Under those parameters the car will not be stolen")
