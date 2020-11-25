from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

c = Counter("Дождь идет на улице? Мы идем сейчас в парк! Дождь идет на улице... О чем вы тут шушукаетесь?")
plt.bar(*zip(*c.most_common()), width=.5)
plt.show()