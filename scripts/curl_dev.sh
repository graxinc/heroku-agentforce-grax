#!/bin/bash

curl -X POST http://localhost:5001/query \
  -H "Content-Type: application/json" \
  -u heroku:agent \
  -d '{"query": "Show me the top 5 accounts by revenue"}'