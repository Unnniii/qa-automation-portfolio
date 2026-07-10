import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def create_booking(payload):
    return requests.post(f"{BASE_URL}/booking", json=payload)


def get_booking(booking_id):
    return requests.get(f"{BASE_URL}/booking/{booking_id}")


def update_booking(booking_id, payload, token):
    return requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=payload,
        headers={"Cookie": f"token={token}"},
    )


def patch_booking(booking_id, partial, token):
    return requests.patch(
        f"{BASE_URL}/booking/{booking_id}",
        json=partial,
        headers={"Cookie": f"token={token}"},
    )


def delete_booking(booking_id, token):
    return requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers={"Cookie": f"token={token}"},
    )
