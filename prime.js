// Function to check if a number is prime
function isPrime(num) {
    if (num <= 1) return false; //if number is less than equal to 1 then it's not prime so return false
    for (let i = 2; i < num; i++) {  //start from 2 and iterate till one less than the number
      if (num % i === 0) {
        return false;   //if number is divisible by any of the number return false
      }
    }
    return true;  //otherwise return true
  }
  
  // Function to find the next prime number after x
  function nextPrime(num) {
    let next = num + 1; //start from one greater than given number
    while (!isPrime(next)) {   //iterate until next is prime
      next++;
    }
    return next;  //return the next prime number
  }
  
  let num = prompt("Enter a number:");  //prompt the user for input
  num = parseInt(num);  //convert the input string to integer
  
  if (isPrime(num)) {   //check if the number is prime or not
    console.log(`The number ${num} is prime.`);
  } else {
    let nextPrimeNum = nextPrime(num);  //find the next prime number
    console.log(`The number ${num} is not prime.`);
    console.log(`The next prime number after ${num} is ${nextPrimeNum}.`);
    console.log(`The difference between ${nextPrimeNum} and ${num} is ${nextPrimeNum - num}.`);
    //Find the difference and print out the difference
  }
  