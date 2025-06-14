def join_numbers(num_list):
  """
  This function joins a list of integers into one string of digits
  >>>join_numbers([123,455,01])
  12345501
  """
  joined = "".join(map(str, num_list))
  return joined

def digit_list(joined):
  """
  This function extracts unique digits from a string to an ordered list
  >>>digit_list(1231230)
  ['0','1','2','3']
  """
  L=[]
  for digit in joined:
    if digit not in L:
      L.append(digit)
  L.sort()
  return L

def count_dig(L, joined):
  """
  This function prints the frequency of each digit in the joined string
  """
  for x in L:
    num = joined.count(x)
    print("{:<2}{}".format(x, num))
  return None
