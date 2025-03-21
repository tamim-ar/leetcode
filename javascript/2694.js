class EventEmitter {
    constructor() {
        this.events = {};  // Store events and their callbacks
    }
    
    subscribe(eventName, callback) {
        // Initialize the event's callback list if it doesn't exist
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        
        // Add the callback to the event's callback list
        this.events[eventName].push(callback);
        
        // Return an unsubscribe object
        return {
            unsubscribe: () => {
                // Find the index of the callback and remove it
                const index = this.events[eventName].indexOf(callback);
                if (index !== -1) {
                    this.events[eventName].splice(index, 1);
                }
                return undefined;  // As per the problem statement
            }
        };
    }
    
    emit(eventName, args = []) {
        // Check if the event has any listeners
        if (!this.events[eventName]) {
            return [];  // No listeners, return empty array
        }
        
        // Call all the subscribed callbacks and store their results
        const results = this.events[eventName].map(callback => callback(...args));
        return results;
    }
}
