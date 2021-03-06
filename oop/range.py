class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:                # special case of range(n)
            start, stop = 0, start      # should be treated as if range(0, n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out or range')

        return self._start + k * self._step

    def contains(self, k):
        """Return whether the range contains k or not."""
        return 0 <= k < self._length

for n in Range(10, None, 2):
    print(n),

r = Range(10)
print(r[-1])
print(r[10])
