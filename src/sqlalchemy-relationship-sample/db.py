import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# ==================================================
# DBファイル作成
# ==================================================
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# データベースエンジンを作成
db_engine = create_engine(database, echo=True)
Base = declarative_base()

# ==================================================
# モデル
# ==================================================
# 部署
class Department(Base):
    # テーブル名
    __tablename__ = 'departments'
    # 部署ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 部署名
    name = Column(String, nullable=False, unique=True)
    # リレーション: １対多
    employees = relationship("Employee", back_populates = "department")
        
    # 表示用関数
    def __str__(self):
        return f"部署ID：{self.id}, 部署名：{self.name}"

# 従業員
class Employee(Base):
    # テーブル名
    __tablename__ = 'employees'
    # 従業員ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 従業員名
    name = Column(String, nullable=False)
    # ForeignKeyには「テーブル名.カラム名」を指定
    department_id = Column(Integer, ForeignKey('departments.id'))
    # リレーション: １対１
    department = relationship("Department", back_populates = "employees", uselist=False)
        
    # 表示用関数
    def __str__(self):
        return f"従業員ID：{self.id}, 従業員名：{self.name}"

# ==================================================
# テーブル操作
# ==================================================
print('（１）テーブルを削除してから作成')
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# セッションの生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# データ作成
print('（２）データ登録：実行')
# 部署
dept01 = Department(name='開発部')
dept02 = Department(name='営業部')

# 従業員
emp01 = Employee(name='太郎')
emp02 = Employee(name='ジロウ')
emp03 = Employee(name='さぶろう')
emp04 = Employee(name='花子')

# 部署に従業員を紐づける
# 開発部：太郎、ジロウ
# 営業部：さぶろう、花子
dept01.employees.append(emp01)
dept01.employees.append(emp02)
dept02.employees.append(emp03)
dept02.employees.append(emp04)

# セッションで「部署」を登録
session.add_all([dept01, dept02])
session.commit()

print('（３）データ参照：実行')
print('■：Employeeの参照')
target_emp = session.query(Employee).filter_by(id=1).first() 
print(target_emp)
print('■：Employeeに紐付いたDepartmentの参照')
print(target_emp.department) 

print('■' * 100)

print('■：Departmentの参照')
target_dept = session.query(Department).filter_by(id=1).first() 
print(target_dept)
print('■：Departmentに紐付いたのEmployeeの参照')
for emp in target_dept.employees:
    print(emp)