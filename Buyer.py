# buyer_module.py
class BuyerModule:
    def __init__(self, df):
        self.df = df

    def get_buyer_position(self, buyer_name):
        buyer_stats = self.df.groupby('Buyer')['Payment Volume'].sum().sort_values(ascending=False)
        if buyer_name in buyer_stats.index:
            position = buyer_stats.index.get_loc(buyer_name) + 1
            volume = buyer_stats[buyer_name]
            return f"Buyer {buyer_name} is in position {position} with overall payment volume of {volume}M."
        else:
            return f"Buyer {buyer_name} not found."
    def get_number_of_issuers(self, buyer_name):
        issuers = self.df[self.df['Buyer'] == buyer_name]['Issuer'].nunique()
        return f"Number of Issuer under Buyer {buyer_name}: {issuers}"
