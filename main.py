import click

@click.command()
@click.option("--name",prompt="Enter your name",help="Enter ur name")
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
@click.argument("priority",type=click.Choice(PRIORITIES.keys()),default="m")
@click.argument("todofile",type=click.Path(exists=False),required=0)
@click.option("--name",prompt="Enter the todo name",help="the name of the todo")
@click.option("--desc",prompt="Enter description",help="the description")
def add_todo(name,desc,priority,todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename,"a+") as f:
        f.write(f"{name}:{desc} [priority:{PRIORITIES[priority]}]\n")

@click.command()
@click.argument("idx",type=int,required=1)
def delete_todo(idx):
    with open("mytodos.txt","r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt","w") as f:
        f.write("\n".join(todo_list))
        f.write('\n')

@click.command()
@click.option("-p","--priority",type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile",type=click.Path(exists=True),required=0)
def list_todos(priority,todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open("mytodos.txt","r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx,todo in enumerate(todo_list):
            print(f"({idx}) - ({todo})")
    else:
        for idx,todo in enumerate(todo_list):
            if f"[priority:{PRIORITIES[priority]}]" in todo:
                print(f"({idx}) - ({todo})")

mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__=="__main__":
    mycommands()