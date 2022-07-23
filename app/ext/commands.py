import os
import click

from app.core.create_superuser import CreateSuperuser
from app.core.init_roles import InitRoles



def init_commands(app):
    @app.cli.command("app-install")
    def app_install():
        os.system("flask db init")
        os.system("flask db migrate")
        os.system("flask db upgrade")
        InitRoles().run()
    
    
    @app.cli.command("create-superuser")
    def create_superuser():
        print("Create superuser command")
        print("Entry with values to create")
        username = input("Username: ")
        email = input("E-mail: ")
        password = input("Password: ")
        try:
            CreateSuperuser(username=username, email=email, password=password).run()
        except Exception as error:
            print(error)
        
    
    @app.cli.command("create-superuser:args")
    @click.argument("username")
    @click.argument("email")
    @click.argument("password")
    def create_superuser_args(username, email, password):
        print("Create superuser command")
        try:
            CreateSuperuser(username=username, email=email, password=password).run()
        except Exception as error:
            print(error)
        
    
    app.cli.add_command(app_install)
    app.cli.add_command(create_superuser)
    app.cli.add_command(create_superuser_args)