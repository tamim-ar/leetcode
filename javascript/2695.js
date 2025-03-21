class ArrayWrapper {
    constructor(nums) {
        this.nums = nums;
    }

    // Method to sum all elements of the array
    valueOf() {
        return this.nums.reduce((sum, num) => sum + num, 0);
    }

    // Method to convert the object to a string representation
    toString() {
        return `[${this.nums.join(',')}]`;
    }
}
