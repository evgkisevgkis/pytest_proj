from utils import dicts


def test_get_val():
    data = {1: "a", 2: "b", 3: "c"}
    assert dicts.get_val(data, 2) == "b"
    data = {}
    assert dicts.get_val(data, 1) == "git"
    assert dicts.get_val(data, 1, "uuo") == "uuo"
