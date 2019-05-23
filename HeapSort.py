#Sorting list by Heap sort algorithm
class HeapSort:
    a = []
    def Heap(self,a, n, i):
        big = i
        right = (i * 2) + 2
        left = (i * 2) + 1

        if left < n :   #if left child greater than root
            if a[i] < a[left]:
                big = left

        if right < n :  #if right child greater than root
            if a[big] < a[right]:
                big = right

        if big != i: #swap existed root
            temp = a[i]
            a[i] = a[big]
            a[big] = temp
            self.Heap(a, n, big)

obj = HeapSort()

print("Enter any six integers to sort")
i=0
while i< 6:
    obj.a.append(int(input()))
    i=i+1
n = len(obj.a)
print("Before Sorting....")
for i in range(n):
    print("%d" % obj.a[i])
for i in range(n, -1, -1):  # maxheap.
    obj.Heap(obj.a, n, i)
for i in range(n - 1, 0, -1):
    temp = obj.a[i]
    obj.a[i] = obj.a[0]
    obj.a[0] = temp
    obj.Heap(obj.a, i, 0)

print("After Sorting....")
for i in range(n):
    print("%d" % obj.a[i])