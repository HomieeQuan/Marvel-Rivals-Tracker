import json, time, uuid

event = {
  "matchId": str(uuid.uuid4()),
  "playerId": "YourGamerTag",
  "hero": "Iron Man",
  "action": "kill",
  "timestamp": int(time.time()*1000)
}
print(json.dumps(event))
