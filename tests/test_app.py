"""Test if the home page returns status code 200 and contains expected content"""
def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data or b"Rero+" in response.data

""" Test if the help page returns status code 200 and contains expected content"""
def test_help_status_code(client):
    response = client.get("/help")
    assert response.status_code == 200
    assert b"Aide" in response.data or b"Help" in response.data

"""  Test if the 404 error handler returns status code 404 and contains expected content"""
def test_404_status_code(client):
    response = client.get("/nonexistent_page")
    assert response.status_code == 404
    assert b"Page not found" in response.data 
