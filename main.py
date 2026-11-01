# to find out that the number is palindrome or not
num = (input("Enter a number"))
# reversed num = num[::-1]
reversed_num = ''.join(reversed(num))

if num == reversed_num:
    print("It is a Palindorme number")
else:
    print("It is not a Palindrome number")

# program to find HCF
# 
# # enter 2 numbers
numberLargest = int(input("Enter the Largest number:")) 
numberSmallest = int(input("Enter the Smallest number:"))

# using eucliden algorithms
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ", numberLargest)