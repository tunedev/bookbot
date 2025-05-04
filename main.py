import sys
from stats import get_word_count, get_char_freq_map, get_sorted_freq_list

def get_book_text(filepath):
  file_content = ''
  with open(filepath) as f:
    file_content += f.read()
  return file_content

def main():
  args = sys.argv
  if len(args) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path_to_file = args[1]
  book_txt = get_book_text(path_to_file)
  num_words = get_word_count(book_txt)
  sorted_freq_list = get_sorted_freq_list(get_char_freq_map(book_txt))

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_file}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for obj in sorted_freq_list:
    print(f"{obj['char']}: {obj['count']}")
  print("============= END ===============")

main()