
def parse_score(text):
    """Parse two non-negative integer scores separated by a hyphen."""

    # Check input type
    if not isinstance(text, str):
        raise TypeError("Score must be a string")

    # Split the score
    parts = text.split('-')

    # Check number of values
    if len(parts) != 2:
        raise ValueError("Score must contain exactly two values")

    a, b = parts

    # Check for empty values
    if not a.strip() or not b.strip():
        raise ValueError("Both score values must be provided")

    # Convert values into integers
    try:
        first = int(a.strip())
        second = int(b.strip())
    except ValueError:
        raise ValueError("Score values must be integers")

    # Reject negative scores
    if first < 0 or second < 0:
        raise ValueError("Scores cannot be negative")

    return first, second


def game_lead(text):
    """Calculate the difference between two valid tennis point scores."""

    # Check input type
    if not isinstance(text, str):
        raise TypeError("Game score must be a string")

    # Split the score
    parts = text.split('-')

    # Check number of values
    if len(parts) != 2:
        raise ValueError("Game score must contain exactly two values")

    # Valid tennis point scores
    points = {
        '0': 0,
        '15': 1,
        '30': 2,
        '40': 3
    }

    first, second = parts

    first = first.strip()
    second = second.strip()

    # Validate both point scores
    if first not in points or second not in points:
        raise ValueError("Invalid tennis point score")

    return points[first] - points[second]


def set_spread(games_csv):
    """Calculate the difference between maximum and minimum game counts."""

    # Check input type
    if not isinstance(games_csv, str):
        raise TypeError("Games must be provided as a string")

    # Reject empty input
    if not games_csv.strip():
        raise ValueError("Games input cannot be empty")

    # Convert CSV values into integers
    try:
        games = [int(g.strip()) for g in games_csv.split(',')]
    except ValueError:
        raise ValueError("All game counts must be integers")

    # Reject negative game counts
    if any(g < 0 for g in games):
        raise ValueError("Game counts cannot be negative")

    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    print("Spread:", result)


if __name__ == "__main__":
    main()
