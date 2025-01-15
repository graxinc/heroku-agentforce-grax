from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_anthropic import ChatAnthropic
from langchain.tools import BaseTool
from typing import Optional, Type, Any, Dict, List
import pandas as pd
from datalake import query
from langchain.callbacks.base import BaseCallbackHandler

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

class LoggingCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        self.logs = []

    def _format_content(self, content: Any) -> str:
        """Format content to ensure it's JSON serializable"""
        if hasattr(content, 'to_json'):
            return content.to_json()
        if hasattr(content, 'to_dict'):
            return content.to_dict()
        if isinstance(content, (list, tuple)):
            return [self._format_content(item) for item in content]
        if isinstance(content, dict):
            return {k: self._format_content(v) for k, v in content.items()}
        return str(content)

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
        print(f"\n🤔 LLM is thinking about: {prompts}")
        self.logs.append({
            "type": "llm_start",
            "content": self._format_content(prompts)
        })

    def on_llm_end(self, response, **kwargs: Any) -> None:
        print(f"\n💭 LLM responded: {response}")
        self.logs.append({
            "type": "llm_end",
            "content": self._format_content(response)
        })

    def on_tool_start(self, serialized: Dict[str, Any], input_str: str, **kwargs: Any) -> None:
        print(f"\n🔧 Using tool {serialized.get('name', 'unknown')} with input: {input_str}")
        self.logs.append({
            "type": "tool_start",
            "tool": serialized.get('name', 'unknown'),
            "content": self._format_content(input_str)
        })

    def on_tool_end(self, output: str, **kwargs: Any) -> None:
        print(f"\n📊 Tool output: {output}")
        self.logs.append({
            "type": "tool_end",
            "content": self._format_content(output)
        })

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
        print(f"\n⛓️ Starting chain with: {inputs}")
        self.logs.append({
            "type": "chain_start",
            "content": self._format_content(inputs)
        })

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
        print(f"\n🔗 Chain finished with: {outputs}")
        self.logs.append({
            "type": "chain_end",
            "content": self._format_content(outputs)
        })

    def on_agent_action(self, action, **kwargs: Any) -> Any:
        print(f"\n🤖 Agent action: {action}")
        self.logs.append({
            "type": "agent_action",
            "content": self._format_content(action)
        })

    def on_agent_finish(self, finish, **kwargs: Any) -> Any:
        print(f"\n✅ Agent finished: {finish}")
        self.logs.append({
            "type": "agent_finish",
            "content": self._format_content(finish)
        })

def get_salesforce_objects_description():
    """Read the Salesforce objects description from the markdown file"""
    try:
        with open('text/salesforce_objects.md', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ""

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

    # Get Salesforce objects description
    sf_objects_desc = get_salesforce_objects_description()

    # Add system instructions with Salesforce objects context
    system_message = f"""You are a helpful data analyst assistant that helps users query a Salesforce data lake.
    The data lake contains standard Salesforce objects like Account, Contact, Opportunity, etc.
    When users ask questions, convert them to SQL queries and use the datalake_query tool to get results.
    Always format your responses clearly and explain the results in a user-friendly way.
    If you encounter errors, provide helpful explanations about what might have gone wrong.

    Here is detailed information about the Salesforce objects in the data lake:

    {sf_objects_desc}
    """

    # Initialize the agent with system message
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        system_message=system_message
    )

    return agent

def query_agent(agent, query: str) -> tuple[str, list]:
    """
    Use the agent to process a natural language query and get results from the data lake

    Args:
        agent: The initialized LangChain agent
        query: Natural language query string

    Returns:
        tuple[str, list]: (response, logs) where logs is a list of tuples (log_type, content)
    """
    try:
        callback = LoggingCallbackHandler()
        response = agent.run(query, callbacks=[callback])
        return response, callback.logs
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return f"Error processing query: {str(e)}", []
