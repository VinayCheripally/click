import click
from sqlite import init_db  ,add_todo_db , delete_todo_db

@click.command()
@click.option("-n","--name",prompt="Enter your name",help="Enter ur name")
def hello(name):
    click.echo(f"hello {name}")

PRIORITIES={
    "o":"Optional",
    "l":"Low",
    "m":"Medium",
    "h":"High",
    "c":"Crucial"
}

@click.group
def mycommands():
    pass

@click.command()
def initialize_db():
    init_db()

@click.command()
@click.argument("priority",type=click.Choice(PRIORITIES.keys()),default="m")
@click.option("-n","--name",prompt="Enter the todo name",help="the name of the todo")
@click.option("-d","--desc",prompt="Enter description",help="the description")
@click.option("--due",prompt="Enter time",help="the time")
def add_todo(name,desc,priority,due):
    due = due.replace("_"," ")
    add_todo_db(name,desc,priority,due)

mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(initialize_db)

if __name__=="__main__":
    mycommands()