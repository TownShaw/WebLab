import nltk
import gensim
import tqdm

s = "CHICAGO, April 26, 2018 /PRNewswire/ -- CME Group Inc. (NASDAQ: CME) today reported record revenue of $1.1 billion and operating income of $741 million for the first quarter of 2018. Net income was $599 million and diluted earnings per share were $1.76. On an adjusted basis, net income was $634 million and diluted earnings per share were $1.86. Financial results presented on an adjusted basis for the first quarters of 2018 and 2017 exclude certain items, which are detailed in the reconciliation of non-GAAP results. 1\n\"Broad-based strength across all of our asset classes drove first-quarter revenue to more than $1.1 billion, up nearly 20 percent compared with a strong first quarter last year,\" said CME Group Chairman and Chief Executive Officer Terry Duffy. \"We achieved quarterly average daily volume records in five of our six product lines, as well as records in total options and electronic options. From a global perspective, we had growth of 41 percent in Asia and 37 percent in Europe during the quarter, with each product line experiencing increases of more than 30 percent from non-U.S. customers. In addition to significant revenue growth, our focus on expense efficiency contributed to a 50 percent increase in net income compared with the same quarter last year.\"\nFirst-quarter 2018 average daily volume was an all-time high of 22.2 million contracts, up 30 percent compared with first-quarter 2017. Clearing and transaction fee revenue was $974 million, up 23 percent compared with first-quarter 2017. First-quarter 2018 total average rate per contract was $0.706, compared with $0.736 in fourth-quarter 2017, driven primarily by a higher proportion of volume from lower priced financial products, which grew by 49 percent while higher priced commodities rose 15 percent. Market data revenue was $95 million, down 2 percent compared with the first quarter last year.\n1. A reconciliation of the non-GAAP financial results mentioned to the respective GAAP figures can be found within the Reconciliation of GAAP to non-GAAP Measures chart at the end of the financial statements and earnings presentation materials.\nAs of March 31, 2018, the company had $875 million of cash and marketable securities, excluding $491 million held in escrow related to the potential NEX Group plc acquisition, and $2.2 billion of long-term debt. The company paid dividends during the first quarter of $1.4 billion, consisting of the annual variable dividend for 2017 of $1.2 billion and the regular first-quarter dividend of $238 million. The company has returned more than $9.8 billion to shareholders in the form of dividends since implementing the variable dividend policy in early 2012.\nCME Group will hold a Q&A conference call to discuss first-quarter 2018 results at 8:30 a.m. Eastern Time today. A live audio Webcast of the Q&A call will be available on the Investor Relations section of CME Group's Web site at www.cmegroup.com . An archived recording will be available for up to two months after the call.\nAs the world's leading and most diverse derivatives marketplace, CME Group ( www.cmegroup.com ) is where the world comes to manage risk. CME Group exchanges offer the widest range of global benchmark products across all major asset classes, including futures and options based on interest rates , equity indexes , foreign exchange , energy , agricultural products and metals . Around the world, CME Group brings buyers and sellers together through its CME Globex \u00ae electronic trading platform. CME Group also operates one of the world's leading central counterparty clearing providers through CME Clearing , which offers clearing and settlement services across asset classes for exchange-traded and over-the-counter derivatives. CME Group products and services ensure that businesses around the world can effectively manage risk and achieve growth.\nCME Group, the Globe logo, CME, Chicago Mercantile Exchange, Globex and E-mini are trademarks of Chicago Mercantile Exchange Inc. CBOT, Chicago Board of Trade, KCBT and Kansas City Board of Trade are trademarks of Board of Trade of the City of Chicago, Inc. NYMEX, New York Mercantile Exchange and ClearPort are trademarks of New York Mercantile Exchange, Inc. COMEX is a trademark of Commodity Exchange, Inc. Dow Jones, Dow Jones Industrial Average, S&P 500 and S&P are service and/or trademarks of Dow Jones Trademark Holdings LLC, Standard & Poor's Financial Services LLC and S&P/Dow Jones Indices LLC, as the case may be, and have been licensed for use by Chicago Mercantile Exchange Inc. All other trademarks are the property of their respective owners.\nStatements in this press release that are not historical facts are forward-looking statements. These statements are not guarantees of future performance and involve risks, uncertainties and assumptions that are difficult to predict. Therefore, actual outcomes and results may differ materially from what is expressed or implied in any forward-looking statements. We want to caution you not to place undue reliance on any forward-looking statements. We undertake no obligation to publicly update any forward-looking statements, whether as a result of new information, future events or otherwise. Among the factors that might affect our performance are increasing competition by foreign and domestic entities, including increased competition from new entrants into our markets and consolidation of existing entities; our ability to keep pace with rapid technological developments, including our ability to complete the development, implementation and maintenance of the enhanced functionality required by our customers while maintaining reliability and ensuring that such technology is not vulnerable to security risks; our ability to continue introducing competitive new products and services on a timely, cost-effective basis, including through our electronic trading capabilities, and our ability to maintain the competitiveness of our existing products and services, including our ability to provide effective services to the swaps market; our ability to adjust our fixed costs and expenses if our revenues decline; our ability to maintain existing customers, develop strategic relationships and attract new customers; our ability to expand and offer our products outside the United States; changes in regulations, including the impact of any changes in laws or government policy with respect to our industry, such as any changes to regulations and policies that require increased financial and operational resources from us or our customers; the costs associated with protecting our intellectual property rights and our ability to operate our business without violating the intellectual property rights of others; decreases in revenue from our market data as a result of decreased demand; changes in our rate per contract due to shifts in the mix of the products traded, the trading venue and the mix of customers (whether the customer receives member or non-member fees or participates in one of our various incentive programs) and the impact of our tiered pricing structure; the ability of our financial safeguards package to adequately protect us from the credit risks of clearing members; the ability of our compliance and risk management methods to effectively monitor and manage our risks, including our ability to prevent errors and misconduct and protect our infrastructure against security breaches and misappropriation of our intellectual property assets; changes in price levels and volatility in the derivatives markets and in underlying equity, foreign exchange, interest rate and commodities markets; economic, political and market conditions, including the volatility of the capital and credit markets and the impact of economic conditions on the trading activity of our current and potential customers; our ability to accommodate increases in contract volume and order transaction traffic and to implement enhancements without failure or degradation of the performance of our trading and clearing systems; our ability to execute our growth strategy and maintain our growth effectively; our ability to manage the risks and control the costs associated with our strategy for acquisitions, investments and alliances; our ability to continue to generate funds and/or manage our indebtedness to allow us to continue to invest in our business; industry and customer consolidation; decreases in trading and clearing activity; the imposition of a transaction tax or user fee on futures and options on futures transactions and/or repeal of the 60/40 tax treatment of such transactions; our failure to maintain our brand's reputation; the unfavorable resolution of material legal proceedings and the uncertainties of the ultimate impact of the Tax Cuts and Jobs Act. For a detailed discussion of these and other factors that might affect our performance, see our filings with the Securities and Exchange Commission, including our most recent periodic reports filed on Form 10-K and Form 10-Q.\nCME Group Inc. and Subsidiaries\nConsolidated Balance Sheets\n(in millions)\nMarch 31, 2018\nDecember 31, 2017\nASSETS\nCurrent Assets:\nCash and cash equivalents\n$\n784.6\n$\n1,903.6\nMarketable securities\n90.4\n90.1\nAccounts receivable, net of allowance\n444.1\n359.7\nOther current assets (includes $492.3 and $0 in restricted cash)\n646.8\n367.8\nPerformance bonds and guaranty fund contributions\n39,088.9\n44,185.3\nTotal current assets\n41,054.8\n46,906.5\nProperty, net of accumulated depreciation and amortization\n387.2\n399.7\nIntangible assets\u2014trading products\n17,175.3\n17,175.3\nIntangible assets\u2014other, net\n2,322.6\n2,346.3\nGoodwill\n7,569.0\n7,569.0\nOther assets (includes $1.4 and $2.4 in restricted cash)\n1,410.4\n1,394.4\nTotal Assets\n$\n69,919.3\n$\n75,791.2\nLIABILITIES AND EQUITY\nCurrent Liabilities:\nAccounts payable\n$\n25.0\n$\n31.3\nOther current liabilities\n331.4\n1,456.3\nPerformance bonds and guaranty fund contributions\n39,088.9\n44,185.3\nTotal current liabilities\n39,445.3\n45,672.9\nLong-term debt\n2,233.5\n2,233.1\nDeferred income tax liabilities, net\n4,846.6\n4,857.7\nOther liabilities\n621.1\n615.7\nTotal Liabilities\n47,146.5\n53,379.4\nShareholders' equity\n22,772.8\n22,411.8\nTotal Liabilities and Equity\n$\n69,919.3\n$\n75,791.2\nCME Group Inc. and Subsidiaries\nConsolidated Statements of Income\n(dollars in millions, except per share amounts; shares in thousands)\nQuarter Ended\nMarch 31,\n2018\n2017\nRevenues\nClearing and transaction fees\n$\n973.6\n$\n792.0\nMarket data and information services\n94.9\n96.8\nAccess and communication fees\n26.0\n24.3\nOther\n14.5\n16.2\nTotal Revenues\n1,109.0\n929.3\nExpenses\nCompensation and benefits\n152.7\n142.6\nCommunications\n5.9\n6.3\nTechnology support services\n19.6\n18.7\nProfessional fees and outside services\n42.6\n28.6\nAmortization of purchased intangibles\n23.7\n24.0\nDepreciation and amortization\n28.1\n29.4\nOccupancy and building operations\n20.0\n20.1\nLicensing and other fee agreements\n49.5\n33.8\nOther\n26.0\n24.9\nTotal Expenses\n368.1\n328.4\nOperating Income\n740.9\n600.9\nNon-Operating Income (Expense)\nInvestment income\n156.4\n138.9\nInterest and other borrowing costs\n(30.1)\n(29.8)\nEquity in net earnings of unconsolidated subsidiaries\n40.1\n30.8\nOther non-operating income (expense)\n(118.6)\n(33.8)\nTotal Non-Operating Income (Expense)\n47.8\n106.1\nIncome before Income Taxes\n788.7\n707.0\nIncome tax provision\n189.9\n307.2\nNet Income\n$\n598.8\n$\n399.8\nEarnings per Common Share:\nBasic\n$\n1.76\n$\n1.18\nDiluted\n1.76\n1.18\nWeighted Average Number of Common Shares:\nBasic\n339,305\n338,339\nDiluted\n340,747\n339,946\nCME Group Inc. and Subsidiaries\nQuarterly Operating Statistics\n1Q 2017\n2Q 2017\n3Q 2017\n4Q 2017\n1Q 2018\nTrading Days\n62\n63\n63\n63\n61\nQuarterly Average Daily Volume (ADV)\nCME Group ADV (in thousands)\nProduct Line\n1Q 2017\n2Q 2017\n3Q 2017\n4Q 2017\n1Q 2018\nInterest rate\n9,169\n8,210\n7,424\n7,970\n11,948\nEquity\n2,766\n2,707\n2,624\n2,632\n4,096\nForeign exchange\n894\n879\n971\n941\n1,100\nEnergy\n2,496\n2,632\n2,693\n2,489\n2,754\nAgricultural commodity\n1,261\n1,491\n1,381\n1,278\n1,593\nMetal\n512\n533\n611\n616\n713\nTotal\n17,098\n16,453\n15,704\n15,925\n22,204\nVenue\nElectronic\n14,947\n14,582\n14,264\n14,265\n19,796\nOpen outcry\n1,362\n1,115\n889\n1,066\n1,556\nPrivately negotiated\n789\n756\n551\n594\n851\nTotal\n17,098\n16,453\n15,704\n15,925\n22,204\nAverage Rate Per Contract (RPC)\nCME Group RPC\nProduct Line\n1Q 2017\n2Q 2017\n3Q 2017\n4Q 2017\n1Q 2018\nInterest rate\n$\n0.492\n$\n0.491\n$\n0.485\n$\n0.467\n$\n0.464\nEquity\n0.718\n0.731\n0.738\n0.768\n0.781\nForeign exchange\n0.823\n0.807\n0.796\n0.785\n0.762\nEnergy\n1.130\n1.096\n1.072\n1.133\n1.140\nAgricultural commodity\n1.334\n1.300\n1.251\n1.251\n1.246\nMetal\n1.496\n1.449\n1.376\n1.315\n1.367\nAverage RPC\n$\n0.731\n$\n0.749\n$\n0.749\n$\n0.736\n$\n0.706\nCME Group Inc. and Subsidiaries\nReconciliation of GAAP to non-GAAP Measures\n(dollars in millions, except per share amounts; shares in thousands)\nQuarter Ended\nMarch 31,\n2018\n2017\nNet Income\n$\n598.8\n$\n399.8\nRestructuring and severance\n1.4\n1.8\nAmortization of purchased intangibles\n23.7\n24.0\nLitigation matters\n8.9\n\u2014\nAcquisition-related costs (1)\n9.5\n\u2014\nForeign exchange transaction (gains) losses (2)\n1.6\n(2.5)\nGains on CME Ventures investments\n(1.1)\n\u2014\nGains on sale of BM&FBOVESPA shares\n\u2014\n(86.5)\nIncome tax effect related to above\n(9.3)\n(8.9)\nOther income tax item\n\u2014\n87.8\nAdjusted Net Income\n$\n633.5\n$\n415.5\nGAAP Earnings per Common Share:\nBasic\n$\n1.76\n$\n1.18\nDiluted\n1.76\n1.18\nAdjusted Earnings per Common Share:\nBasic\n$\n1.87\n$\n1.23\nDiluted\n1.86\n1.22\nWeighted Average Number of Common Shares:\nBasic\n339,305\n338,339\nDiluted\n340,747\n339,946\n1. Acquisition-related costs include professional fees related to the proposed acquisition with NEX Group plc.\n2. Results include foreign exchange transaction net gains and losses principally related to cash held in British pounds within entities whose functional currency is the U.S. dollar.\nCME-G\nView original content: http://www.prnewswire.com/news-releases/cme-group-inc-reports-record-first-quarter-2018-financial-results-300636021.html\nSOURCE CME Group"

search_words = []
counter = 0
porter_stemmer = nltk.stem.PorterStemmer()
with open("lab1/data/searchwords.txt", "r", encoding="utf-8") as fin:
    for line in fin:
        search_words.append(porter_stemmer.stem(line.strip()))

word_list = [porter_stemmer.stem(i) for i in (gensim.utils.tokenize(s, lowercase=True, deacc=True))]

# tokenize

for word in search_words:
    if word in word_list:
        counter+=1

print(counter)
print(len(word_list))