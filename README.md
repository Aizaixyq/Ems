# 项目名称

这是一个基于 Django 开发的学生管理系统，用于实现学生信息的录入、查询、修改、删除等功能。

## 项目结构

- `ems/`：Django 项目主目录。
- `stu/`：学生管理模块。
- `templates/`：模板文件目录。
- `static/`：静态文件目录。
- `db.sqlite3`：SQLite 数据库文件。
- `manage.py`：Django 命令行工具。

## 安装

1. 安装 Python 3 和 Django。
2. 克隆本项目到本地。
3. 进入项目目录，运行以下命令初始化数据库：

```python
python manage.py migrate
```

## 运行

在项目目录下运行以下命令：

```python
python manage.py runserver
```

然后在浏览器中访问 http://localhost:8000/ 即可进入学生管理系统。

## 功能

- 学生列表展示：展示所有学生的信息，支持排序和搜索。
- 添加学生信息：支持添加学生的基本信息，包括姓名、年龄、性别等。
- 修改学生信息：支持修改学生的基本信息。
- 删除学生信息：支持删除学生的基本信息。

## 技术栈

- Python
- Django
- SQLite

## 许可证

本项目采用 MIT 许可证，详情请参见 LICENSE 文件。