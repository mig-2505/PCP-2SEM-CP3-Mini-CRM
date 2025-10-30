from datetime import date

class Stages:

    STAGES = ["novo"] # por enquanto so marcamos "novo" esses leads

    @staticmethod
    def model_lead(name, company, email):
        """Cria um lead como um dicionario simples"""
        return {
            "name" : name,
            "company" : company,
            "email" : email,
            "stage" : "novo",
            "created" : date.today().isoformat()
        }