# http://localhost/index.php?route=account/login
class TestAccountLogin:

    '''
    New Customer при клике на Continue меняется ссылка
    '''
    def test_new_customer(self, account_login):
        assert account_login.get_clicked_url() is True

    '''
    При отправке пустой формы в Returning Customer, появляется сообщение об ошибке
    '''
    def test_returning_customer(self, account_login):
        assert account_login.get_message_danger() > -1

    '''
    Проверка, что при нажатии Forgotten Password меняется url
    '''
    def test_forgotten_password(self, account_login):
        assert account_login.get_url_forgotten() is True

    '''
    Проверка, что при вводе не существующего email и пароля, появляется сообщение, что пользователь не найден
    '''
    def test_user_not_found(self, account_login):
        assert account_login.get_message_not_login != -1

    '''
    Проверка, что при вводе существующего email и пароля, пользователь авторизован
    '''
    def test_account(self, account_login):
        assert account_login.get_heading_account != -1
