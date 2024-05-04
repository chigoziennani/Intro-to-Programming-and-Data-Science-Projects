"""Entry point for simulating a river ecosystem."""

__author__ = "730710373"

from exercises.ex09.river import River


def main():
    """Entry point for simulating a river ecosystem."""
    my_river = River(num_fish=10, num_bears=2)
    my_river.view_river()
    my_river.one_river_week()
    my_river.view_river()


if __name__ == "__main__":
    main()