import logging
from typing import Union
from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from db import forms
from models import DBForm, Form, SuccessResponse
from utils import data_to_bd, check_result, get_from_db, type_form

logger = logging.getLogger(__name__)

router = APIRouter(prefix='/api/v1')


@router.get("/create_collection")
async def create():
    forms.drop()
    result = forms.insert_many(data_to_bd)
    x = list()
    for i in forms.find():
        i.pop('_id')
        x.append(i)
    return {"message": x}


@router.post("/get_form")
async def get_form(
        body: dict = Body(...)
) -> JSONResponse:

    logger.info(body)

    conditions = await type_form(body)
    if not conditions:
        return JSONResponse(content="Не задана форма для поиска", status_code=400)

    logger.info(conditions)

    result_from_db = await get_from_db(conditions)

    if result_from_db:
        check = await check_result(result_from_db, conditions)
        logger.info(check)
        if check:
            return JSONResponse(content=result_from_db.get('name', 'Не указано'), status_code=200)
        else:
            return JSONResponse(content=conditions, status_code=200)
