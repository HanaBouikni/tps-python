word=str(input("type in a word :"))

palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        palindrome = False
    else:
        palindrome = True

        break

if palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")