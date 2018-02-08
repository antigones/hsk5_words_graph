# -*- coding: utf-8 -*-

import csv

word_array = []
file = open("output.csv","w",encoding='utf8') 

with open("HSK5_freqorder.txt", 'r',encoding='utf8') as csvfile:
    freader = csv.reader(csvfile, delimiter='\t')
    for row in freader:
        word_array.append(row[0])

hmap = {}
for i in range(0,len(word_array)):
    # for each word...
    cur_word = word_array[i]
    for j in range(0,len(cur_word)):
        # for each word component
        hanzi = cur_word[j]
        for k in range(0,len(word_array)):
            # search in every other word...
            opp_word = word_array[k]
            for w in range(0,len(opp_word)):
                # a component in this other word...
                opp_hanzi = opp_word[w]
                if (i != k):
                    if (opp_hanzi == hanzi):
			# equal to the source word, deliberately don't care about duplicate words
                        cur_values = hmap.get(hanzi,[])
                        cur_values.append(opp_word)
                        hmap[hanzi] = cur_values

# use the map to write a csv to be used by Gephi
for key, value in hmap.items():
    file.write(key+","+','.join(hmap[key])+'\n')
file.close()
