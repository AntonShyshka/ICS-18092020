from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

c = Counter("каждый охотник желает знать где сидит фазан")
plt.bar(*zip(*c.most_common()), width=.5)
plt.show()



Дождь идет на улице? Мы идем сейчас в парк! Дождь идет на улице... О чем вы тут шушукаетесь?