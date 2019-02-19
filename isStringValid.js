let stringToValidate = "(hell)(oqwe(asfa)sfljr(wngke)))("

const isStringValid = stringToValidate => {
  let balance = 0;
  let stringArr = [...stringToValidate];
  for(let char of stringArr){
    if (char === '(') balance++;
    if (char === ')') balance--;
    if (balance < 0) break;
  }
  if(balance !== 0) return false;
  return true;
}
isStringValid(stringToValidate);