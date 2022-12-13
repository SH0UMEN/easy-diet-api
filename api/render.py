from rest_framework.exceptions import ErrorDetail
from djangorestframework_camel_case.render import CamelCaseJSONRenderer


class CamelCaseJSONStatusRenderer(CamelCaseJSONRenderer):
    def render(self, data, *args, **kwargs):
        return super().render(self.render_status(data), *args, **kwargs)

    def render_status(self, data):
        is_dict = isinstance(data, dict)
        result = {} if is_dict else []
        keys = data.keys() if is_dict else range(len(data))

        for key in keys:
            value = data[key]

            if isinstance(value, (dict, list)):
                value = self.render_status(value)
            elif isinstance(value, ErrorDetail):
                value = value.code

            if is_dict:
                result[key] = value
            else:
                result.append(value)

        return result
