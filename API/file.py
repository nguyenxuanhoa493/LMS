def upload(self, file_path):
    payload = {}
    files = {"file": open(file_path, "rb")}
    response = self.send("/file/upload", payload, files=files)
    file_uploaded = response["result"]["attachments"][0]
    print(f">>> Uploaded: {file_path} > {file_uploaded['link']}")
    return file_uploaded
