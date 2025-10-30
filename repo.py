from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

class Repo:

    def __init__(self):
        self.db_path = DB_PATH
        self.leads = self._loads()

    def _loads(self):
        if not self.db_path.exists():
            return []
        try:
            return json.loads(DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            # se corromper, começa vazio
            return []

    def _save(self):
        self.db_path.write_text(json.dumps(self.leads, ensure_ascii=False, indent=2), encoding="utf-8")

    def create_lead(self, lead_dict):
        leads_loaded = self.leads
        leads_loaded.append(lead_dict)
        self._save()

    def leads_list(self):
        return self.leads
