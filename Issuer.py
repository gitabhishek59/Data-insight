# issuer_module.py
class IssuerModule:
    def __init__(self, df):
        self.df = df

    def get_stats(self):
        issuer_stats = self.df.groupby('Issuer')['Payment Volume'].sum().sort_values(ascending=False)
        return issuer_stats

    def get_issuer_position(self, issuer_name):
        issuer_stats = self.get_stats()
        if issuer_name in issuer_stats.index:
            position = issuer_stats.index.get_loc(issuer_name) + 1
            volume = issuer_stats[issuer_name]
            return f"Issuer {issuer_name} is in position {position} with overall payment volume of {volume}M."
        else:
            return f"Issuer {issuer_name} not found."

    def get_number_of_buyers(self, issuer_name):
        buyers = self.df[self.df['Issuer'] == issuer_name]['Buyer'].nunique()
        return f"Number of buyers under issuer {issuer_name}: {buyers}"

    def get_top_and_bottom_buyers(self, issuer_name, top_n):
        issuer_df = self.df[self.df['Issuer'] == issuer_name]
        buyer_stats = issuer_df.groupby('Buyer')['Payment Volume'].sum().sort_values(ascending=False)
        top_buyers = buyer_stats.head(top_n)
        bottom_buyers = buyer_stats.tail(top_n)
        return top_buyers, bottom_buyers

    def get_top_buyer_industry(self, issuer_name, top_n):
        issuer_df = self.df[self.df['Issuer'] == issuer_name]
        buyer_industry_stats = issuer_df.groupby('Buyer Industry')['Payment Volume'].sum().sort_values(ascending=False)
        top_buyer_industries = buyer_industry_stats.head(top_n)
        bottom_buyer_industries = buyer_industry_stats.tail(top_n)
        return top_buyer_industries, bottom_buyer_industries

    def get_top_and_bottom_suppliers(self, issuer_name, top_n):
        issuer_df = self.df[self.df['Issuer'] == issuer_name]
        supplier_stats = issuer_df.groupby('Supplier')['Payment Volume'].sum().sort_values(ascending=False)
        top_suppliers = supplier_stats.head(top_n)
        bottom_suppliers = supplier_stats.tail(top_n)
        return top_suppliers, bottom_suppliers

    def get_top_supplier_industry(self, issuer_name, top_n):
        issuer_df = self.df[self.df['Issuer'] == issuer_name]
        supplier_industry_stats = issuer_df.groupby('Supplier Industry')['Payment Volume'].sum().sort_values(ascending=False)
        top_supplier_industries = supplier_industry_stats.head(top_n)
        bottom_supplier_industries = supplier_industry_stats.tail(top_n)
        return top_supplier_industries, bottom_supplier_industries
