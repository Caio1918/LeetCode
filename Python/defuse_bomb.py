#class Solution:
#    def decrypt(self, code: List[int], k: int) -> List[int]:
#        soma = 0
#        
#        if k > 0:
#            for i in range(len(code)):
#                print()
#
#         if k < 0:
#            print()
#        if k == 0:
#            print()



lista = [5,7,1,4]
k = 3

for i in range(len(lista)):
    for j in range(k):
        if j+(i+1) > len(lista):
            print(lista[j-i+1])
        else:
            print(lista[j+i+1])


