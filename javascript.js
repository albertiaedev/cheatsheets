//JAVASCRIPT CHEATSHEET

//String Methods
1. string.includes('substring'); // checks whether a substring exists inside of a string
2. string.indexOf(n); /*returns the index of the first occurrence of the specified value,
                        starting the search at fromIndex.
                        returns -1 if the value is not found.*/
3. string.lastIndexOf(n); /*returns the index of the last occurrence of the specified value,
                            searching backwards from fromIndex.
                            returns -1 if the value is not found.*/
4. string.slice(beginIndex, endIndex); /*extracts a section of a string and returns it as a new
                                         string, without modifying the original string.*/

//Array Methods
1. {nameOfArray}[n]; // returns a certain value from an array
2. push(value); // adds the value to the end of the array
3. pop(); // removes the value from the end of the array
4. shift(); // removes the value from the start of the array
5. unshift(value); // adds the value to the start of the array
6. splice(fromIndex, no_of_elements); // removes the number_of_elements, starting from fromIndex from the array
7. slice(fromIndex, toIndex); // copies a certain part of the array
8. concat(); // join several arrays into one
9. join(''); // returns a string of array values
10. array.length; // returns the number of elements in the array
11. reverse(); // reverse the order of the elements in an array
12. toString(); // returns a string representing the specified array and its elements

//Date Objects
1. getUTCMinutes(); // same as getMinutes(), but returns the UTC minutes

2. getUTCSeconds(); // same as getSeconds(), but returns the UTC seconds

3. getUTCMilliseconds(); // same as getMilliseconds(), but returns the UTC milliseconds
