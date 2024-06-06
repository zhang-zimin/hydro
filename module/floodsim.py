# -*- coding: utf-8 -*-
import math
import pandas as pd


def anstr3(x, n, d=-99):
    # x: 任意实数,待转换成n位有效数字的实数
    # n: 有效数字的位数
    # d: 小数点后位数，可缺省。
    x1 = abs(x)
    n1 = int(math.log10(x1))

    if d == -99:
        d = max(0, n - n1 - 1)

    x1 = round(x1 * 10 ** d, n - n1 - 1) * 10 ** (n1 - n + 1)

    return x1 if x >= 0 else -x1


def zxcz(t0, rg, l):
    if l not in [1, 2]:
        return -1

    l2 = 2 if l == 1 else 1

    if t0 < rg[0][l - 1] or t0 > rg[-1][l - 1]:
        return -1

    for i in range(len(rg) - 1):
        if rg[i][l - 1] <= t0 <= rg[i + 1][l - 1]:
            q = rg[i][l2 - 1] + (rg[i + 1][l2 - 1] - rg[i][l2 - 1]) / (rg[i + 1][l - 1] - rg[i][l - 1]) * (
                    t0 - rg[i][l - 1])
            break
    return round(q, 3)


class Reservoir:
    def __init__(self, inithead, dataframe):
        self.input = dataframe  # 接收dataframe输入
        self.inithead = inithead  # 启调水位，用户输入

    def calculate_outflow(self):
        Flood_Hydrograph = self.input[0].values
        Reservoir_Capacity = self.input[1].values
        Discharge_Curve = self.input[2].values
        q = pd.DataFrame(self.input[3].values, columns=["t", "q"])
        t = [float(x["t"]) for x in q.to_dict(orient='records')]
        q = [float(x["q"]) for x in q.to_dict(orient='records')]
        Inflow = [zxcz(i, Flood_Hydrograph, 1) for i in t]
        Inflow[-1] = Inflow[0]
        Reservoir_Capacity_1 = zxcz(self.inithead, Reservoir_Capacity, 1) * 10000

        dataframe = pd.DataFrame({'t': t,
                                  'Inflow': Inflow,  # 入流量
                                  'q': q,  # 出库 q
                                  'Reservoir_Capacity': Reservoir_Capacity_1,  # 库容V
                                  'Reservoir_Level': self.inithead,  # 库水位H
                                  'Calculated_Discharge': 0,  # 出库q
                                  'Discharge_Deviation': 0,  # 泄量误差
                                  'Discharge': 0})

        for i in range(1, len(dataframe)):
            dataframe.iloc[i, 3] = dataframe.iloc[i - 1, 3] + (
                    dataframe.iloc[i, 1] + dataframe.iloc[i - 1, 1] - dataframe.iloc[i, 2] - dataframe.iloc[
                i - 1, 2]) / 2 * (
                                           dataframe.iloc[i, 0] - dataframe.iloc[i - 1, 0]) * 3600
        for i in range(1, len(dataframe)):
            dataframe.iloc[i, 4] = zxcz(dataframe.iloc[i, 3] / 10000, Reservoir_Capacity.tolist(), 2)
        for i in range(1, len(dataframe)):
            dataframe.iloc[i, 5] = zxcz(dataframe.iloc[i, 4], Discharge_Curve.tolist(), 1)
        for i in range(1, len(dataframe)):
            dataframe.iloc[i, 6] = dataframe.iloc[i, 2] - dataframe.iloc[i, 5]
        for i in range(1, len(dataframe)):
            dataframe.iloc[i, 7] = anstr3(dataframe.iloc[i, 2], 3)
        return dataframe


if __name__ == "__main__":
    dfs = []
    uploaded_file = r'D:\Devfile\hydro-sty\resources\input.xlsx'
    dfs.append(pd.read_excel(uploaded_file, sheet_name="Flood_Hydrograph", header=0))
    dfs.append(pd.read_excel(uploaded_file, sheet_name="Reservoir_Capacity", header=0))
    dfs.append(pd.read_excel(uploaded_file, sheet_name="Discharge_Curve", header=0))
    dfs.append(pd.read_excel(uploaded_file, sheet_name="Outflow", header=0))
    print(dfs[0].values)
    reservoir = Reservoir(500, dfs)

    df = reservoir.calculate_outflow()
    print(df)
