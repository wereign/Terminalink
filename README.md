# Terminalink

## About Terminalink
This a python tool that let's you update a Notion Table from your command line.

## Setup
1. Download the code from github.
2. Replace the "db_id" value with your own db_id , from notion.
    The database ID is the part of the URL after your workspace name (if you have one) and the slash (myworkspace/) and before the question mark (?). The ID is 32 characters long, containing numbers and letters. Copy the ID and paste it somewhere you can easily find later.
3. Add your own secret token.
    https://developers.notion.com/docs/getting-started



## Commands
1. hello - Test if the tool works, with the command
    ```
    python main.py hello
    ```

    Incase you're using linux, replace python with python3
 
 2. list-links - Lists all the links in your table.
    
    ```
    python list-links
    ```

3. add-link - Adds a row to your notion database
a. Parameters
-  name - the title for your row.
- link - link to the interesting article/ webpage of choice.
    
    ```
    python add-link <name> <link>

    ```

