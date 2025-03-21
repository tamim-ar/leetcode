var join = function(arr1, arr2) {
    const map = new Map();

    for (const obj of arr1) {
        map.set(obj.id, obj);
    }

    for (const obj of arr2) {
        map.set(obj.id, { ...map.get(obj.id), ...obj });
    }

    return Array.from(map.values()).sort((a, b) => a.id - b.id);
};
