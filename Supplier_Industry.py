# supplier_industry_module.py
class SupplierIndustryModule:
    def __init__(self, df):
        self.df = df

    def get_stats(self):
        supplier_industry_stats = self.df.groupby('Supplier Industry')['Payment Volume'].sum().sort_values(ascending=False)
        return supplier_industry_stats

    def get_supplier_industry_position(self, supplier_industry_name):
        supplier_industry_stats = self.get_stats()
        if supplier_industry_name in supplier_industry_stats.index:
            position = supplier_industry_stats.index.get_loc(supplier_industry_name) + 1
            volume = supplier_industry_stats[supplier_industry_name]
            return f"Supplier Industry {supplier_industry_name} is in position {position} with overall payment volume of {volume}M."
        else:
            return f"Supplier Industry {supplier_industry_name} not found."
