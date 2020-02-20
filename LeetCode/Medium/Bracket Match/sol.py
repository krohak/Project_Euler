def bracket_match(text):
  
  balance = 0
  counter = 0
  
  for char in text:
    if is_opening(char):
      balance+=1
    else:
      balance-=1
      
    if balance<0:
      balance = 0
      counter+=1
      
  if balance<=0:
    return counter
  else:
    return counter+balance
  
  
def is_opening(char):
  return True if char=='(' else False
  