from unicodedata import name
import typer
import requests
import json

app = typer.Typer()        


# NOTION PARAMETERS
db_id = "c39f07940a4b4e9381bd21dbbae87e02"
token = ""
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

@app.command()
def hello():
    print("Hello")


def list_groups(databaseId=db_id, headers=headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    # print(res.status_code)

    pages = data["results"]
    for page in pages:
        print(page['properties']['Link']['rich_text'][0]['text']['content'])
        print(page['properties']['Name']['title'][0]['text']['content'])






def add_link_function(name_row,link_row,databaseId=db_id, headers=headers):

    create_url = "https://api.notion.com/v1/pages"

    new_page_data = {
        "parent": { "database_id": databaseId},
            "properties": {
                "Link": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": link_row,
                                "link": {
                                    "url": link_row
                                }
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": link_row,
                            "href": link_row
                        }
                    ]
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": name_row,
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": name_row,
                        }
                    ]
                }
            },
        }

    data = json.dumps(new_page_data)


    res = requests.request("POST",create_url,headers=headers,data=data)
    print(res.status_code)


@app.command()
def list_links():
    list_groups()


@app.command()
def add_link(name_row,link_row):
    print(f"Adding {name_row} with link {link_row}")
    add_link_function(name_row,link_row)

if __name__ == "__main__":
    app()