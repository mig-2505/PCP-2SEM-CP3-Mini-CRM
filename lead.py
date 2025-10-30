from repo import Repo
from stages import Stages

repo_instance = Repo()

class Lead:

    def __init__(self, name, company, email):
        self.name = name
        self.company = company
        self.email = email

    def add_lead(self):
        repo_instance.create_lead(Stages.model_lead(self.name, self.company, self.email))
        print("Lead adicionado")

    @staticmethod
    def list_leads():
        print("Listar Leads")
        print(repo_instance.leads_list())

    @staticmethod
    def print_menu():
        print("\nMenu CRM de Leads - (Adicionar/Listar)")
        print("[1] Adicionar - Lead")
        print("[2] Listar leads")
        print("[0] Sair")