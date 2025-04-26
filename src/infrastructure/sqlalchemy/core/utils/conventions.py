import re


class NamingConvention:
    @staticmethod
    def camel_to_snake(class_name: str) -> str:
        class_name = re.sub(r"(Model)$", "", class_name)
        snake_case_name = re.sub(r"(?<!^)(?=[A-Z])", "_", class_name).lower()
        return snake_case_name
