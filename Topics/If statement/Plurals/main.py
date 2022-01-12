number = int(input())
word = input()

# write a condition for plurals
if number != 1:
    new_word = word + "s"
    word = new_word
print(number, word)
