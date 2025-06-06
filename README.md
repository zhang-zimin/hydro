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
- Docker

## 安装说明

### 方法一：直接安装

#### 环境要求
- Python 3.8+
- pip (Python包管理器)

#### 安装步骤
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

### 方法二：使用Docker

#### 环境要求
- Docker

#### 安装步骤
1. 构建Docker镜像
```bash
docker build -t hydro:latest .
```

2. 运行Docker容器
```bash
docker run -d -p 8501:8501 --name hydro hydro:latest
```

## 使用说明
1. 直接运行
```bash
streamlit run app.py
```

2. Docker运行
```bash
# 启动容器
docker start hydro

# 停止容器
docker stop hydro

# 查看容器日志
docker logs hydro
```

3. 在浏览器中访问
默认情况下，应用将在 http://localhost:8501 运行

## 项目结构
```
hydro/
├── app.py              # 主应用文件
├── requirements.txt    # 项目依赖
├── Dockerfile         # Docker配置文件
├── .dockerignore     # Docker忽略文件
├── module/            # 功能模块
├── pages/            # 页面组件
├── resources/        # 资源文件
└── v/               # 版本控制相关
```

## 贡献指南
1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证
本项目采用 MIT 许可证 

