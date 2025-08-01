# server.py
from mcp.server.fastmcp import FastMCP
import requests
from utilities import validate_api_token

from typing import Optional, Tuple

# Create an MCP server
mcp = FastMCP("Demo")


# getTask tool
@mcp.tool()
def get_task(taskID: str) -> str:
    """
    Retrieves detailed information about a specific ClickUp task.
    
    This tool fetches comprehensive task data including title, description, status, 
    assignees, due dates, priority, and other metadata for the specified task.
    
    Args:
        taskID (str): The unique identifier of the ClickUp task to retrieve
        
    Returns:
        str: JSON response containing complete task details including:
             - Task name and description
             - Current status and priority
             - Assignee information
             - Due dates and time tracking
             - Custom fields and tags
             - Creation and modification timestamps
    
    Use this when you need to:
    - Get current task status or details
    - Check task assignments or due dates
    - Review task descriptions or requirements
    - Analyze task metadata for reporting
    """

    # Validate API token
    is_valid, token_or_error = validate_api_token()
    if not is_valid:
        return token_or_error
    
    api_token = token_or_error

    url = f"https://api.clickup.com/api/v2/task/{taskID}"
    headers = {
        "accept": "application/json",
        "Authorization": api_token
    }

    response = requests.get(url, headers=headers)
    return response.text

# get_comments tool
@mcp.tool()
def get_comments(taskID: str) -> str:
    """
    Retrieves all comments and discussion threads from a specific ClickUp task.
    
    This tool fetches the complete comment history for a task, including all replies,
    timestamps, and author information. Useful for understanding task context,
    decisions made, and communication history.
    
    Args:
        taskID (str): The unique identifier of the ClickUp task whose comments to retrieve
        
    Returns:
        str: JSON response containing all comments with:
             - Comment text content
             - Author names and user IDs  
             - Timestamps for each comment
             - Reply threads and mentions
             - Comment formatting and attachments
    
    Use this when you need to:
    - Review discussion history on a task
    - Understand context or decisions made
    - Find specific information mentioned in comments
    - Analyze team communication patterns
    - Get updates or status reports from comments
    """

    # Validate API token
    is_valid, token_or_error = validate_api_token()
    if not is_valid:
        return token_or_error
    
    api_token = token_or_error

    url = f"https://api.clickup.com/api/v2/task/{taskID}/comment"
    headers = {
        "accept": "application/json",
        "Authorization": api_token
    }

    response = requests.get(url, headers=headers)
    return response.text

# get_tasks_by_listId tool
@mcp.tool()
def get_tasks_by_listId(listID: str) -> str:
    """
    Retrieves all tasks within a specific ClickUp list.
    
    This tool fetches all tasks from a given list, including task details such as
    titles, descriptions, statuses, assignees, due dates, and other metadata.
    Useful for getting an overview of work within a specific project or list.
    
    Args:
        listID (str): The unique identifier of the ClickUp list to retrieve tasks from
        
    Returns:
        str: JSON response containing all tasks in the list with:
             - Task IDs, names, and descriptions
             - Current status and priority levels
             - Assignee information and due dates
             - Creation and modification timestamps
             - Custom fields and tags
             - Progress and completion status
    
    Use this when you need to:
    - Get an overview of all tasks in a project/list
    - Check the status of multiple tasks at once
    - Review task assignments across a list
    - Generate reports on list progress
    - Find specific tasks within a list context
    - Analyze workload distribution in a list
    """

    # Validate API token
    is_valid, token_or_error = validate_api_token()
    if not is_valid:
        return token_or_error
    
    api_token = token_or_error

    url = f"https://api.clickup.com/api/v2/list/{listID}/task"
    headers = {
        "accept": "application/json",
        "Authorization": api_token
    }

    response = requests.get(url, headers=headers)
    return response.text

    
def main():
    mcp.run()

if __name__ == "__main__":
    main()