# print(p.shares_alphas(p.candidate_shares, p.mkt_ticker, p.risk_free_rate))
#
# specrisk = p.shares_specific_risk(p.candidate_shares, p.mkt_ticker)
#
# betas = p.shares_betas(p.candidate_shares, p.mkt_ticker)
#
# mktret = p.mkt_return( p.mkt_ticker)
#
# tots = p.mkt_risk( p.mkt_ticker)
#
# print(p.non_zero_alpha(p.shares_alphas(p.candidate_shares, p.mkt_ticker, p.risk_free_rate)))
#
#
# alphas = p.shares_alphas(p.candidate_shares, p.mkt_ticker, p.risk_free_rate)
#
# unadjw = p.unadjusted_weights(alphas, p.shares_specific_risk(p.candidate_shares, p.mkt_ticker), p.non_zero_alpha(p.shares_alphas(p.candidate_shares, p.mkt_ticker, p.risk_free_rate)))
#
# print(p.adj_weight_percent(p.adjusted_weights(unadjw)))
#
# # a = p.portfolio_alpha(adjusted, alphas)
# # b = p.portfolio_beta(adjusted, betas)
# # sp = p.portfolio_specific_risk(adjusted, specrisk)
# #
# # print(p.active_port(a,b,sp,mktret,p.risk_free_rate,tots))
#
