class ReversedSequenceIterator:
    """A reversed iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    it = ReversedSequenceIterator(lst)
    for n in it:
        print(n),

