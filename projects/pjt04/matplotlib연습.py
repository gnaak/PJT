import matplotlib.pyplot as plt

# 예제 1 : x, y 가 같을 때 
plt.plot([1,2,3,4])
# plt.show()

# 참고 : 이때까지 그렸던 plot 지우기 
# 안쓰면 위에 plt.plot([1,2,3,4])과 같이 나옴 
plt.clf()

# 예제 2 : x, y 가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
# plt.show()
plt.clf()


# 예제 3 : 제목 + 각 축의  설명
plt.plot(x, y)

# 제목
plt.title("TEST GRAPH") # 한글은 안되네요 

# x, y 축
plt.xlabel('x label')
plt.ylabel('y label')
# plt.show()

# 파일로 저장하기 -> plt.show()를 지워줘야함 
plt.savefig('filenamge.png')