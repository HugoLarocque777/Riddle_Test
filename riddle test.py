# this is a riddle knowledge test
print ("Please answer these riddles")
print ("If you need a hint, type help")
correct_answers = 0
#this is the riddle
print ("1. Riddle: What has to be broken before you can use it?")
# defining the input as the variable answer
answer = input()
# telling the computer what the correct answer is
if answer == 'an egg' or answer == 'An Egg' or answer ==' An egg' or answer == 'egg':
    print ("correct")
# for when I need to find the percentage of correct at the end of the program
    correct_answers += 1
# a hint
elif answer == 'help':
    print ("think of baking")
    print ("please try again")
# remaking the input for another answer
    cool = input()
    if cool == 'an egg' or cool == 'An Egg' or cool ==' An egg' or cool == 'egg':
        print("correct")
        correct_answers += 1
# if you get it wrong again you get it incorrect
    else:
        print ("sorry incorrect")
# if you got it wrong before you typed help it skips the indented code and goes to here
else:
    print ("sorry incorrect")
# another riddle

print ("2. Riddle: I’m tall when I’m young, and I’m short when I’m old. What am I?")
ans = input()
if ans == 'A Candle' or ans == 'A candle' or ans == 'a candle' or ans == 'candle':
    print ("correct")
    correct_answers += 1
elif ans == 'help':
    print ("burn! burn! burn!")
    print("please try again")
    chill = input()
    if chill == 'A Candle' or chill == 'A candle' or chill == 'a candle' or chill == 'candle':
        print ("correct")
        correct_answers += 1
    else:
        print ("sorry incorrect")
else:
    print ("sorry incorrect")


print ("3. Riddle: What gets wet when its drying")
man = input()
if man == 'A Towel' or man == 'A towel' or man ==  'a towel' or man == 'towel':
    print ("correct")
    correct_answers += 1
elif man == 'help':
    print ("Think of where YOU get wet!")
    print("please try again")
    fat = input()
    if fat == 'A Towel' or fat == 'A towel' or fat ==  'a towel' or fat == 'towel':
        print ("correct")
        correct_answers += 1
    else:
        print ("sorry incorrect")
else:
    print ("sorry incorrect")



print ("4. Riddle: David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?")
l = input()
if l == 'David' or l == 'david':
    print ("correct")
    correct_answers += 1
elif 1 == 'help':
    print ("David's parents!")
    print("please try again")
    lego = input()
    if lego == 'david' or lego == 'David':
        print ("correct")
        correct_answers += 1
    else:
        print ("sorry incorrect")
else:
    print ("sorry incorrect")


# write a code to tell what percentage you got correct
percentage = (correct_answers / 4) * 100
print(f"You got {percentage}% correct!")


