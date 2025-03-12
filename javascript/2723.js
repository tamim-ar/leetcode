async function addTwoPromises(promise1, promise2) {
    const [result1, result2] = await Promise.all([promise1, promise2]);
    return result1 + result2;
  }
  