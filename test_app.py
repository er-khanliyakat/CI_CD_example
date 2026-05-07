from app import login
def test_login_success():
    assert login("1234") == "Login successful"

def test_login_failure():
    assert login("wrongpassword") == "Login failed"
print("hello"