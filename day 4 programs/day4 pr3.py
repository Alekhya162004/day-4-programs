def smallerNumbersThanCurrent(numbers):
    result = [0] * len(numbers)
    for i in range(len(numbers)):
        count = 0
        for j in range(len(numbers)):
            if i != j and numbers[j] < numbers[i]:
                count += 1
        result[i] = count
    return result

numbers = list(map(int, input("Enter the numbers in the array: ").split(',')))
print(smallerNumbersThanCurrent(numbers))
Footer
