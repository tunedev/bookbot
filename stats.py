def get_word_count(txt):
  return len(txt.split())

def get_char_freq_map(txt):
  char_map = {}
  normalized_txt = txt.lower()
  for char in normalized_txt:
    if char in char_map:
      char_map[char] = (char_map[char] + 1)
    else: 
      char_map[char] = 1
  return char_map

def sort_on(dict):
  return dict['count']

def get_sorted_freq_list(freq_map):
  freq_list = []
  for key in freq_map:
    if key.isalpha():
      freq_list.append({ "char": key, "count": freq_map[key] })
  
  freq_list.sort(reverse=True, key=sort_on)
  return freq_list

