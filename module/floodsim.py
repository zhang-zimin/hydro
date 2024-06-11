# -*- coding: utf-8 -*-
import math
import pandas as pd
import numpy as np


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

    def calculate_outflow2(self):
        # 确保self.input包含正确的数据
        if len(self.input) != 4:
            raise ValueError("Input should contain 4 elements.")

        Flood_Hydrograph = self.input[0].values
        Reservoir_Capacity = self.input[1].values
        Discharge_Curve = self.input[2].values
        t = self.input[3]['t(h)']

        dataframe = pd.DataFrame({'t': t,
                                  'Inflow': 0,  # 入流量
                                  'Reservoir_Level': self.inithead,  # 库水位H  初始化为起调水位
                                  'Reservoir_Capacity': 0,  # 库容V
                                  'q': 0,  # 出库 q
                                  'verification_q': 0,  # 验算q
                                  'Discharge_Deviation': 0  # 泄量误差
                                  })

        # 计算入流量
        dataframe["Inflow"] = dataframe["t"].apply(lambda _t: zxcz(_t, Flood_Hydrograph, 1))
        # 计算库容列第一行
        dataframe.loc[0, "Reservoir_Capacity"] = zxcz(self.inithead, Reservoir_Capacity, 1) * 10000
        # 试算
        threshold = 0.003
        step = 0.001

        Reservoir_Level_np = dataframe["Reservoir_Level"].astype(float).values
        Reservoir_Capacity_np = dataframe["Reservoir_Capacity"].astype(float).values
        verification_q_np = dataframe["verification_q"].astype(float).values
        Discharge_Deviation_np = dataframe["Discharge_Deviation"].astype(float).values
        q_np = dataframe["q"].astype(float).values
        Inflow_np = dataframe["Inflow"].astype(float).values
        time_np = dataframe["t"].astype(float).values
        iteration_count = 0
        optimalresult = np.zeros(7)
        optimalresult[2] = 99
        for i in range(1, len(Reservoir_Level_np)):
        # for i in range(1, 3):  # 调试用
            while 1:
                iteration_count += 1
                print(f"Iteration {iteration_count} completed.")
                # 计算库容列其余行
                Reservoir_Capacity_np[i] = Reservoir_Capacity_np[i - 1] + (
                        Inflow_np[i] + Inflow_np[i - 1] - q_np[i] - q_np[i - 1]) / 2 * (
                                                   time_np[i] - time_np[i - 1]) * 3600
                # 计算库水位列
                Reservoir_Level_np[i] = zxcz(Reservoir_Capacity_np[i] / 10000, Reservoir_Capacity, 2)
                print(f"Reservoir_Level_np:{Reservoir_Level_np[i]}")
                # 计算验算流量列
                verification_q_np[i] = zxcz(Reservoir_Level_np[i], Discharge_Curve, 1)
                print(f"verification_q_np[i]:{verification_q_np[i]}")
                # 计算泄量误差
                Discharge_Deviation_np[i] = np.abs(q_np[i] - verification_q_np[i])
                print(f"verification_q_np[i]:{verification_q_np[i]}")

                # 更新解域
                if np.abs(Discharge_Deviation_np[i]) < optimalresult[2]:
                    optimalresult[1] = q_np[i]
                    optimalresult[2] = Discharge_Deviation_np[i]
                    optimalresult[3] = Reservoir_Capacity_np[i]
                    optimalresult[4] = verification_q_np[i]
                    optimalresult[5] = Discharge_Deviation_np[i]
                    optimalresult[6] = Reservoir_Level_np[i]

                # 达到最大迭代深度或者误差降至0,装载最优解域
                if q_np[i] >= Inflow_np[i-1]+10 or optimalresult[2] == 0:
                    q_np[i] = optimalresult[1]
                    Discharge_Deviation_np[i] = optimalresult[2]
                    Reservoir_Capacity_np[i] = optimalresult[3]
                    verification_q_np[i] = optimalresult[4]
                    Discharge_Deviation_np[i] = optimalresult[5]
                    Reservoir_Level_np[i] = optimalresult[6]
                    optimalresult = np.zeros(7)
                    optimalresult[2] = 99
                    break

                # 累进
                q_np[i] += step
                print(f"此时的流量{q_np[i]}")

        dataframe["Reservoir_Level"] = Reservoir_Level_np  # 库水位列
        dataframe["Reservoir_Capacity"] = Reservoir_Capacity_np
        dataframe["verification_q"] = verification_q_np  # 验算流量列
        dataframe["Discharge_Deviation"] = Discharge_Deviation_np  # 泄量误差列
        dataframe["q"] = q_np  # 泄量

        return dataframe

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
    pass
    # dfs = []
    # uploaded_file = r'/resources/input.xlsx'
    # dfs.append(pd.read_excel(uploaded_file, sheet_name="Flood_Hydrograph", header=0))
    # dfs.append(pd.read_excel(uploaded_file, sheet_name="Reservoir_Capacity", header=0))
    # dfs.append(pd.read_excel(uploaded_file, sheet_name="Discharge_Curve", header=0))
    # dfs.append(pd.read_excel(uploaded_file, sheet_name="Outflow", header=0))
    # reservoir = Reservoir(526.5, dfs)
    #
    # df = reservoir.calculate_outflow2()
    # print(df)
