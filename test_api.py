import pytest
import allure

class TestApi:
    @pytest.mark.parametrize("caseinfo",["百里", "北凡", "凡"])
    def test_01_mashang(self,caseinfo):
        print("test:%s " %caseinfo)

if __name__ == '__main__':
    pytest.main(['-s','test_api.py', '--alluredir', './result'])
    os.system(allure generate ./result -o ./report)