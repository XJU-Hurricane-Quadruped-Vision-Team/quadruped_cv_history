import requests


def call_local_api():
    # 本地接口的地址和端口号
    local_api_url = 'http://localhost:8000/api/endpoint'  # 示例地址和端口，请替换为您实际的本地接口地址和端口号

    try:
        # 发起GET请求到本地接口
        response = requests.get(local_api_url)

        # 检查响应状态码
        if response.status_code == 200:
            # 如果请求成功，获取响应内容
            data = response.json()  # 假设接口返回JSON格式的数据
            print("本地接口调用成功，响应数据：", data)
        else:
            print("本地接口调用失败，状态码：", response.status_code)

    except requests.exceptions.RequestException as e:
        # 捕获请求异常
        print("本地接口调用出现异常：", e)


if __name__ == "__main__":
    # 调用本地接口
    call_local_api()
