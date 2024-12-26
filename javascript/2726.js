class Calculator {
    constructor(value) {
        this.result = value;
    }

    add(value) {
        this.result += value;
        return this; // Return current instance for method chaining
    }

    subtract(value) {
        this.result -= value;
        return this; // Return current instance for method chaining
    }

    multiply(value) {
        this.result *= value;
        return this; // Return current instance for method chaining
    }

    divide(value) {
        if (value === 0) {
            throw "Division by zero is not allowed"; // Handle division by zero
        }
        this.result /= value;
        return this; // Return current instance for method chaining
    }

    power(value) {
        this.result = Math.pow(this.result, value);
        return this; // Return current instance for method chaining
    }

    getResult() {
        return this.result;
    }
}





AAAAAAaa
