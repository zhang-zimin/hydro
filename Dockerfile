# 使用Python 3.9作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app/

# 安装依赖
RUN pip install -r requirements.txt 

# 暴露端口
EXPOSE 8501

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 启动命令
CMD ["streamlit", "run", "app.py"] 