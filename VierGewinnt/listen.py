#listen iterieren 

liste = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

#range(n) => [0, 1, 2, ..., n] nicht inklusive n
#0 
#1
#2

spalte = 2

for i in range(3):
    print(i, liste[i][spalte])
    #print(i, liste[][i])

