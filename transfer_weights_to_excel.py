from openpyxl import Workbook

#Just creating the list variables. No need to look at this part.
one_year = [('SNX', 0.00515), ('SUSHI', 0.00159), ('UMA', 0.00621), ('XLM', 0.00613), ('XRP', 0.00539), ('XTZ', 0.00012), ('YFI', 0.151), ('ZRX', 0.00177), ('LINK', 0.00612), ('LRC', 0.00382), ('LTC', 0.00434), ('MATIC', 0.20113), ('MIR', 0.00157), ('NKN', 0.0172), ('OMG', 0.00317), ('OXT', 0.00076), ('BTC', 0.00564), ('CELO', 0.00222), ('COMP', 0.00015), ('CRV', -0.00091), ('DOGE', 0.47599), ('ENJ', 0.01208), ('EOS', 0.00102), ('ETH', 0.01819), ('FIL', 0.00706), ('AAVE', -0.00116), ('ADA', 0.04354), ('ALGO', 0.00559), ('BAND', 0.00768), ('BAT', 0.00208), ('BCH', 0.00204), ('BNT', 0.00333)]
six_months = [('SNX', 0.05049), ('SUSHI', -0.08884), ('UMA', 0.44698), ('XLM', 0.07119), ('XRP', 0.13807), ('XTZ', -0.06522), ('YFI', -0.49263), ('ZRX', -0.10333), ('LINK', -0.35701), ('LRC', 0.26698), ('LTC', -0.39048), ('MATIC', 0.97074), ('MIR', 0.13998), ('NKN', 0.10209), ('OMG', 0.01286), ('OXT', -0.10906), ('BTC', 0.68593), ('CELO', 0.1437), ('COMP', -0.21233), ('CRV', -0.48063), ('DOGE', 1.0), ('ENJ', 0.12262), ('EOS', 0.09754), ('ETH', 0.41822), ('FIL', -0.06852), ('AAVE', -0.2448), ('ADA', 0.14534), ('ALGO', 0.16478), ('BAND', -0.39622), ('BAT', -0.21458), ('BCH', -0.90226), ('BNT', 0.14841)]
three_months = [('SNX', 0.05601), ('SUSHI', -0.08653), ('UMA', 0.44822), ('XLM', 0.0783), ('XRP', 0.13373), ('XTZ', -0.06321), ('YFI', -0.49317), ('ZRX', -0.09636), ('LINK', -0.35624), ('LRC', 0.25211), ('LTC', -0.38887), ('MATIC', 0.96528), ('MIR', 0.1395), ('NKN', 0.10358), ('OMG', 0.00964), ('OXT', -0.12563), ('BTC', 0.6866), ('CELO', 0.14262), ('COMP', -0.21584), ('CRV', -0.4871), ('DOGE', 1.0), ('ENJ', 0.12543), ('EOS', 0.10241), ('ETH', 0.41696), ('FIL', -0.06833), ('AAVE', -0.23636), ('ADA', 0.14039), ('ALGO', 0.16871), ('BAND', -0.3901), ('BAT', -0.21391), ('BCH', -0.90231), ('BNT', 0.15445)]
one_month = [('SNX', 0.0907), ('SUSHI', -0.23399), ('UMA', -0.24534), ('XLM', 0.02733), ('XRP', -0.30886), ('XTZ', 0.37802), ('YFI', 0.2672), ('ZRX', -0.66136), ('LINK', -0.40608), ('LRC', -0.30886), ('LTC', 0.06413), ('MATIC', 0.2712), ('MIR', -0.11001), ('NKN', -0.26088), ('OMG', -0.52132), ('OXT', -0.20364), ('BTC', 1.0), ('CELO', -0.05949), ('COMP', -0.17337), ('CRV', 1.0), ('DOGE', -0.2895), ('ENJ', 0.26966), ('EOS', -0.16417), ('ETH', 0.35095), ('FIL', -0.02072), ('AAVE', -0.51346), ('ADA', 1.0), ('ALGO', 1.0), ('BAND', -0.35293), ('BAT', 0.14823), ('BCH', -0.08242), ('BNT', 0.04899)]
fifteen_days = [('SNX', -0.06443), ('SUSHI', -0.09735), ('UMA', -0.43963), ('XLM', -0.33083), ('XRP', -0.19521), ('XTZ', 0.67856), ('YFI', 0.4544), ('ZRX', -0.37064), ('LINK', 0.13262), ('LRC', -0.42467), ('LTC', -0.24943), ('MATIC', 1.0), ('MIR', 0.34198), ('NKN', -0.03912), ('OMG', -0.3224), ('OXT', -0.34694), ('BTC', 1.0), ('CELO', 1.0), ('COMP', -0.43434), ('CRV', -0.535), ('DOGE', -0.25891), ('ENJ', 0.26173), ('EOS', -0.4944), ('ETH', -0.13585), ('FIL', 0.02454), ('AAVE', -0.21762), ('ADA', 1.0), ('ALGO', 0.16814), ('BAND', -0.48655), ('BAT', 1.0), ('BCH', -0.25219), ('BNT', -0.36644)]
#we can automate this part later if it's required.

wb = Workbook()
ws = wb.active
count = 0
for tp in one_year:
    count += 1
    ws[f"A{count}"] = tp[0]
    ws[f"B{count}"] = tp[1]


count = 0
for tp in three_months:
    count += 1
    ws[f"D{count}"] = tp[1]


count = 0
for tp in six_months:
    count += 1
    ws[f"C{count}"] = tp[1]

count = 0
for tp in one_month:
    count += 1
    ws[f"E{count}"] = tp[1]

count = 0
for tp in fifteen_days:
    count += 1
    ws[f"F{count}"] = tp[1]

wb.save(filename="invest_ratios.xlsx")

#sorry for the redundant code but i don't want to waste time writing efficient code for something
#that we may not use again.

