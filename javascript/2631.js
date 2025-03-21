Array.prototype.groupBy = function(fn) {
    return this.reduce((acc, item) => {
        const key = fn(item);
        (acc[key] ||= []).push(item);
        return acc;
    }, {});
};
