import online


class TestOnline:

    def test_case_1(self):
        nick = 'Lord of Irdorath'           # Was offline while testing
        testing = online.IsOnline()
        assert testing.checking(nick) == f'{nick} is offline'

    def test_case_2(self):
        nick = 'Rittart Orcus'      # Was offline while testing
        testing = online.IsOnline()
        assert testing.checking(nick) == f'{nick} is offline'

    def test_case_3(self):
        nick = 'Adasq'      # Was online while testing
        testing = online.IsOnline()
        assert testing.checking(nick) == f'{nick} is online'

    def test_case_4(self):
        nick = 'Lord of Irdorathg'
        testing = online.IsOnline()
        assert testing.checking(nick) == f'{nick} does not exist'
