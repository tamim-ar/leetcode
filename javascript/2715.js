function cancellable(fn, args, t) {
    const timeoutId = setTimeout(() => fn(...args), t);
    return () => clearTimeout(timeoutId);
  }
  