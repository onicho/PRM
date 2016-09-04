from logic.sharefactory import *
from logic.portfolio import *
from logic.calculator import *

list_of_epic_strings = ['ERM', 'AML', 'CGL', 'NG']

shares = []

for epic in list_of_epic_strings:
    shares.append(ShareFactory.create(epic, '2009-01-01', '2014-12-31'))

market = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

share = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')

p = EltonGruberPortfolio(shares, market, 1.5)

print(p.shares_alphas(p.candidate_shares, p.mkt_ticker, p.risk_free_rate))

print(p.shares_specific_risk(p.candidate_shares, p.mkt_ticker))

print(p.shares_betas(p.candidate_shares, p.mkt_ticker))

print(p.mkt_return( p.mkt_ticker))

print(p.mkt_risk( p.mkt_ticker))


print(p.order_by_erb(p.candidate_shares, p.risk_free_rate, p.mkt_ticker))


print(p.cut_off_rate(p.order_by_erb(p.candidate_shares, p.risk_free_rate, p.mkt_ticker), p.risk_free_rate, p.mkt_ticker))


index = (p.cut_off_rate(p.order_by_erb(p.candidate_shares, p.risk_free_rate, p.mkt_ticker), p.risk_free_rate, p.mkt_ticker))

filtered  = p.cor_filter_shares_portf(p.order_by_erb(p.candidate_shares, p.risk_free_rate, p.mkt_ticker), index)

print(p.unadjusted_weights(filtered, market, index, p.risk_free_rate))

print(p.normalised_weights(p.unadjusted_weights(filtered, market, index, p.risk_free_rate)))

nw = p.normalised_weights(p.unadjusted_weights(filtered, market, index, p.risk_free_rate))

print(sum(p.norm_weight_percent(nw)))

p.zip_shares_proportions(filtered, p.norm_weight_percent(nw))

print(p.final_active_portfolio)