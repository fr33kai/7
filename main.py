```python
import os
import re
from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import json
from groq import Groq

# Set up the Groq API client with separate API keys for each agent
ORCHESTRATOR_API_KEY = "orchestrator_api_key_here"
SUB_AGENT_API_KEY = "sub_agent_api_key_here"
REFINER_API_KEY = "refiner_api_key_here"

client_orchestrator = Groq(api_key=ORCHESTRATOR_API_KEY)
client_sub_agent = Groq(api_key=SUB_AGENT_API_KEY)
client_refiner = Groq(api_key=REFINER_API_KEY)

# Define the models to use for each agent
ORCHESTRATOR_MODEL = "llama3-8b-8192"
SUB_AGENT_MODEL = "llama3-8b-8192"
REFINER_MODEL = "llama3-70b-8192"

# Initialize the Rich Console
console = Console()

# Function definitions remain the same, but with the following changes:
# - Use the separate client instances for each function
# - Increase the number of sub task agents to 3

# The rest of the code remains unchanged, except for the client instances
# being passed to the respective functions and the increased number of sub task agents.
```