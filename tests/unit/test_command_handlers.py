from pytest import mark


@mark.parametrize(
        "args,expected",
        (
            (, "[Q]uick Commands\n"),
            ("B", "[B]BS\n"),
        )
)
def test_build_menu_items(args, expected):
    pass
