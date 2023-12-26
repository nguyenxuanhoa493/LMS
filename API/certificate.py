def new(self, name_cer, code_cer, id_cer_template):
    payload = {
        "name": name_cer,
        "code": code_cer,
        "type": "syllabus_pass",
        "certificate_template_ids[0]": id_cer_template,
    }
    response = self.send("/certificate/index/new", payload)
