import yaml

# 读取yaml测试用例的方法。
def read_yaml(yamlpath):
    with open(yamlpath, mode="r", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

if __name__ == '__main__':
    print(read_yaml("test_api.yaml"))
