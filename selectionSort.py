#Make an array for the sorting of the selection
#writing a new status for gitbash to see
array = [32, 34,5,6,23,7,12,68]
#creating our selection sort funtion
def selectionSort(array):

	n = len(array)#<-- n is the length of our array

	for i in range(n): #<--Whatever the length of the array is how many times you are going to run the loop
		#Initially assum the first element of the unsorted part as teh minimum
		minimum = i #<-- giving the variable of minimum i
		#creating a for loop
		for j in range(i+1, n):

			if (array[j] < array[minimum]):

				minimum = j

		#Swap the minimum element with the first element of the unsorted part.

		temp = array[i]
		array[i] = array[minimum]
		array[minimum] = temp

	return array

print(selectionSort(array))









