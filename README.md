# ClickUp MCP Server

A Model Context Protocol (MCP) server that provides integration with ClickUp's API, allowing you to retrieve task information and manage ClickUp data through MCP-compatible clients.

## Features

- **Task Retrieval**: Get detailed information about specific ClickUp tasks
- **List Management**: Retrieve all tasks within a ClickUp list
- **Comments Access**: Fetch comments and discussion threads from tasks

## Available Tools

### `get_task(taskID: str)`

Retrieves comprehensive details about a specific ClickUp task including:

- Task name, description, and status
- Assignee information and due dates
- Priority levels and custom fields
- Creation and modification timestamps

### `get_tasks_by_listId(listID: str)`

Fetches all tasks within a specified ClickUp list, providing:

- Complete task overview for project management
- Status tracking across multiple tasks
- Assignment and progress monitoring
- Workload distribution analysis

### `get_comments(taskID: str)`

Retrieves all comments and discussion threads from a specific task:

- Complete comment history with timestamps
- Author information and reply threads
- Communication context and decision tracking

## Prerequisites

- Python 3.11 or higher
- ClickUp API token
- UV package manager (recommended) or pip

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sksudeepvarma/clickup-mcp.git
   cd clickup-mcp-python
   ```

2. **Install dependencies using UV**:

   ```bash
   uv sync
   ```

   Or using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your ClickUp API token**:

   Create a `.env` file in the project root:

   ```env
   CLICKUP_API_TOKEN=your_clickup_api_token_here
   ```

   Or set the environment variable directly:

   ```bash
   # Windows
   set CLICKUP_API_TOKEN=your_clickup_api_token_here

   # Linux/macOS
   export CLICKUP_API_TOKEN=your_clickup_api_token_here
   ```

## Getting Your ClickUp API Token

1. Log in to your ClickUp account
2. Go to **Settings** → **Apps**
3. Click **Generate** to create a new API token
4. Copy the token and add it to your environment variables

## Usage

### Running the MCP Server

```bash
python main.py
```

### Using with MCP Clients

Configure your MCP client (like Claude Desktop) to use this server by adding it to your MCP configuration:

```json
{
	"servers": {
		"clickup-mcp": {
			"type": "stdio",
			"command": "python",
			"args": ["path/to/clickup-mcp-python/main.py"],
			"env": {
				"CLICKUP_API_TOKEN": "${env:CLICKUP_API_TOKEN}"
			}
		}
	}
}
```

### Example Usage

Once connected to an MCP client, you can use the tools like:

```
# Get details about a specific task
get_task("86cyecyvu")

# Get all tasks in a list
get_tasks_by_listId("901607370347")

# Get comments from a task
get_comments("86cyecyvu")
```

## Project Structure

```
clickup-mcp-python/
├── main.py           # Main MCP server implementation
├── utilities.py      # Helper functions for API token validation
├── pyproject.toml    # Project dependencies and configuration
├── uv.lock          # Locked dependency versions
├── README.md        # This file
└── .vscode/
    └── mcp.json     # VS Code MCP configuration
```

## Dependencies

- **mcp[cli]**: Model Context Protocol implementation
- **requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management

## Security

- API tokens are managed through environment variables
- No sensitive data is logged or stored
- Secure HTTPS communication with ClickUp API
