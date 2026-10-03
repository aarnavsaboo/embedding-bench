def batches(items:list, size:int):
    if size<1:
        raise ValueError("batch size must be positive")
    for start in range(0,len(items),size):
        yield items[start:start+size]
