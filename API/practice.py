def update_practice_correct_count(self, iid_user, iid_sco, correct_count, created_ts):
    payload = {
        "user_iid": iid_user,
        "sco_iid": iid_sco,
        "correct_count": correct_count,
        "created_ts": created_ts,
    }
    response = self.send("/practice/data/update-practice-correct-count", payload)
    print(response)
