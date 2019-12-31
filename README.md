# 基于flask的网上求助平台搭建
- 1.安装数据库迁移。输入以下命令
```
python3 manager.py db init (使用init命令创建迁移仓库)
python3 manager.py db migrate -m "initial migration" (migrate命令用来自动创建迁移脚本)
python3 manager.py db upgrade (更新数据库)
```
- 2.部署程序，python3 manager.py deploy
- 3.在本地运行程序,`python3 manager.py runserver`打开http://127.0.0.1:5000端口查看, 按Ctrl+C退出程序。
* 添加角色:
```
python3 manager.py shell
from app.models import Role
Role.insert_roles()
```

# v1.0.1
### 添加功能:
1. 更换头像
2. 修改密码
3. 用户管理
4. 文章查询
5. 文章删除