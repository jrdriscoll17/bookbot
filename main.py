path_to_file = "books/frankenstein.txt"

def sort_on(dict):
  return dict["count"]

def dict_to_list(dict):
  char_list = []

  for key in dict:
    if key.isalpha():
      char_list.append({"name": key, "count": dict[key]})

  return char_list

def sort_char_list(char_list):
  char_list.sort(reverse=True, key=sort_on)

  return char_list

def count_chars(file_contents):
  char_counts = {}

  for char in file_contents.lower():
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

  return char_counts

def count_words(file_contents):
  return len(file_contents.split())

def file_contents(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def main():
  file = file_contents(path_to_file)

  char_list = dict_to_list(count_chars(file))

  print(sort_char_list(char_list))

main()
