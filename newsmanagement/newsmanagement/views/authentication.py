from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..services.authentication import check_authentication


@extend_schema(operation={
    "operationId": "api_login",
    "description": "User login",
    "tags": ["api"],
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "password": {"type": "string"}
                    }
                }
            },
        }
    },
    "responses": {
        "200": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "created_at": {"type": "string", "format": "date-time"},
                            "updated_at": {"type": "string", "format": "date-time"},
                            "email": {"type": "string", "maxLength": 255},
                            "username": {"type": "string", "maxLength": 255},
                            "fullname": {"type": "string", "maxLength": 128},
                            "token": {"type": "string", "maxLength": 40}
                        }
                    }
                }
            },
            "description": ""
        },
    }
})
@api_view(['POST'])
@permission_classes([])
def login(request):
    request_data = request.data.copy()
    results = check_authentication(request_data)
    return Response(results)

