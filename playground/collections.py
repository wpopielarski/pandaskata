from typing import List


def sum(collection: List[int]) -> int:
    if not collection: return 0
    (head, *tail) = collection 
    return head + sum(tail)
