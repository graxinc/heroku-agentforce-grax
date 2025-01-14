#!/bin/bash
curl -X POST https://heroku-agentforce-grax-01118551be31.herokuapp.com/query \
  -H "Content-Type: application/json" \
  -u heroku:agent \
  -d '{"query": "Show me the top 5 accounts by revenue"}'