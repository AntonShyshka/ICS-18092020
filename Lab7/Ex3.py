from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

c = Counter("Дождь идет на улице? Мы идем сейчас в парк! Дождь идет на улице... О чем вы тут шушукаетесь?")

def charCounter(validChars):
       vc = set(validChars)
       def counter(ln):
           return sum(1 for ch in ln if ch in vc)
       return counter
countSentences = charCounter('...!?')
plt.bar(*zip(*c.most_common()), width=.5)
plt.show()
