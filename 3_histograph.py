from matplotlib import pyplot as plt
import collections # 책에는 없음 ㅡㅡ

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

decile = lambda grade: grade // 10 * 10

histogram = collections.Counter(decile(grade) for grade in grades)
# 책에는 없음 collections의 Counter 기능 사용

plt.bar([x - 4 for x in histogram.keys()],
        histogram.values(),
        8)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("decile")
plt.ylabel("# of students")
plt.title("distribution of exam 1 grades")
plt.show()

