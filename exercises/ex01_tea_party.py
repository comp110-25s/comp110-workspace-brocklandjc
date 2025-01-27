"""Calculates the number of teabags, treats and expected cost for a tea party based on the amount of guests."""

__author__: str = "730470079"


def main_planner(guests: int) -> None:
    """Number of people attending the party."""
    print(f"A Cozy Tea Party For {guests} People!")
    print(f"Tea bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    """Calculates the number of teabags per guest."""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats per guest based on the amount of teabags."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of teabags and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
