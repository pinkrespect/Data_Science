from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]

num_oscar = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscar)
plt.ylabel("# of Academy Awards")
plt.title("my favorite movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()
