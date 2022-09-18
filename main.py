import typer
from GroupOfGroups import Groups

CONSUMEr_KEY = "103842-89aabf8bd8094760d81d63b"
app = typer.Typer()



@app.command()
def list_groups():
    pass

@app.command()
def add_groups():
    pass

@app.command()
def remove_group():
    pass

@app.command()
def select_group():
    pass

@app.command()
def list_articles():
    pass

@app.command()
def add_article():
    pass

@app.command()
def remove_article():
    pass

@app.command()
def remove_all():
    pass



if __name__ == "__main__":
    app()