class ObjectPool:
    def __init__(self, object_type, max_objects=5):
        self.object_type = object_type
        self.max_objects = max_objects
        self._pool = []

    def acquire_object(self):
        if self._pool:
            return self._pool.pop()
        elif len(self._pool) < self.max_objects:
            return self.object_type()
        else:
            raise Exception("Maximum limit reached, cannot create more objects.")

    def release_object(self, obj):
        if len(self._pool) < self.max_objects:
            self._pool.append(obj)

class PooledObject:
    def __init__(self):
        self.property = None

    def use(self):
        print(f"Using object {id(self)}")

pool = ObjectPool(PooledObject, max_objects=3)

obj1 = pool.acquire_object()
obj1.use()

obj2 = pool.acquire_object()
obj2.use()

pool.release_object(obj1)
pool.release_object(obj2)

obj3 = pool.acquire_object()
obj3.use()

obj4 = pool.acquire_object()
obj4.use()
