from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from typing import Optional, Type, Any
import pandas as pd
from datalake import query

class DataLakeQueryTool(BaseTool):
    name: str = "datalake_query"
    description: str = """
    Useful for querying the GRAX data lake using SQL. Input should be a valid SQL query.
    The query will be executed against an Athena database containing Salesforce data.
    Common tables include Account, Contact, Opportunity, and other Salesforce objects.
    Use this tool when you need to retrieve data from the data lake.
    """

    def _run(self, sql_query: str) -> str:
        try:
            # Basic SQL injection prevention
            dangerous_keywords = ['DROP', 'DELETE', 'TRUNCATE', 'UPDATE', 'INSERT']
            if any(keyword in sql_query.upper() for keyword in dangerous_keywords):
                return "This query type is not allowed for safety reasons."

            df = query(sql_query)

            if len(df) == 0:
                return "Query executed successfully but returned no results."

            return df.to_string()
        except Exception as e:
            return f"Error executing query: {str(e)}"

    def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")

def create_agent(openai_api_key: str):
    """
    Creates a LangChain agent with the DataLakeQueryTool

    Args:
        openai_api_key (str): OpenAI API key for the language model

    Returns:
        Agent: Initialized LangChain agent
    """
    # Initialize the language model
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        openai_api_key=openai_api_key
    )

    # Create the datalake query tool
    datalake_tool = DataLakeQueryTool()

    # Create a list of tools
    tools = [
        Tool(
            name="datalake_query",
            func=datalake_tool._run,
            description=datalake_tool.description
        )
    ]

    # Add system instructions
    system_message = """You are a helpful data analyst assistant that helps users query a Salesforce data lake.
    The data lake contains standard Salesforce objects like Account, Contact, Opportunity, etc.
    When users ask questions, convert them to SQL queries and use the datalake_query tool to get results.
    Always format your responses clearly and explain the results in a user-friendly way.
    If you encounter errors, provide helpful explanations about what might have gone wrong."""

    # Initialize the agent with system message
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        system_message=system_message
    )

    return agent

def query_agent(agent, query: str) -> str:
    """
    Use the agent to process a natural language query and get results from the data lake

    Args:
        agent: The initialized LangChain agent
        query: Natural language query string

    Returns:
        str: Response from the agent
    """
    try:
        response = agent.run(query)
        return response
    except Exception as e:
        return f"Error processing query: {str(e)}"
