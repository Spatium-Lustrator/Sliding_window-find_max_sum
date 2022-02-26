def find_maximum_sum(array, k):

    # Variable initialization
    n = len(array)
    current_sum = 0
    maximum_sum = 0
    for i in range(0, k):  # Sum in first window

        current_sum += array[i]

    maximum_sum = current_sum
    for i in range(k, n):  # Main loop

        current_sum -= array[i - k]  # Take away left element value
        current_sum += array[i]  # And add value of next right element
        if maximum_sum < current_sum:

            maximum_sum = current_sum

    return maximum_sum


a = [1, 4, 2, 10, 2, 3, 1, 0, 20]  # Our array
k = 4  # Window size

print("Maximum sum is", find_maximum_sum(a, k))
