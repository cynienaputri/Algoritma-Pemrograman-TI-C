#python if 
a = 33
b = 200
if b > a:
  print("b is greater than a")

  #python elif
  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  #python else
  temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

  #shorthand if
  a = 2
b = 330
print("A") if a > b else print("B")

#logical operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

  #nested if 
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    #pass statement
    score = 85

if score > 90:
  pass # This is excellent
print("Score processed")
