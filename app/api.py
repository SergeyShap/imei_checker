from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from app.schemas import IMEICheckRequest, IMEICheckResponse
from app.services import check_imei
from app.config import settings

app = FastAPI()

api_key_header = APIKeyHeader(name="token")

async def authenticate(token: str = Depends(api_key_header)):
    print("Допустимые токены:", settings.api_auth_tokens_as_list)
    if token not in settings.api_auth_tokens_as_list:
        raise HTTPException(status_code=403, detail="Invalid token")

@app.post("/api/check-imei", response_model=IMEICheckResponse)
async def check_imei_api(request: IMEICheckRequest, token: str = Depends(authenticate)):
    if not request.imei.isdigit() or len(request.imei) != 15:
        raise HTTPException(status_code=400, detail="Invalid IMEI")

    result = await check_imei(request.imei, settings.imei_check_api_token)
    return {"imei": request.imei, "result": result}
