

def q1(): 
  word = ("\"Hello World\"")
  print(word)

def q2(): 
  word = input("Input a word: ")
  word = word.lower()
  print(word)
  word = word.upper()
  print(word)

def q3(): 
  word = input("Input a word that is at least 5 letters long: ")
  print(word[1:4])

def q4(): 
      word = input("Input a word: ")
      print(word.index("o"))

def q5(): 
  word = input("Input a word: ")
  print(len(word))

#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
