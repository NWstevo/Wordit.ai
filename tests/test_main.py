from wordit.__main__ import main


def test_approved_reference_goes_live(capsys):
    # The fake operator types a sentence, approves the suggestion, then stops the program.

    keys = ["Turn with me to John 3:16", "a", ""]

    def fake_operator(prompt):
        return keys.pop(0)

    main(read_input=fake_operator)
    shown = capsys.readouterr().out
    assert "LIVE: John 3:16" in shown
