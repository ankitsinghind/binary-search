How binary search works:

1. Take an input array and an element to be searched.
2. Initialize two variables, ‘low’ and ‘high’, which represent the starting and ending index of the array, respectively.
3. Calculate the middle index of the array using the formula: middle = (low + high) // 2
4. Compare the middle element of the array with the search element.
5. If the middle element is equal to the search element, return the index of the middle element.
6. If the middle element is greater than the search element, search in the left half of the array by updating the ‘high’ variable to middle-1.
7. If the middle element is less than the search element, search in the right half of the array by updating the ‘low’ variable to middle+1.
8. Repeat the above steps until the search element is found or the array is exhausted.

<img width="1510" height="299" alt="Screenshot 2025-08-24 154735" src="https://github.com/user-attachments/assets/bdce58a0-5d7f-4801-bf4c-b3191a91fd28" />
