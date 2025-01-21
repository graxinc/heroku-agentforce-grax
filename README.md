# GRAX Agentforce Action

A Flask API service that enables natural language querying of Salesforce data in the GRAX data lake.
The service uses LangChain and Claude to answer natural language questions from Agentforce about your current and historical Salesforce data.

## Installation


[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://www.heroku.com/deploy/?template=https://github.com/graxlabs/heroku-agentforce-grax/tree/main)

## Setup

### Environment Variables

Required environment variables can be set in your environment or in a `.env` file:

```bash
# Grax
GRAX_DATALAKE_URL=      # URL connection to GRAX Datalake

# Claude API
ANTHROPIC_API_KEY=      # Your Anthropic API key for LLM access

# Database
DATABASE_URL=           # URL connection to postgres database

# Google OAuth
GOOGLE_CLIENT_ID=        # Google OAuth 2.0 Client ID
GOOGLE_CLIENT_SECRET=    # Google OAuth 2.0 Client Secret
SECRET_KEY=              # Flask secret key for sessions

# Optional
PORT=5001                # Server port (default: 5001)

```

### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create the database
(Assumes you have a postgres instance at DATABASE_URL)
```bash
python create_db.py
```

3. Start the server:

```bash
python app.py
```

### Usage Example

You can query the API using curl:

```bash
curl -X POST http://localhost:5001/query \
  -H "Content-Type: application/json" \
  -u heroku:agent \
  -d '{"query": "Show me the top 5 accounts by revenue"}'
```

The API will return a JSON response containing the natural language answer to your question.