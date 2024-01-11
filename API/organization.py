from .until import get_value


def get_sub_organization(self, iid_org):
    payload = {
        "type": "organization",
        "depth": 0,
        "pIids[]": iid_org,
        "sub_type": 1,
    }
    response = self.send("/organization/api/search", payload)
    return get_value(input_data=response, key="result", default=[])
