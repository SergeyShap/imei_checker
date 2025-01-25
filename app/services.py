import json

import httpx
from httpx import HTTPStatusError


async def check_imei(imei: str, api_token: str) -> dict:
    print("imei: ", imei)
    print("api_token: ", api_token)
    url = "https://api.imeicheck.net/v1/checks"
    headers = {
        'Authorization': 'Bearer ' + api_token,
        'Content-Type': 'application/json'
    }

    body = json.dumps({
        "deviceId": f"{imei}",
        "serviceId": 1
    })
    try:
        async with httpx.AsyncClient() as client:
            print(body)
            response = await client.post(url, headers=headers, data=body)
            print(response.text)
            response.raise_for_status()  # Проверка на ошибки
            print(response.text)
            return response.json()
    except HTTPStatusError as e:
        print(f"Ошибка {e.response.status_code}: {e.response.text}")
        return None