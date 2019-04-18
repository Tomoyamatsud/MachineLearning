from pandas import DataFrame
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron

breast_cancer = load_breast_cancer()
x = breast_cancer.data[:, :10]
y = breast_cancer.target

columns = ['半径', 'テクスチャ', '周囲の長さ', '面積', 'なめらかさ',
           'コンパクト性', 'へこみ', 'へこみの数', '対称性', 'フラクタル次元']

df = DataFrame(data=x[:, :10], columns=columns)
df['目的変数'] = y

x = df[['面積', 'へこみ']].values
y = df['目的変数'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,
                                                    random_state=42)

print('全てのデータ数 = ', len(y))
print('訓練データ数 = ', len(y_train))
print('テストデータ数 = ', len(y_test))

# StandardScalerのインスタンスを作成する
sc = StandardScaler()
# 訓練データの平均と標準偏差を計算する
sc.fit(x_train)

print(sc.mean_)

# 訓練データの標準化
x_train_std = sc.transform(x_train)

# テストデータの標準化
# テストデータは訓練データの平均と標準偏差を用いて変換する
x_test_std = sc.transform(x_test)

# 標準化後の訓練データの平均値
train_mean = x_train_std.mean(axis=0)
print(train_mean)

# 標準化後の訓練データの標準偏差
train_std = x_train_std.std(axis=0)
print(train_std)

# 標準化後のテストデータの平均値
test_mean = x_test_std.mean(axis=0)

# 標準化後のテストデータの標準偏差
test_std = x_test_std.std(axis=0)
print(test_std)

# パーセプトロンのインスタンスを作成する
ppn = Perceptron(max_iter=1000, random_state=42)

# パーセプトロンの学習
ppn.fit(x_train_std, y_train)
