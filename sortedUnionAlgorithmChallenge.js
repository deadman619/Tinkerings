/* Write a function that takes two or more arrays and returns a new array of unique values in the order of the original provided arrays.
In other words, all values present from all arrays should be included in their original order, but with no duplicates in the final array.
The unique numbers should be sorted by their original order, but the final array should not be sorted in numerical order.

Check the assertion tests for examples.
Assertion tests: 

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) should return [1, 3, 2, 5, 4].

uniteUnique([1, 3, 2], [1, [5]], [2, [4]]) should return [1, 3, 2, [5], [4]].

uniteUnique([1, 2, 3], [5, 2, 1]) should return [1, 2, 3, 5].

uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]) should return [1, 2, 3, 5, 4, 6, 7, 8].

Remember to use Read-Search-Ask if you get stuck. Try to pair program. Write your own code. */

function uniteUnique(arr) {
  var fullArrStart = [];
  var fullArrEnd = [];
  for (let i = 0; i<arguments.length; i++) {
    fullArrStart.push(arguments[i]);
  } 

  for (let b = 0; b<fullArrStart.length; b++) {
    for (let c = 0; c<fullArrStart[b].length; c++) {
      fullArrEnd.push(fullArrStart[b][c]);
    }
  }
 
  for (let j = 0; j<fullArrEnd.length; j++) {
    for (let k = j+1; k<fullArrEnd.length; k++) {
      if (fullArrEnd[j] === fullArrEnd[k]) {
        fullArrEnd.splice(k, 1);
      }
    }
  }

  return fullArrEnd;
}


console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]));
console.log(uniteUnique([1, 3, 2], [1, [5]], [2, [4]]));
console.log(uniteUnique([1, 2, 3], [5, 2, 1]));
console.log(uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]));