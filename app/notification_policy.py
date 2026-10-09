def plan_notification(event, preferences):
    return [{"user_id":event["user_id"],"channel":"email","event_id":event["id"]}]
