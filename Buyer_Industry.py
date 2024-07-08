# buyer_industry_module.py
class BuyerIndustryModule:
    def __init__(self, df):
        self.df = df

    def get_stats(self):
        buyer_industry_stats = self.df.groupby('Buyer Industry')['Payment Volume'].sum().sort_values(ascending=False)
        return buyer_industry_stats

    def get_buyer_industry_position(self, buyer_industry_name):
        buyer_industry_stats = self.get_stats()
        if buyer_industry_name in buyer_industry_stats.index:
            position = buyer_industry_stats.index.get_loc(buyer_industry_name) + 1
            volume = buyer_industry_stats[buyer_industry_name]
            return f"Buyer Industry {buyer_industry_name} is in position {position} with overall payment volume of {volume}M."
        else:
            return f"Buyer Industry {buyer_industry_name} not found."
