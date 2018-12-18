function checkCashRegister(price, cash, cid) {
  var change = cash - price;
  var changeValues = [100, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01];
  var cashInRegister = cid.reverse();
  var totalCash = 0;
  var finalChange = [];
  var returnToCustomer = {status: "", change: [["ONE HUNDRED", 0], ["TWENTY", 0], ["TEN", 0], ["FIVE", 0], ["ONE", 0], ["QUARTER", 0], ["DIME", 0], ["NICKEL", 0], ["PENNY", 0]]};
  console.log(totalCash)
  for (let i = 0; i<cid.length; i++) {
    totalCash += cashInRegister[i][1];
    if (i < 5) {
      cashInRegister[i][1] = Math.round(cashInRegister[i][1]/changeValues[i]);
    } else {
      cashInRegister[i][1] = Math.round((cashInRegister[i][1] * 100)/(changeValues[i]*100))
    }
  }
  console.log(cashInRegister[1])
  if(change > totalCash) {
    returnToCustomer.status = "INSUFFICIENT_FUNDS";
    returnToCustomer.change = [];
  } else if (change == totalCash) {
    returnToCustomer.status = "CLOSED";
    for (let i = 0; i<cid.length; i++) {
      if (change >= changeValues[i] && cashInRegister[i][1]>=0.01) {
        cashInRegister[i][1]-=1;
        returnToCustomer.change[i][1]+=changeValues[i] * 100;
        change -=changeValues[i];
        change = parseFloat(change).toFixed(2);
        i--;
      }
      if (i == cid.length-1) {
        returnToCustomer.change[i][1]/=100;
        returnToCustomer.change = returnToCustomer.change.reverse();
      }
    } return returnToCustomer;
    } else if (change < totalCash) {
    returnToCustomer.status = "OPEN";
    for (let i = 0; i<cid.length; i++) {
      if (change >= changeValues[i] && cashInRegister[i][1]>=0.01) {
        cashInRegister[i][1]-=1;
        returnToCustomer.change[i][1]+=changeValues[i];
        change -=changeValues[i];
        change = parseFloat(change).toFixed(2);
        i--;
      }
    }
  }
  if (change != 0) {
    returnToCustomer.status = "INSUFFICIENT_FUNDS";
    returnToCustomer.change = [];
  }
  for (let i = 0; i<returnToCustomer.change.length; i++) {
     if (returnToCustomer.change[i][1]>=0.01) {
       finalChange.push(returnToCustomer.change[i]);
    }
  }
  returnToCustomer.change = finalChange;
  console.log(returnToCustomer.change);
  console.log(returnToCustomer);
  return returnToCustomer;
}


checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);