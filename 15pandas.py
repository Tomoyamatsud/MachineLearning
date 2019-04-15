import matplot
import numpy
numpy.random.seed(42)

import pandas

# 10行5列の配列(要素は乱数)を作る
data = numpy.random.randn(10, 5)
print(data)

# dataを要素とするDataFrameを作る
df = pandas.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'] )

# 先頭3行を取得する
df.head(3)

# 後ろから3行を取得する
df.tail(3)

%matplotlib lnline
 df.plot()
