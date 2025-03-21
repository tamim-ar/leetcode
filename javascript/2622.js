class TimeLimitedCache {
    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        let exists = this.cache.has(key);
        if (exists) clearTimeout(this.cache.get(key).timeout);
        
        let timeout = setTimeout(() => this.cache.delete(key), duration);
        this.cache.set(key, { value, timeout });

        return exists;
    }

    get(key) {
        return this.cache.has(key) ? this.cache.get(key).value : -1;
    }

    count() {
        return this.cache.size;
    }
}
