def checkpalindrome(nums):

    # return the palindrome numbers i.e original num equals to the same number in reverse form
    return nums == nums[::-1]

def largestpalindrome():

    # Initial largest to zero
    largest = 0

    # Nested for loop to generate three digit numbers for 100-999
    # Check if product is higher than largest and is palindrome
    # Assign largest to product and return largest

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j

            if product > largest and checkpalindrome(str(product)):
                largest = product

    return largest


# The correct answer is 906609
print(largestpalindrome())

