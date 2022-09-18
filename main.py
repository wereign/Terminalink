import typer
from Groups import Groups
# CONSUMER_KEY = "103842-89aabf8bd8094760d81d63b"
app = typer.Typer()        


articles_repo = Groups()

SELECTED_GROUP = ""
@app.command()
def hello():
    print("Hello")

@app.command()
def list_groups():
    print(articles_repo)
    

@app.command()
def add_group(name:str):
    articles_repo.add(name)
    # print(articles_repo)

@app.command()
def remove_group(name:str):
    articles_repo.remove(name)

@app.command()
def select_group(name:str):
    global SELECTED_GROUP
    print(articles_repo.groups)
    if name in articles_repo.groups:
        SELECTED_GROUP = name
        print(f"Selected Group: {name}")
    else:
        print("Group doesn't exist")

@app.command()
def list_articles():
    print(articles_repo.groups[SELECTED_GROUP])

@app.command()
def add_article(article_name:str,link:str):
    articles_repo.add_to_group(SELECTED_GROUP,article_name,link)


@app.command()
def remove_article(article_name:str):
    articles_repo.remove_from_group(SELECTED_GROUP,article_name)

@app.command()
def remove_all_articles():
    articles_repo.groups[SELECTED_GROUP]



if __name__ == "__main__":
    app()