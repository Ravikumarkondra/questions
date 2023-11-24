
def ispalindrome(string):
    if (string==string[::-1]):
        return "the string is a palindrome"
    else :
        return "the string is not palindrome"


string = input("enter a sring :")

print(ispalindrome(string))