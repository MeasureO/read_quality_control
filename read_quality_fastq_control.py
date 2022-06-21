import sys
import os
import gzip

data = {i: [] for i in range(3)}
for j in range(3):
    path = input()
    with gzip.open(path, 'r') as file:
        lines = [i.decode('utf8').strip() for i in file.readlines()]
        # print(lines)
        size_dict = {}
        for i in range(1, len(lines), 4):
            if len(lines[i]) not in size_dict:
                size_dict[len(lines[i])] = 1
            else:
                size_dict[len(lines[i])] += 1
        size_dict = dict(sorted(size_dict.items()))
        #print(f"Reads in the file = {len(range(1, len(lines), 4))}")
        data[j].append(len(range(1, len(lines), 4)))
        s = 0
        for size in size_dict:
            s += size * size_dict[size]
        # print(f"Reads sequence average length = {round(s / len(range(1, len(lines), 4)))}")
        data[j].append(round(s / len(range(1, len(lines), 4))))
        # print(f"\nRepeats = {len(lines[1::4]) - len(set(lines[1::4]))}")
        data[j].append(len(lines[1::4]) - len(set(lines[1::4])))
        # print(f"Reads with Ns = {sum([1 if 'N' in i else 0 for i in lines[1::4]])}")
        data[j].append(sum([1 if 'N' in i else 0 for i in lines[1::4]]))
        averages = [round((i.count("G") + i.count("C")) * 100 / len(i), 2) for i in lines[1:len(lines):4]]
        # print(f"\nGC content average = {round(sum(averages) / len(averages), 2)}%")
        data[j].append(round(sum(averages) / len(averages), 2))
        ns_per_seq = [round(i.count('N') * 100 / len(i), 2) if 'N' in i else 0 for i in lines[1::4]]
        # print(f"Ns per read sequence = {round(sum(ns_per_seq) / len(ns_per_seq), 2)}")
        data[j].append(round(sum(ns_per_seq) / len(ns_per_seq), 2))
        data[j].append(lines[1 + 4 * j].count('N'))
# print(data)
# print(dict(sorted(data.items(), key=lambda kv: kv[1][0])))
j_best = min([(0, data[0][0]), (1, data[1][0]), (2, data[2][0])], key=lambda x: x[1])
# print(data)
print(f"Reads in the file = {data[j_best[0]][0]}")
print(f"Reads sequence average length = {round(data[j_best[0]][1])}")
print(f"\nRepeats = {data[j_best[0]][2]}")
print(f"Reads with Ns = {data[j_best[0]][3]}")
print(f"\nGC content average = {round(data[j_best[0]][4], 2)}%")
print(f"Ns per read sequence = {round(data[j_best[0]][5], 2)}")
