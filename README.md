 # 水文数字设计平台

## 项目简介
水文数字设计平台是一个基于Streamlit开发的水文数据分析和可视化工具。该平台旨在为水文工作者提供便捷的数据处理、分析和可视化功能，帮助用户更好地理解和分析水文数据。

## 功能特点
- 用户友好的Web界面
- 数据可视化展示
- 水文数据分析工具
- 交互式数据探索

## 技术栈
- Python 3.x
- Streamlit
- Pandas
- NumPy
- Altair (数据可视化)

## 安装说明

### 环境要求
- Python 3.8+

### 安装步骤
1. 克隆仓库
```bash
git clone https://github.com/zhang-zimin/hydro.git
cd hydro
```

2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

## 使用说明
1. 启动应用
```bash
streamlit run app.py
```

2. 在浏览器中访问
默认情况下，应用将在 http://localhost:8501 运行

## 项目结构
```
hydro/
├── app.py              # 主应用文件
├── requirements.txt    # 项目依赖
├── module/            # 功能模块
├── pages/            # 页面组件
├── resources/        # 资源文件
└── v/               # 版本控制相关
```


## 许可证
本项目采用 MIT 许可证

