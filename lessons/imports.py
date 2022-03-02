"""Examples of importing python."""


from lessons import helpers
from lessons import helpers as hp  # alias


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")


if __name__ == "__main__":
    main()