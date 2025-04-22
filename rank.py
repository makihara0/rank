# ダミーデータ（No, 生徒名, 国語, 数学, 情報）
students = [
    [1, '田中太郎', 75, 88, 92],
    [2, '佐藤花子', 82, 70, 85],
    [3, '鈴木一郎', 68, 64, 71],
    [4, '高橋二郎', 90, 90, 95],
    [5, '田中三子', 55, 60, 65],
    [6, '渡辺四郎', 70, 77, 89],
    [7, '伊藤五月', 85, 72, 84],
    [8, '中村六子', 60, 69, 73],
    [9, '小林七郎', 88, 91, 94],
    [10, '加藤八子', 73, 68, 72]
]

# 合計点を計算し、新しいリストに格納
results = []
for s in students:
    total = s[2] + s[3] + s[4]
    results.append([s[0], s[1], s[2], s[3], s[4], total])

# 合計点で降順にソート
results.sort(key=lambda x: x[5], reverse=True)

# 順位をつける
rank = 1
previous_score = -1
for i in range(len(results)):
    if results[i][5] != previous_score:
        rank = i + 1
    results[i].append(rank)
    previous_score = results[i][5]

# 結果を表示
print("No 生徒名     国語 数学 情報 合計点 順位")
for r in results:
    print(f"{r[0]:>2} {r[1]:<8} {r[2]:>3} {r[3]:>3} {r[4]:>3} {r[5]:>4} {r[6]:>2}")