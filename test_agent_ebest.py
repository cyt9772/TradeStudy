import unittest
from ebest import EBest
import inspect, time

class TestEBest(unittest.TestCase):
    def setUP(self):
        self.ebest=EBest("DEMO")
        self.ebest.login()

    def tearDown(self):
        self.ebest.logout()


    def test_get_code_list(self):

        print(inspect.stack()[0][3])
        all_result=self.ebest.get_code_list("ALL")
        assert all_result is not None
        kospi_result=self.ebest.get_code_list("KOSPI")
        assert all_result is not None
        kosdaq_result=self.ebest.get_code_list("KOSDAQ")
        assert all_result is not None

        try:
            error_result=self.ebest.get_code_list("KOS")
        except:
            error_result=None

        assert error_result is None
        print("result: ", len(all_result), len(kospi_result), len(kosdaq_result))


    def test_get_credit_trend_by_code(self):
        print(inspect.stack()[0][3])
        result=self.ebest.get_credit_trend_by_code("005930","20230126")
        assert result is not None
        print(result)

    def test_get_short_trend_by_code(self):
        print(inspect.stack()[0][3])
        result = self.ebest.get_short_trend_by_code("005930", sdate="20230101", edate="20230126")
        assert result is not None
        print(result)

    def test_get_agent_trend_by_code(self):
        print(inspect.stack()[0][3])
        result = self.ebest.get_agent_trend_by_code("005930", fromdt="20230101", todt="20230126")
        assert result is not None
        print(result)

    def test_get_account_info(self):
        result=self.ebest.get_account_info()
        assert result is not None
        print(result)

    def test_get_account_stock_info(self):
        result=self.ebest.get_account_stock_info()
        assert result is not None
        print(result)

    def test_order_stock(self):
        print(inspect.stack()[0][3])
        result=self.ebest.order_stock("005930","2","50000","2","00")
        assert result
        print(result)

    def test_order_cancel(self):
        print(inspect.stack()[0][3])
        result = self.ebest.order_cancel("29515", "A005930", "2")
        assert result
        print(result)

    def test_order_check(self):
        print(inspect.stack()[0][3])
        result = self.ebest.order_check("29515")
        assert result
        print(result)

    def test_get_current_call_price_by_code(self):
        print(inspect.stack()[0][3])
        result = self.ebest.get_current_call_price_by_code("005930")
        assert result
        print(result)

    def test_get_price_n_min_by_code(self):
        print(inspect.stack()[0][3])
        result = self.ebest.get_price_n_min_by_code("20230217","180640")
        assert result
        print(result)

    def test_get_price_n_min_by_code_tick(self):
        print(inspect.stack()[0][3])
        result = self.ebest.get_price_n_min_by_code("20230217","005930",0)
        assert result
        print(result)

agent=TestEBest()
agent.setUP()
# agent.test_get_credit_trend_by_code()
# agent.test_get_short_trend_by_code()
# agent.test_get_agent_trend_by_code()
# agent.test_get_account_info()
# agent.test_get_account_stock_info()
# agent.test_order_stock()
# agent.test_order_cancel()
# agent.test_order_check()
# agent.test_get_current_call_price_by_code()
agent.test_get_price_n_min_by_code()
agent.test_get_price_n_min_by_code_tick()