from random import shuffle

file = open("resultado.txt", "w")

members = [
'Gabriel Domingos',
'Joao Felipe',
'Leonardo Toledo',
'Pedro Henrique',
'Rodrigo Perdigao',
'Victor Raphael',
'Yan Cardoso']

file.write("Tempo total da rodada: %d min\n" %(len(members)*10))

shuffle(members)

for i in range(1,len(members)):
    file.write("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(i,members[i-1],members[i]))
    if (i==len(members)-1) :
        file.write("\nDupla %d:\n Piloto: %s\n Co-piloto: %s\n" %(len(members),members[len(members)-1],members[0]))

file.close()
