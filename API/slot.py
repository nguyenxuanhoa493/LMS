def update_status(self, id_slot, status="approved"):
    # status: approved or queued
    payload = {"id": id_slot, "_sand_step": "status", "status": status}
    response = self.send("/slot/api/update", payload)


def new(self, name_slot, start_time, end_time):
    payload = {"name": name_slot, "start_time": start_time, "end_time": end_time}
    response = self.send("/slot/api/new", payload)
    id_slot = response["result"]["id"]
    update_status(self, id_slot)
