from sklearn.datasets import load_breast_cancer
from matplotlib import pyplot
# フォントが見つからない。エラー。とりあえずコメントアウト
#pyplot.rcParams['font.family'] = 'IPAPGothic'
from pandas import DataFrame
from pandas.plotting import scatter_matrix

breast_cancer = load_breast_cancer()
x = breast_cancer.data #特徴量
y = breast_cancer.target #目的変数
feature_names = breast_cancer.feature_names #特徴量名

x = x[:, :10]

columns = [ '半径', 'テクスチャ', '周囲の長さ',
            '面積', 'なめらかさ', 'コンパクト性', 'へこみ',
            'へこみの数', '対称性', 'フラクタル次元']

df = DataFrame( data=x[:, :10], columns = columns)

# ここの意味を把握する
# 目的変数カラムを追加する
df['目的変数'] = y

print( df['目的変数'] )

# 悪性の腫瘍を赤色、良性の腫瘍を青色にする
colors = ['red' if v == 0 else 'blue' for v in y ]

# 散布図の描画
axes = scatter_matrix( df[columns], figsize=( 20, 20 ), diagonal='kde', c=colors)
