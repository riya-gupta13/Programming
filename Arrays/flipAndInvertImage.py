def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    l=[]
    for i in image:
        i=i[::-1]
        li=[]
        for j in range(0,len(i)):
            # print(i[j])
            if i[j]==1:
                i[j]=0
            else:
                i[j]=1
            li.append(i[j])
        l.append(li)

    print(l)



image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
flipAndInvertImage(image)