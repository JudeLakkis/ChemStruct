#!/usr/bin/env python3
# -*- coding: utf-8 -*-

result = [([[327, 277], [419, 277], [419, 515], [327, 515]], 'H', 0.5169475173293883), ([[32, 604], [130, 604], [130, 714], [32, 714]], 'H', 0.8897842079336193), ([[193, 577], [671, 577], [671, 713], [193, 713]], '~(-h', 0.45371490716934204), ([[300, 892], [458, 892], [458, 1006], [300, 1006]], 'Oh', 0.3088542355854099)]

def clean_results(result):
    results = []
    for i in result:
        if not i[1].isalnum():
            code = ""
            for char in i[1]:
                if char == "(":
                    code += "C"
                elif char == "~":
                    code += "-"
                else:    
                    code += char.upper()
        else:
            code = i[1].upper()
        results.append([code, i[0]])
    return results

def break_characters(data, font_size=3):
    characters = []
    for i in data:
        if not i[0].isalnum():
            code = i[0]
            length, height = i[1][1][0] - i[1][0][0], i[1][3][1] - i[1][0][1]
            segment = (length + (length % len(code))) // len(code)
            x1, y1 = i[1][0]
            x2, y2 = i[1][3]
            points, addition = [], 0
            for j in range(len(code) -1):
                addition += segment
                a = [[x1, y1],  [x1 + addition,y1], [x1 + addition, y2], [x2, y2]]
                points.append([code[j], a])
                x1 += segment
                x2 += segment

            #  a = [[x1, y1],  [x2, y1], [x2, y2], [x2, y2]]
            [characters.append(k) for k in points]
        else:
            characters.append(i)

    for i in characters:
        top_left, bottom_right  = i[1][0], i[1][2]
        xmid = ((bottom_right[0] - top_left[0])//2) + top_left[0]
        ymid = ((bottom_right[1] - top_left[1])//2) + top_left[1]
        i.append((xmid-(font_size * 10), ymid+(font_size * 10)))

    return characters


result = [([[327, 277], [419, 277], [419, 515], [327, 515]], 'H', 0.5169475173293883), ([[32, 604], [130, 604], [130, 714], [32, 714]], 'H', 0.8897842079336193), ([[193, 577], [671, 577], [671, 713], [193, 713]], '~(-h', 0.45371490716934204), ([[300, 892], [458, 892], [458, 1006], [300, 1006]], 'Oh', 0.3088542355854099)]
clean = clean_results(result)
for i in clean:
    print(i)
print()

data = break_characters(clean, 3)
for i in data:
    print(i)
