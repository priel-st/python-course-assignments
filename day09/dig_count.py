def join_numbers(num_list):
  joined = "".join(map(str, num_list))
  return joined

def digit_list(joined):
  L=[]
  for digit in joined:
    if digit not in L:
      L.append(digit)
  L.sort()
  return L

def count_dig(L, joined):
  for x in L:
    num = joined.count(x)
    print("{:<2}{}".format(x, num))
  return None
