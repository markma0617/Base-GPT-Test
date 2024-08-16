import ast
import os
import re
def get_file(file_path: str) -> str:
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()

def save_file(file_path: str, content: str):
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(content)

def get_function_source_code(file_path: str) -> str:
    return get_file(file_path).split("METADATA")[0].strip()


def extract_function_name(code: str):
    # 正则表达式匹配def关键字后面跟着空格，然后是函数名（由字母、数字、下划线组成）
    # 直到遇到左括号 '('。使用\w+匹配函数名。
    match = re.finditer(r'^def\s+(\w+)\s*\(', code, re.MULTILINE)
    
    if match:
        return match  # group(1)获取第一个括号内匹配的内容，即函数名
    else:
        return None

def call_prompt_on_model_gpt35(
    prompt: str,  
    max_tokens: int = 2000,  
    code_model: str = "gpt-3.5-turbo-0125",  
    temperature: float = 0.8,  
    reruns_if_empty: int = 2,  
    reruns_no_assert: int = 2, 
) -> str:
    from openai import OpenAI
    client = []
    if code_model == "gpt-3.5-turbo-0125" or code_model == "gpt-4o":
        client = OpenAI(
            api_key = "sk-raI78THPRceYRqOpAcD5548bEf1048Fb8f29E1A210Ea072d",
            base_url = "https://openkey.cloud/v1"
        )
    elif code_model == "qwen_plus":
        #print("qwen_plus")
        code_model = "qwen-plus"
        client = OpenAI(
        api_key="sk-27380e1610f442bbb6fa452b7925857e", # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope SDK的base_url
        )
    else:
        return ""
    message = [
        {"role": "system", "content": "You're an expert in the field of generating python unit test cases."},
        {"role": "user", "content": prompt}
    ]
    explanation_response = client.chat.completions.create(
    model=code_model,
    messages=message,
    max_tokens=max_tokens,
    temperature=temperature
    )

    explanation_completion = explanation_response.choices[0].message.content
    print('explanation_completion_raw:', explanation_completion)
    if explanation_completion.find('```python') != -1:
        start_index = explanation_completion.find('```python') + len('```python')
    else:
        start_index = -1
    end_index = explanation_completion[start_index:].find('```')
    print('start_index:', start_index)
    print('end_index:', end_index)
    if start_index != -1 and end_index != -1:
        explanation_completion = explanation_completion[start_index:start_index+end_index]
    print('explanation_completion:', explanation_completion)

    if reruns_if_empty>0 and explanation_completion == "":
        print("empty output")
        return call_prompt_on_model_gpt35(
            prompt = prompt,    
            code_model = code_model,  
            max_tokens = max_tokens,  
            temperature = temperature,  
            reruns_if_empty= reruns_if_empty-1, 
            reruns_no_assert = reruns_no_assert,
        )
    
    if reruns_no_assert>0 and not re.search('assert', explanation_completion):
        print("no assert in output")
        return call_prompt_on_model_gpt35(
            prompt = prompt,  
            code_model = code_model,  
            max_tokens = max_tokens,  
            temperature = temperature,  
            reruns_if_empty= reruns_if_empty, 
            reruns_no_assert = reruns_no_assert-1,
        )
    return explanation_completion

def extract_failure_info_from_string(test_output):
    # 初始化标记，表示是否开始提取内容
    extract = False
    failure_info = ""
    
    # 将字符串按行分割，然后模拟逐行处理
    lines = test_output.split('\n')
    for line in lines:
        # 当找到FAILURES分割线时，设置标记为True开始提取
        if "FAILURES" in line:
            extract = True
            continue  # 跳过当前FAILURES行
            
        # 当找到short test summary info分割线时，停止提取
        if "short test summary info" in line:
            break
            
        # 在需要提取内容的区间内，累加行内容
        if extract:
            failure_info += line + '\n'  # 累加行内容，并保留换行符以保持格式
    
    return failure_info.strip()  # 返回提取的内容并去除首尾空白字符



def write_coveragerc(file_path: str):
    content = "[.coveragerc]\n[run]\nomit = test_*.py"
    save_file(file_path+'/.coveragerc', content)
    
def coverage_calculate(test_path: str):
    os.system('cd ' + test_path + ' && coverage run  --context=CONTEXT --branch  -m pytest ')
    os.system('cd ' + test_path + '&& coverage html')