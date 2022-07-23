import click



def init_commands(app):
    @app.cli.command("app-install")
    def app_install():
        pass
    
    
    @app.cli.command("create-superuser")
    def create_user():
        print("Create superuser command")
        print("Entry with values to create")
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        print("{} {} {}".format(username, email, password))
        
    
    @app.cli.command("create-superuser:args")
    @click.argument("username")
    @click.argument("email")
    @click.argument("password")
    def create_user_args(username, email, password):
        print("Create superuser command")
        print("{} {} {}".format(username, email, password))
        
        
    
    app.cli.add_command(app_install)
    app.cli.add_command(create_user)
    app.cli.add_command(create_user_args)