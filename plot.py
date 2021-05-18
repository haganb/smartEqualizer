import matplotlib.pyplot as plt
import numpy as np

accs= [0.722, 0.723, 0.719, 0.732, 0.738, 0.713, 0.696, 0.702, 0.696, 0.696]
vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fig, ax = plt.subplots()
rects = ax.bar(vals, accs, 0.5, color='r')
plt.xlabel("K value")
ax.set_xticks(np.arange(len(accs)))
plt.ylabel("Accuracy")
for index, data in enumerate(accs):
    plt.text(x=index+0.75, y=data*1.02, s=f"{data}", fontdict=dict(fontsize=8))
#plt.plot(vals, accs)
#plt.axis([0, 10, 0, 1])

plt.savefig("k.png")
#print("KNN accuracy on dataset:", accuracy1)