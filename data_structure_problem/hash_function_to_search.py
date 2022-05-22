class Hashtable:
    def __init__(self, items):
        self.bucket_size = len(items)
        self.buckets = [[] for i in range(self.bucket_size)]
        self.assign_buckets(items)

    def assign_buckets(self, items):
        """
        function for getting proper hash code and assign to respective index
        :param items: item to insert in key
        :return: generate hash code and append item
        """
        for key, value in self.buckets:
            hash_value = hash(key)
            index = hash_value % self.bucket_size
            self.buckets[index].append((key, value))

    def search_value(self, input_keys):
        """
        function for search particular value in table
        :param input_keys: searched item
        :return: true or false
        """
        hash_value = hash(input_keys)
        index = hash_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_keys:
                return value


if __name__ == "__main__":
    lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ht = Hashtable(lt)
    ht.assign_buckets(lt)
    print(ht.search_value(6))
