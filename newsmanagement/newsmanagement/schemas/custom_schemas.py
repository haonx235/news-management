from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter, OpenApiExample


class CustomAutoSchema(AutoSchema):
    global_params = [
        OpenApiParameter(name="Authorization", type=str, required=True, examples=[
            OpenApiExample('Example 1', value='Token 401f7ac837da42b97f613d789819ff93537bee6a')
        ], location=OpenApiParameter.HEADER, description="Authorization token")
    ]

    def get_override_parameters(self):
        params = super().get_override_parameters()
        return params + self.global_params
