secret_word = "password"
guess = " "
count = 0
limit = 4
out_of_limit= False
while guess != secret_word:
    if count< limit:
       guess = input("Guess a word: ")
    count +=1
else: out_of_limit = True

       

print("Correct!")