# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 13:43:00 2025

@author: sahakian.a
"""

import json

import re

def load_bible(filepath):
    lines = []
    dicti = {}
    book_name = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                line = line.strip()
                lines.append(line)
                split_line = line.split()
                key= split_line[0]+split_line[1]
                value = " ".join(split_line[2:])
                dicti [key] = value
                book_name.append(split_line[0])
            except:
                pass
        return  dicti, set(book_name)
    
verses_east= load_bible(r"C:\Users\sahakian.a\Downloads\datas\datas\bible_arm\east.txt")
verses_west =  load_bible(r"C:\Users\sahakian.a\Downloads\datas\datas\bible_arm\west.txt")




def align_bibles(ea, wa, output_path):
    
    aligned = []
    count = 0
    for verse_id in ea:
        if verse_id in wa:
            aligned.append({
                "id": verse_id,
                "source": ea[verse_id],
                "target": wa[verse_id]
            })
            count += 1

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(aligned, f, ensure_ascii=False, indent=2)

    print(f"Aligned {count} verse pairs.")

# Example usage:
if __name__ == "__main__":
    align_bibles(verses_east[0],verses_west[0], r"C:\Users\sahakian.a\Downloads\datas\datas\bible_arm\parallel_bible.json")



with open(r"C:\Users\sahakian.a\Downloads\datas\datas\bible_arm\parallel_bible.json", 'r', encoding='utf-8') as f:
    data = json.load(f)  # Loads JSON data into a Python dict or list

