# Glen
# Period 4
# 11-23-15


# This will get the name and grade level, also it will print out a greeting

name = input("What is your name? ")
grade = int(input("What is your grade level you are currently in? "))

if grade == 9:
    print (" Hello, %s, welcome to your first year in highschool." %(name))
elif grade == 10:
      print (" Hello, %s, welcome to your second year in highschool." %(name))
elif grade == 11:
      print (" Hello, %s, one more year until yuor a senior." %(name))
elif grade == 12:
      print (" Hello, %s, dont forget to get ready for college." %(name))
else:
    print("Sorry it's an invalid grade.")
