import allure
def test_a():
    print("aaaa")
    assert 1


@allure.step(title="测试注册的过程")
def test_login():
    allure.attach("注册","输入用户名")
    print("aaaa")
    allure.attach("注册","输入密码")
    print("bbbb")
    allure.attach("注册","点击注册")
    print("cccc")
    assert 1
