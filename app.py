"""
Agentforce Action API

This module implements a simple Flask-based API for handling agent requests for the GRAX datalake
The API provides a single endpoint (`/query`) that accepts a JSON payload containing a plain language
query for the datalake and uses a langchain agent to run the query, returning an answer for the user,

Key Features:
- Implements HTTP Basic Authentication to protect the `/query` endpoint.
- Utilizes Flask-RESTx for API documentation and validation.
- Logs incoming requests and query activity for debugging purposes.

Classes:
    AgentRequest: Represents an agent request containing a query.
    AgentResponse: Represents a response to the agent with a message.

Endpoints:
    POST /process:
        - Input: JSON payload containing a `query` field.
        - Output: JSON payload containing a response.

Usage:
    - Run the application with `python <filename>.py`.
    - The server listens on the port specified in the `PORT` environment variable or defaults to 5000.
    - Use an HTTP client (e.g., Postman, curl) to interact with the `/query` endpoint.

Dependencies:
    - Flask
    - Flask-RESTx
    - Flask-HTTPAuth
    - Werkzeug (for password hashing)
    - badgecreator (external module for badge generation)
"""
import logging
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
from flask_restx import Api, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
from agent import create_agent, query_agent


app = Flask(__name__)
api = Api(app,
          title='GRAX Agentforce Action',
          description="GRAX Agentforce Action example",
          version='0.1.0'
          )

auth = HTTPBasicAuth()

# Define a hardcoded user with a hashed password
users = {
    "heroku": generate_password_hash("agent")
}

# Verify the username and password
@auth.verify_password
def verify_password(username, password):
    """
    Verifies a user's credentials using HTTP Basic Auth.

    Parameters:
        username (str): The provided username.
        password (str): The provided password.

    Returns:
        str: The username if the authentication succeeds, otherwise None.
    """
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file if it exists
load_dotenv()

class AgentRequest:
    """
    Represents an agent request containing a query.

    Attributes:
        query (str): The name included in the request.
    """
    def __init__(self, query):
        self.query = query

class AgentResponse:
    """
    Represents a response to an agent request.

    Attributes:
        message (str): The response message.
    """
    def __init__(self, message):
        self.message = message

    def to_dict(self):
        """
        Converts the agent_response object to a dictionary.

        Returns:
            dict: A dictionary representation of the agent_response.
        """
        return {"message": self.message}

# Define the AgentRequest model for the input
agent_request_model = api.model('AgentRequest', {
    'query': fields.String(
        required=True,
        description='A query from the agent request',
        default="What are the tables in the datalake?"  # Default value for the OpenAPI schema
    )
})

# Define the AgentResponse model for the output
agent_response_model = api.model('AgentResponse', {
    'message': fields.String(
        required=True,
        description='A response to the agent'
    )
})

# API Routes
@api.route('/query')
class Process(Resource):
    """
    RESTful resource for processing agent requests and returning a response.
    """

    @auth.login_required  # Protect the endpoint with HTTP Basic Auth
    @api.expect(agent_request_model)  # Use the model here
    @api.response(200, 'Success', agent_response_model)  # Define the response model here
    def post(self):
        """
        Handles POST requests to process an agent request.
        """
        # Parse the JSON data from the request body
        data = request.json
        if not data or 'query' not in data:
            response = make_response(jsonify({"error": "Invalid request, 'query' field is required"}))
            response.status_code = 400
            response.headers['Content-Type'] = 'application/json'
            return response

        # Create MyRequest instance from JSON data
        agent_request = AgentRequest(data['query'])
        logger.info("Received query: %s", agent_request.query)

        try:
            # Create and use the agent
            openai_api_key = os.getenv('OPENAI_API_KEY')
            if not openai_api_key:
                logger.error("OPENAI_API_KEY environment variable is not set")
                return make_response(
                    jsonify({"error": "OpenAI API key not configured"}),
                    500
                )

            agent = create_agent(openai_api_key)
            message = query_agent(agent, agent_request.query)

        except Exception as e:
            logger.error("Error running query: %s", str(e))
            return make_response(
                jsonify({"error": f"Error running query: {str(e)}"}),
                500
            )

        agent_response = AgentResponse(message)
        logger.info("Result is: %s", agent_response)
        return agent_response.to_dict()

if __name__ == '__main__':
    """
    Entry point for the application. Starts the Flask server and runs the application.
    """
    # Use the PORT environment variable if present, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
