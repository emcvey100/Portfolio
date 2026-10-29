"""Page replacement algorithms: FIFO and LRU."""

from collections import OrderedDict, deque
from typing import Iterable, List, Tuple


def fifo(pages: Iterable[int], frame_count: int) -> Tuple[int, List[List[int]]]:
    """Return FIFO page faults and the frame state after each page request."""
    if frame_count < 1:
        raise ValueError("frame_count must be at least 1")

    frames = deque()
    states = []
    faults = 0

    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) == frame_count:
                frames.popleft()
            frames.append(page)
        states.append(list(frames))

    return faults, states


def lru(pages: Iterable[int], frame_count: int) -> Tuple[int, List[List[int]]]:
    """Return LRU page faults and the frame state after each page request."""
    if frame_count < 1:
        raise ValueError("frame_count must be at least 1")

    frames = OrderedDict()
    states = []
    faults = 0

    for page in pages:
        if page in frames:
            frames.move_to_end(page)
        else:
            faults += 1
            if len(frames) == frame_count:
                frames.popitem(last=False)
            frames[page] = None
        states.append(list(frames))

    return faults, states


def display(name: str, pages: List[int], frame_count: int) -> None:
    algorithm = fifo if name == "FIFO" else lru
    faults, states = algorithm(pages, frame_count)
    print(f"{name}: {faults} page faults")
    for page, state in zip(pages, states):
        print(f"  {page}: {state}")


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_count = 3
    display("FIFO", reference_string, frame_count)
    display("LRU", reference_string, frame_count)