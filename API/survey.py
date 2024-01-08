def add_surveys_to_applied_item(self, iid_item, iid_survey):
    payload = {
        "applied_position": "end",
        "survey_iids[0]": iid_survey,
        "item_iids[0]": iid_item,
        "type": "course",
        "_sand_step": "add_surveys_to_applied_item",
        "apply_for_all_session": 0,
    }
    response = self.send("/survey/api/add-applied-items", payload)
    print(response)
