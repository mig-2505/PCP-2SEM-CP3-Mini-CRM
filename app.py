from lead import Lead

def main():

    while True:
        Lead.print_menu()
        op = input("Escolha: ")

        if op == "1":
            name = input("Nome: ")
            company = input("Empresa: ")
            email = input("Email: ")
            lead = Lead(name, company, email)
            Lead.add_lead(lead)

        elif op == "2":
            Lead.list_leads()

        elif op == "0":
            print("Até mais")
            break
        else:
            print("Opcao invalida")

if __name__ == "__main__":
    main()