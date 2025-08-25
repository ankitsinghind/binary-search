<b>How binary search works: </b>

1. Take list of elements in a list and an element to be searched.
2. Initialize two variables, ‘low’ and ‘high’, which represent the starting and ending index of the array, respectively.
3. Calculate the middle index of the array using the formula: middle = (low + high) // 2
4. Compare the middle element of the array with the search element.
5. If the middle element is equal to the search element, return the index of the middle element.
6. If the middle element is greater than the search element, search in the left half of the array by updating the ‘high’ variable to middle-1.
7. If the middle element is less than the search element, search in the right half of the array by updating the ‘low’ variable to middle+1.
8. Repeat the above steps until the search element is found or the array is exhausted.

<img width="1510" height="299" alt="Screenshot 2025-08-24 154735" src="https://github.com/user-attachments/assets/bdce58a0-5d7f-4801-bf4c-b3191a91fd28" />
<br><br>
<b> Explaning with the example: </b>
<br><br>
So, we are having a list of numbers assigned in mylist. We can search for any number present in the list, let it be 5 (assigning x = 5).
<br><br>
Taking position of first element as 0 ie. low and last element position can be find out by subtracting 1 from length of the list ie. high.
<br><br>
The code should only run multiple times when low is less than or equal to high.
<br><br>
Finding the middle value by simple (low + high) divided by 2. Here to avoid float we use integer divison (//)
<br><br>
Now if the element to be searched (let it be x) is greater than mid value means x is on right side. low should be updated to mid + 1.
<br><br>
Similarly, vice versa for other case.
<br><br>
If none of the above is the case then x is the mid value.
<br><br>
In the given mylist having element 1-9, 1 is at index 0 and 9 is at index 8.
<br><br>
From <b> mid = (high + low) // 2 </b>, mid comes out to be 8+0 // 2; which is index 4.
<br><br>
At index 4 the element is 5.
<br><br>
If no. to be searched was other than 5, like 6 then: 
<br<br>
First range: low = 0, high = 8 mid = (0 + 8) // 2 = 4 → mylist[4] = 5 Since 5 < 6, search moves to the right half.
<br><br>
Second range: low = 5, high = 8 mid = (5 + 8) // 2 = 6 → mylist[6] = 7 Since 7 > 6, search moves to the left half.
<br><br>
Third range range: low = 5, high = 5 mid = (5 + 5) // 2 = 5 → mylist[5] = 6 Match found!
<br><br>
To exit the while loop we return -1 ie. if element was not found
<br><br>
Now if result is not equal to -1 then we print element was found and its index
