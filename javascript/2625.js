var flat = function (arr, n) {
    let result = [];

    const flatten = (array, depth) => {
        if (depth >= n) {
            result.push(...array);
            return;
        }

        for (let item of array) {
            if (Array.isArray(item)) {
                flatten(item, depth + 1);
            } else {
                result.push(item);
            }
        }
    };

    if (n === 0) {
        return arr;
    }

    flatten(arr, 0);
    return result;
};
