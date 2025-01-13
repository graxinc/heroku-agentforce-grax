from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_anthropic import ChatAnthropic
from langchain.tools import BaseTool
from typing import Optional, Type, Any
import pandas as pd
from datalake import query

class DataLakeQueryTool(BaseTool):
    name: str = "datalake_query"
    description: str = """
    Useful for querying the GRAX data lake using SQL. Input should be a valid SQL query.
    The query will be executed against an Athena database containing Salesforce data.
    Use this tool when you need to retrieve data from the data lake.

    List table names to see the available tables.
    The datalake contains historical data tables that begin with object_ and then the object name, such as object_account

    Use a common table expression to get the latest data, for example:

    SELECT A.*
    FROM
    (datalake.object_lead A
    INNER JOIN (
    SELECT
        B.Id
    , Max(B.grax__idseq) Latest
    FROM
        datalake.object_lead B
    GROUP BY B.ID
    )  B ON ((A.Id = B.Id) AND (A.grax__idseq = B.Latest)))
    WHERE (A.grax__deleted IS NULL)

    to get the latest data for the lead object.
    Use this technique for any object that has a grax__idseq column.
    Do not use sql code block markers in your query.
    """

    def _run(self, sql_query: str) -> str:
        try:
            df = query(sql_query)

            if len(df) == 0:
                return "Query executed successfully but returned no results."

            return df.to_string()
        except Exception as e:
            return f"Error executing query: {str(e)}"

    def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented")

def create_agent(api_key: str):
    """
    Creates a LangChain agent with the DataLakeQueryTool

    Args:
        api_key (str): API key for the language model

    Returns:
        Agent: Initialized LangChain agent
    """
    # Initialize the language model
    llm = ChatAnthropic(
        temperature=0,
        model_name="claude-3-5-sonnet-20240620",
        anthropic_api_key=api_key
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
