from wordit.reference import Reference, parse_reference


def test_parse_simple_reference():
    assert parse_reference("John 3:16") == Reference("John", 3, 16)
