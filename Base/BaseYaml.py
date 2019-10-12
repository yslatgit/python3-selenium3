# -*- coding: UTF-8 -*-
# author:ysl
# 2019-10-08

import yaml
from yaml.scanner import ScannerError


def get_yaml(path):
    try:
        with open(path, encoding="utf-8") as f:
            x = yaml.safe_load(f)
            return [True, x]
    except FileNotFoundError:
        return [False, "yaml文件不存在"]
    except ScannerError:
        return [False, "yaml文件格式有误"]


if __name__ == '__main__':
    print(get_yaml("../Yamls/Login.yaml"))
