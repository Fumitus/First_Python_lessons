
reiksmes=list(input())

ilgis=len(reiksmes)
print(ilgis)

print(reiksmes)

for i in range(ilgis):
    if '0' in reiksmes:
        x=reiksmes.index('0')
        print(x)
        reiksmes[x]='.'
        print(reiksmes)
    





#def replace_element(reiksmes, set_to=1):
#    return [i
 #              if i != '.'           
               
               
 #              else set_to
 #              for i in reiksmes]
#    print(reiksmes)



