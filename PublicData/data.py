import requests
import configparser
import xml.etree.ElementTree as ET

class Data:
    CORP_CODE_URL="http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByNm"
    CORP_INFO_URL="http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBasicInfo"
    STOCK_DISTRIBUTION_URL="http://api.seibro.or.kr/oopenapi/service/CorpSvc/getStkDistributionStatus"

    def __init__(self):
        config=configparser.RawConfigParser()
        config.read('../config.ini')
        self.api_key=config["DATA"]["api_key"]
        # self.api_key=requests.utils.unquote(self.api_key)
        if self.api_key is None:
            raise Exception("Need to api key")

    def get_corp_code(self, name=None):
        query_params={"ServiceKey":self.api_key, "IssucoNm":name, "numOfRows":str(5000)}
        request_url=self.CORP_CODE_URL+"?"
        for k,v in query_params.items():
            request_url=request_url+k+"="+v+"&"

        res=requests.get(request_url[:-1])
        root=ET.fromstring(res.text)
        from_tags=root.iter("items")

        result={}

        for items in from_tags:
            for item in items.iter('item'):
                if name in item.find('issucoNm').text.split():
                    result["issuecoCustno"]=item.find('issucoCustno').text
                    result["issucoNm"]=item.find('issucoNm').text

        return result

    def get_corp_info(self, code=None):
        query_params = {"ServiceKey": self.api_key, "IssucoCustno": code.replace("0","")}
        request_url = self.CORP_INFO_URL + "?"
        for k, v in query_params.items():
            request_url = request_url + k + "=" + v + "&"

        res = requests.get(request_url[:-1])
        root = ET.fromstring(res.text)
        from_tags = root.iter("item")

        result = {}

        for item in from_tags:
            result["apliDt"]=item.find('apliDt').text
            result["bizno"] = item.find('bizno').text
            result["ceoNm"] = item.find('ceoNm').text
            result["engCustNm"] = item.find('engCustNm').text
            result["foundDt"] = item.find('foundDt').text
            result["homeAddr"] = item.find('homeAddr').text
            result["pval"] = item.find('pval').text
            result["totalSktcnt"] = item.find('totalSktcnt').text

        return result

    def get_stk_distribution_info(self, code=None, date=None):
        query_params = {"ServiceKey": self.api_key, "IssucoCustno": code.replace("0", ""), "rgtStdDt":date}
        request_url = self.STOCK_DISTRIBUTION_URL + "?"
        for k, v in query_params.items():
            request_url = request_url + k + "=" + v + "&"

        res = requests.get(request_url[:-1])
        root = ET.fromstring(res.text)
        from_tags = root.iter("items")

        result_list = []

        for items in from_tags:
            for item in items.iter('item'):
                result={}

                result["shrs"] = item.find('shrs').text
                result["shrs_ratio"] = item.find('shrs_ratio').text
                result["stk_dist_name"] = item.find('stk_dist_name').text
                result["stk_qty"] = item.find('stk_qty').text
                result["stk_qty_ratio"] = item.find('stk_qty_ratio').text
                result["homeAddr"] = item.find('homeAddr').text
                result_list.append(result)

        return result_list