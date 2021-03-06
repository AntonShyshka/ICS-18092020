from collections import Counter
import re
 
t = '''\
Поздняя осень
Осень.Мы ждали её давно. По серому небу плывут низкие облака.
Серо, пусто.Но всё видно сквозь голые деревья. Листья давно облетели,
они лежат на земле, под  деревьями и кустами. Единственная отрада - берёзка,
она  всё ещё не сбросила свои желтоватые листья. Зеленеют ели и сосны.
На них вечнозелёный наряд. Птицы выбрались из леса, их манят в сады яркие кисти
рябины и калины. Я люблю осень, несмотря на её холодную красоту.'''
ls = ['мы', 'её', 'всё', 'они', 'она', 'свои', 'них', 'их', 'я', 'по', 'со' ]
words = re.findall(r'\w+', t.lower())
counter = Counter(words)
for word, count in counter.most_common():
    p = (count/len(words))*100
    print('%s - %.3f %%' % (ls, p))
