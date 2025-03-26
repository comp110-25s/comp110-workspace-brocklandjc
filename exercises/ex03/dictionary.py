"""Practicing Dictionary Functions."""

_author_: str = "730470079"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of the given dictionary."""
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate key detected when inverting: {value}")
        inverted_dict[value] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    """Count the occurrences of each unique string in the given list."""
    count_dict = {}
    for item in values:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color(favorites: dict[str, str]) -> str:
    """Return the most common favorite color from the given dictionary."""
    color_counts = count(list(favorites.values()))
    max_count = max(color_counts.values())
    for color in favorites.values():
        if color_counts[color] == max_count:
            return color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bin words by their lengths into a dictionary."""
    length_bins = {}
    for word in words:
        length = len(word)
        if length not in length_bins:
            length_bins[length] = set()
        length_bins[length].add(word)
    return length_bins


# Example usage
if __name__ == "__main__":
    print(invert({"a": "z", "b": "y", "c": "x"}))  # {'z': 'a', 'y': 'b', 'x': 'c'}
    print(invert({"apple": "cat"}))  # {'cat': 'apple'}
    try:
        print(invert({"kris": "jordan", "michael": "jordan"}))  # Should raise KeyError
    except KeyError as e:
        print(f"KeyError: {e}")

    print(
        count(["apple", "banana", "apple", "orange", "banana", "banana"])
    )  # {'apple': 2, 'banana': 3, 'orange': 1}

    print(
        favorite_color(
            {
                "Alice": "blue",
                "Bob": "red",
                "Charlie": "blue",
                "David": "green",
                "Eve": "red",
            }
        )
    )  # 'blue' or 'red' (whichever appears first)

    print(bin_len(["the", "quick", "fox"]))  # {3: {"the", "fox"}, 5: {"quick"}}
    print(bin_len(["the", "the", "fox"]))  # {3: {"the", "fox"}}
