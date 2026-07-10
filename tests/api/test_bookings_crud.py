from utils import api_client
from utils.test_data import valid_booking


def test_booking_lifecycle(api_token):
    payload = valid_booking()

    created = api_client.create_booking(payload)
    assert created.status_code == 200
    booking_id = created.json()["bookingid"]

    got = api_client.get_booking(booking_id)
    assert got.status_code == 200
    assert got.json()["firstname"] == payload["firstname"]

    payload["firstname"] = "Updated"
    put = api_client.update_booking(booking_id, payload, api_token)
    assert put.status_code == 200
    assert api_client.get_booking(booking_id).json()["firstname"] == "Updated"

    patch = api_client.patch_booking(booking_id, {"lastname": "Patched"}, api_token)
    assert patch.status_code == 200
    assert api_client.get_booking(booking_id).json()["lastname"] == "Patched"

    deleted = api_client.delete_booking(booking_id, api_token)
    assert deleted.status_code in (200, 201)  # restful-booker returns 201 on delete
    assert api_client.get_booking(booking_id).status_code == 404
