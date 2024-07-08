# supplier_module.py
class SupplierModule:
    def __init__(self, df):
        self.df = df

    def get_stats(self):
        supplier_stats = self.df.groupby('Supplier')['Payment Volume'].sum().sort_values(ascending=False)
        return supplier_stats

    def get_supplier_position(self, supplier_name):
        supplier_stats = self.get_stats()
        if supplier_name in supplier_stats.index:
            position = supplier_stats.index.get_loc(supplier_name) + 1
            volume = supplier_stats[supplier_name]
            return f"Supplier {supplier_name} is in position {position} with overall payment volume of {volume}M."
        else:
            return f"Supplier {supplier_name} not found."
