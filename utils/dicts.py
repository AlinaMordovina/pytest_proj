def get_val(collection, key, default="git"):
    if not collection:
        return default
    else:
        for element in collection:
            if element == key:
                return collection[key]
            else:
                return default
