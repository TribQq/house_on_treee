from starlette.testclient import TestClient

from house_on_treee.views.views import app

test_client = TestClient(app=app)


def test_create_chirp():
    expected_422_err_response = test_client.post(url='/create')
    assert expected_422_err_response.status_code == 422

    example_data = {
        "author": {
            "name": "string",
            "born_date": "2023-05-27T18:43:31.038Z",
            "description": "string",
            "sex": "string"
        },
        "text": "string",
        "publish_date": "2023-05-27T18:43:31.038Z",
        "is_draft": True,
        "is_deleted": True
    }
    valid_response = test_client.post(url='/create', json=example_data)
    assert valid_response.status_code == 200
    print(f'RESP: {valid_response}')




