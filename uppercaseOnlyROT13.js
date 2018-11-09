function rot13(str) {
  var preCipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  preCipher = preCipher.split('');
  var postCipher = 'NOPQRSTUVWXYZABCDEFGHIJKLM';
  postCipher = postCipher.split('');
  var strArr = str.split('');
  for (let i = 0; i<str.length; i++) {
    for (let j = 0; j<preCipher.length; j++) {
      if (strArr[i] == preCipher[j]) {
        strArr[i] = postCipher[j];
        break;
      }
    }
  }
  strArr = strArr.join('');
  return strArr;
}

console.log(rot13("THIS IS A TEST"))