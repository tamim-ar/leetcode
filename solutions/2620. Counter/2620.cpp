#include <iostream>
#include <functional>

/**
 * Creates a counter function that, when called, will return a number that
 * increments by 1 each time the counter function is called.
 *
 * @param initialCount The starting point for the counter.
 * @return A function object (lambda) that, when invoked, returns an incremented number.
 */
std::function<int()> createCounter(int initialCount) {
    // Variable 'currentCount' holds the current state of the counter.
    int currentCount = initialCount;

    // The returned function object (lambda) encapsulates the 'currentCount' variable.
    // Each time it is called, it increments the value of 'currentCount' by one,
    // then returns the updated value.
    // Captures 'currentCount' by reference so that the counter state persists across calls.
    return [&currentCount]() -> int {
        return currentCount++;
    };
}

// Example usage:
int main() {
    // Create a counter starting at 10.
    auto counter = createCounter(10);

    // The counter retains its state across calls because 'currentCount' is captured by reference.
    std::cout << counter() << std::endl; // Should output: 10
    std::cout << counter() << std::endl; // Should output: 11
    std::cout << counter() << std::endl; // Should output: 12

    return 0;
}