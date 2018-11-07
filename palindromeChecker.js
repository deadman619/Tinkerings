// A palindrome is a word or sentence that's spelled the same way both forward and backward, ignoring all non-alphanumeric characters.

function palindrome(str) {
  var replaced = str.replace(/[ _,.\-:/\\()]/g, '').toLowerCase();
  var reverseStart = replaced.split('');
  var reverseArray = [];
  var len = reverseStart.length;
  for (let i = len-1; i>=0; i--) {
    reverseArray.push(reverseStart[i]);
  }

  var joinedArray = reverseArray.join('');

  if (replaced === joinedArray) {
    return true;
  } else {
    return false;
  }
}

palindrome("A man, a plan, a canal. Panama");