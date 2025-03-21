var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let results = [];
        let count = 0;
        let hasRejected = false;

        functions.forEach((fn, index) => {
            fn()
                .then(value => {
                    if (hasRejected) return;
                    results[index] = value;
                    count++;
                    if (count === functions.length) {
                        resolve(results);
                    }
                })
                .catch(error => {
                    if (!hasRejected) {
                        hasRejected = true;
                        reject(error);
                    }
                });
        });
    });
};
