class Calculator {
    constructor(value) {
        this.result = value;
    }

    add(value) {
        this.result += value;
        return this; 
    }

    subtract(value) {
        this.result -= value;
        return this; 
    }

    multiply(value) {
        this.result *= value;
        return this; 
    }

    divide(value) {
        if (value === 0) {
            throw "Division by zero is not allowed"; 
        }
        this.result /= value;
        return this; 
    }

    power(value) {
        this.result = Math.pow(this.result, value);
        return this; 
    }

    getResult() {
        return this.result;
    }
}


// Example usage:const calc = new Calculator(10);
console.log(calc.add(5).subtract(2).multiply(3).divide(2).power(2).getResult()); // Output: 169.0
// This code defines a Calculator class with methods for basic arithmetic operations and chaining.      
// The example usage demonstrates how to create an instance of the Calculator and perform a series of operations, returning the final result.