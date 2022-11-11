number_list=[]
n=int(input("Introdu numarul de elemente: "))
print("\n")
for i in range(0, n):
    print("Introdu elementul de pe pozitia: ",i, )
    item=int(input())
    number_list.append(item)
print("Lista este ", number_list)
number_list.append(10)
print("Lista noua dupa ce am adaugat 10 este ", number_list)