with open("propane.gjf") as file:
    data = file.readlines()
    
atoms=[]
for i in data[6:17]:
    #print(i.split())
    atoms.append(i.split())
    
    


print('------------')

counter1 = 1
new_elements = []

for obj1 in atoms:
    print('$atom:{}{}\t $mol:{}\t @atom:{}\t 0.0\t {}\t {}\t {}'\
          .format(obj1[0],counter1,'...','Atype',obj1[1],obj1[2],obj1[3]))
    new_elements.append('{}{}'.format(obj1[0],counter1))
    counter1 += 1
    
print('------------\n')
print('here are the list of elements:\n',new_elements,'and total number of atoms are:',len(new_elements))
print('------------\n')

elements = []
for obj1 in atoms:
    elements.append(obj1[0])

print(elements)

print('------------')
all_connectivity=[]
conn_data = data[18:29]
for i in conn_data:
    #print(i.split())
    all_connectivity.append(i.split())
    
print('------------')

connectivity=[]
for i in range(len(all_connectivity)):
    if len(all_connectivity[i]) >2:
        #print(all_connectivity[i])
        connectivity.append(all_connectivity[i])
        
print('------------')
# print('There are the connectivities:\n',connectivity)




for i in range(0, len(connectivity)):
    while connectivity[i].count('1.0') >0 :
        connectivity[i].remove('1.0')
        
    connectivity[i] = [int(float(i)) for i in connectivity[i]]
        
print('Connectives:\n',connectivity)

print('------------')

my_new_list = []
for i in range(0, len(connectivity)):
    for j in connectivity[i]:
        my_new_list.append([connectivity[i][0], j])
print('Converted Connectives:\n',my_new_list)



bonds = []
for i,j in my_new_list:
    if i!=j:
        #print(new_elements[i-1],new_elements[j-1])
        bonds.append([new_elements[i-1],new_elements[j-1]])
        
print('------------')
print('total number of bonds:', len(bonds))


print('------------')
counter2 = 0
for i,j in my_new_list:
    if i!=j:
        print('$bond:bnd{} $atom:{} $atom:{}'.format(counter2,new_elements[i-1],new_elements[j-1]))
        
    counter2 += 1
print('------------')
    
    
    
