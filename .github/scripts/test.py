import json

test={
  "summary": [
    {
      "key1": "11",
      "key2": "modified",
      "key3": 92,
      "key4": "Excellent"
    },
    {
      "key1": "21",
      "key2": "added",
      "key3": 85,
      "key4": "Good"
    }
  ]
}


print(json.dumps({"summary": test}))
