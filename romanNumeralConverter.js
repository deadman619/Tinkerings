function convertToRoman(num) {
    var stringed = num.toString();
    var fullRoman;

    function hundredsRoman(hundreds) {
        if (hundreds == 4) {
            return 'CD';
        } else if (hundreds == 9) {
            return 'CM';
        } else if (hundreds >= 5) {
            let counter = hundreds - 5;
            let romanString = 'D' + 'C'.repeat(counter);
            return romanString;
        } else {
            return 'C'.repeat(hundreds);
        }
    }

    function tensRoman(tens) {
        if (tens == 4) {
            return 'XL';
        } else if (tens == 9) {
            return 'XC';
        } else if (tens >= 5) {
            let counter = tens - 5;
            let romanString = 'L' + 'X'.repeat(counter);
            return romanString;
        } else {
            return 'X'.repeat(tens);
        }
    }

    function singlesRoman(singles) {
        if (singles == 4) {
            return 'IV';
        } else if (singles == 9) {
            return 'IX';
        } else if (singles >= 5) {
            let counter = singles - 5;
            let romanString = 'V' + 'I'.repeat(counter);
        return romanString;
        } else {
            return 'I'.repeat(singles);
        }
    }

    if (stringed.length > 4) {
        console.log("This function only supports up to 4 digits");
    } else if (stringed.length == 4) {
        var firstRoman = 'M'.repeat(stringed[0]);
        fullRoman = firstRoman + hundredsRoman(stringed[1]) + tensRoman(stringed[2]) + singlesRoman(stringed[3]);
        console.log(fullRoman)
    } else if (stringed.length == 3) {
        fullRoman = hundredsRoman(stringed[0]) + tensRoman(stringed[1]) + singlesRoman(stringed[2]);
        console.log(fullRoman)
    } else if (stringed.length == 2) {
        fullRoman = tensRoman(stringed[0]) + singlesRoman(stringed[1]);
        console.log(fullRoman)
    } else if (stringed.length == 1) {
        fullRoman = singlesRoman(stringed[0]);
        console.log(fullRoman)
    } 
 return fullRoman;
}

convertToRoman(8291);