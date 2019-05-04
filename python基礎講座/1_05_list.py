#!/usr/bin/env python3

squares = [1,4,9,16,25]
print(squares)

print(squares[2]) #3番目の要素を取り出す
print(squares[-1]) #最終要素を取り出す
print(squares[3:]) #4番目から最後までの要素を取り出す

print(squares + [36, 49, 64, 81, 100]) #新しい要素を結合する

cubes = [1, 8, 27, 65, 125] 
print(cubes)

cubes[3] = 4 ** 3 #4番目の要素を入れ替える
print(cubes)

cubes.append(6**3)
cubes.append(7**3)
print(cubes)

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E'] #2番目から4番目を置き換える
print(letters)

letters[2:5] = [] #2番目から4番目を削除する
print(letters)

letters.clear() #リストの要素を全て削除する
print(letters)

letters=['a', 'b', 'c', 'd']
len(letters)

print("'a' in letters=", 'a' in letters)
print("'x' in letters=", 'x' in letters)
print("'z' not in letters =", 'z' not in letters)

