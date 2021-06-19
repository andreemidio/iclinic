from apps.users.models import Users


def test_create_user_with_username(db) -> None:
    user = Users.objects.create_user(fullname="Haki", email="haki@haki.com.br", password="haki@haki.com.br")
    assert user.email == "haki@haki.com.br"
