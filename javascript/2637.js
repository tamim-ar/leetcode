function timeLimit(fn, t) {
    return async function (...args) {
      const timeout = new Promise((_, reject) =>
        setTimeout(() => reject('Time Limit Exceeded'), t)
      );
      const result = fn(...args);
      return Promise.race([timeout, result]);
    };
  }
  