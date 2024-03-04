"""EX05 - Dictionary assignment element."""

__author__ = "730710373"

def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Pretend this was a meaningful docstring."""
    inverted_dict: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("More than one key maps to the same value.")
        inverted_dict[value] = key
    return inverted_dict

def favorite_color(colors: dict[str, str]) -> str:
    """Pretend this was a meaningful docstring."""
    color_count: dict[str, int] = {}
    for color in colors.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_count = max(color_count.values())
    most_popular_colors = [color for color, count in color_count.items() if count == max_count]
    if most_popular_colors:
        return most_popular_colors[0]
    else:
        return "No favorite color found."

def count(values: list[str]) -> dict[str, int]:
    """Pretend this was a meaningful docstring."""
    counts: dict[str, int] = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Pretend this was a meaningful docstring."""
    categorized_words: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter in categorized_words:
            categorized_words[first_letter].append(word)
        else:
            categorized_words[first_letter] = [word]
    return categorized_words

def update_attendance(attendance_log: dict[str, list[str]], day_of_week: str, student: str) -> None:
    """Pretend this was a meaningful docstring."""
    if day_of_week in attendance_log:
        attendance_log[day_of_week].append(student)
    else:
        attendance_log[day_of_week] = [student]