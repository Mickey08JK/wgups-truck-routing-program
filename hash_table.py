class ChainingHashTable:
    """Simple separate-chaining hash table keyed by package ID."""

    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Map key to bucket index."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert new key/value pair, or update existing key in-place."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        self.table[index].append((key, value))  # Insert new key-value pair

    def search(self, key):
        """Return value for key, or None if key is not present."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value associated with the key
        return None  # Key not found

    def delete(self, key):
        """Remove key/value pair and return True when removed, else False."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True
        return False  # Key not found