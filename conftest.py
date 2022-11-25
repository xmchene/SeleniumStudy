# conftest.py配置需要注意以下点：
# conftest.py配置脚本名称是固定的，不能改名称
# conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
# 不需要import导入 conftest.py，pytest用例会自动查找
import pytest


@pytest.fixture(scope='module')
# scope不填默认函数级别
def login():
    print('输入账号和密码')
    # 后置
    yield
    print('退出登陆')
