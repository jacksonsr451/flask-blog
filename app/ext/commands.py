import click



def init_commands(app):
    @app.cli.command("create-super-user")
    @click.argument("username")
    @click.argument("email")
    @click.argument("password")
    def create_user(username, email, password):
        print("{} {} {}".format(username, email, password))