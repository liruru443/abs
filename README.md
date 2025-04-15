# Abstract 自动关注脚本

📌 一个用于Abstract平台的自动回关脚本，自动检测并关注未互关的用户。

---

## 🚀 功能特性
- ​**自动检测未关注用户**：从你的关注者列表中扫描未关注的账号
- ​**一键自动回关**：对未关注的用户自动发起关注
- ​**代理支持**：可通过配置文件添加代理（需自行实现）

---

## ⚙️ 环境准备

### 依赖安装
1. 确保已安装 Python 
2. 安装依赖库：
```bash
pip install -r requirements.txt

## x-privy-token与authorization字段抓取
1.在abstract页面登录后打开控制台刷新一次页面
2.填入筛选链接：https://backend.portal.abs.xyz/api/user/me
3.复制对应字段填入到config.json中
![image](https://github.com/user-attachments/assets/e7cbd6db-a6a5-4db8-abb2-9477e8903146)

## 脚本启动
、、、bash
python main.py
