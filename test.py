from app import index, get_user


def test_index():
    assert index()=="Welcome to Flask Python"


def test_get_user():
    user = get_user()
    assert user["Name"]=="Python"
    assert user["Age"]==2023


if __name__ == "__main__":
    test_index()
    test_get_user()