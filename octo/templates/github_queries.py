from string import Template

SQL_INIT = Template(
    """
    CREATE DATABASE mindsdb_github
    WITH ENGINE = 'github',
    PARAMETERS = {
      "repository": "$repo",
    };
"""
)

SQL_QUERY_ISSUES = Template(
    """
    SELECT * FROM mindsdb_github.issues
    """
)

SQL_QUERY_PRS = Template(
    """
    SELECT * FROM mindsdb_github.pull_requests
    """
)

# TODO: Add remaining useful queries

# TODO: Create separate python file for querie for the agent
