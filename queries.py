class Query:
    def __init__(self):
        self.parts = []
    
    def add_part(self, part):
        self.parts.append(part)
    
    def show(self):
        return 'This query is: ' + ' '.join(self.parts)

class SelectBuilder:
    def __init__(self):
        self.query = Query()
    
    def restart(self):
        self.query = Query()
    
    def set_select(self, values, from_table):
        query_part = f'SELECT {values} FROM {from_table}'
        self.query.add_part(query_part)
        return self
    
    def set_where(self, where_value):
        query_part = f'WHERE {where_value}'
        self.query.add_part(query_part)
        return self