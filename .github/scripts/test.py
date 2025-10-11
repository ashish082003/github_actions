import json

test={
  "summary": [
    {
      "key1": "src/main.py",
      "key2": "modified",
      "key3": 92,
      "key4": "Excellent"
    },
    {
      "key1": "app/routes.py",
      "key2": "added",
      "key3": 85,
      "key4": "Good"
    }
  ]
}


print(json.dumps({"summary": test}))
