from schema.schema_response import Response
from time import time
from fastapi import APIRouter, HTTPException, UploadFile, File
from dependencies import (
    MODEL_PATH,
    MODEL_DOCKER,
    CLASS_NAMES
)
from utils.deteksi import (
    upload_file,
    loadModel,
    detect_img
)

router = APIRouter(tags=['detection'])

async def endpoint_kue(document: UploadFile = File(...)):
    result = {}
    try:
        start_time = time()
        image_path = upload_file(document)
        model = loadModel(MODEL_DOCKER) #TODO: separate between development and production MODEL_PATH
        cake_name = detect_img(img_path=image_path, model=model, class_names=CLASS_NAMES)
        end_time = time()
        process_time = end_time - start_time
        result['nama_kue'] = cake_name
        result['process_time'] = process_time
        response = Response(
            status_code=200,
            message="success",
            body=result
        )
    except (Exception, HTTPException) as e:
        response = Response(
            status_code=401,
            message=str(e),
            body={}
        )
    return response

router.add_api_route(
    methods=["POST"],
    path="/deteksi_kue", response_model=Response,
    endpoint=endpoint_kue
)