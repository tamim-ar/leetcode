function cancellable(fn, args, t) {
    fn(...args); // Immediate invocation
    const intervalId = setInterval(() => fn(...args), t); // Schedule subsequent invocations
    return () => clearInterval(intervalId); // Return cancel function
  }
  