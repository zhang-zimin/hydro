# -*- coding: utf-8 -*-
import math
import pandas as pd
import json


class Reservoir:

    def __init__(self,inithead,jsonfile):
        self.input = self.read_json(jsonfile)  # 接收json输入
        self.flood_hydrograph = None
        self.inithead = inithead  #启调水位，用户输入
        self.reservoir_capacity = None
        self.discharge_curve = None
        self.inflow = None
        self.outflow = None


    def zxcz(self, t0, rg, l):
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

    def a(self,x, n, d=-99):
        # x: 任意实数,待转换成n位有效数字的实数
        # n: 有效数字的位数
        # d: 小数点后位数，可缺省。
        x1 = abs(x)
        n1 = int(math.log10(x1))

        if d == -99:
            d = max(0, n - n1 - 1)

        x1 = round(x1 * 10 ** d, n - n1 - 1) * 10 ** (n1 - n + 1)

        return x1 if x >= 0 else -x1

    def read_json(self,jsonfile):
        with open(jsonfile, 'r') as file:
            json_data = json.load(file)
        return json_data

    def save_json(self,data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def calculateoutflow(self):
        Flood_Hydrograph = pd.DataFrame(self.input["Flood_Hydrograph"])
        Reservoir_Capacity = pd.DataFrame(self.input["Reservoir_Capacity"])
        Discharge_Curve = pd.DataFrame(self.input["Discharge_Curve"])
        q = pd.DataFrame(self.input["Outflow"], columns=["t", "q"])

        t = [float(x["t"]) for x in q.to_dict(orient='records')]
        q = [float(x["q"]) for x in q.to_dict(orient='records')]

        Inflow = [self.zxcz(i, Flood_Hydrograph.to_dict(orient='records'), 1) for i in t]
        Inflow[-1] = Inflow[0]
        Reservoir_Capacity_1 = self.zxcz(self.inithead, Reservoir_Capacity.to_dict(orient='records'), 1) * 10000

        df = pd.DataFrame({'t': t,
                           'Inflow': Inflow,
                           'q': q,
                           'Reservoir_Capacity': Reservoir_Capacity_1,
                           'Reservoir_Level': self.inithead,
                           'Calculated_Discharge': 0,
                           'Discharge_Deviation': 0,
                           'Discharge': 0})

        for i in range(1, len(df)):
            df.iloc[i, 3] = df.iloc[i - 1, 3] + (
                        df.iloc[i, 1] + df.iloc[i - 1, 1] - df.iloc[i, 2] - df.iloc[i - 1, 2]) / 2 * (
                                        df.iloc[i, 0] - df.iloc[i - 1, 0]) * 3600
        for i in range(1, len(df)):
            df.iloc[i, 4] = self.zxcz(df.iloc[i, 3] / 10000, Reservoir_Capacity.values.tolist(), 2)
        for i in range(1, len(df)):
            df.iloc[i, 5] = self.zxcz(df.iloc[i, 4], Discharge_Curve.values.tolist(), 1)
        for i in range(1, len(df)):
            df.iloc[i, 6] = df.iloc[i, 2] - df.iloc[i, 5]
        for i in range(1, len(df)):
            df.iloc[i, 7] = self.a(df.iloc[i, 2], 3)
        return df


if __name__ == "__main__":
    pass


