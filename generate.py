import typer
import logging
import time
import os
from tqdm import tqdm
import datetime
from utils import call_prompt_on_model_gpt35, coverage_calculate, get_file, get_function_source_code, save_file, extract_function_name, write_coveragerc
PROMPT = '''
MISSION:
You are a Python unit test generator, please generate the test() function for the following function. Just return the test function, no need to output any other natural language information.
FUNCTION TO TEST:
'''
FEW_SHOT_PROMPT = '''
MISSION:
You are a Python unit test generator, please generate the test() function for the following function. Just return the test function, no need to output any other natural language information.
OUTPUT FORMAT:
def test():
    assert ...
INPUT EXAMPLE:
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
OUTPUT EXAMPLE:  
def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
    
INPUT EXAMPLE:
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

OUTPUT EXAMPLE:
def test():   
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
FUNCTION TO TEST:
'''
REFINED_PROMPT = '''
MISSION:
You are a Python unit test generator, please generate the test() function for the following function. Just return the test function, no need to output any other natural language information.
NOTICE:
1. You only need to return the completed test() function, and do not return other information.
2. The test() function should contain at least three test cases.
3. The test() function should be able to test the correctness of the function, which means the function in assert must be consistent with the original function.
4. If you refer to a function that does not appear in FUNCTION TO TEST in test(), it is regarded as a generation failure.
OUTPUT FORMAT:
def test():
    assert ...
INPUT EXAMPLE:
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
OUTPUT EXAMPLE:  
def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
    
INPUT EXAMPLE:
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

OUTPUT EXAMPLE:
def test():   
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
FUNCTION TO TEST:
'''
REFINED_COV_PROMPT = '''
MISSION:
You are a Python unit test generator, please generate the test() function for the following function. Just return the test function, no need to output any other natural language information.
NOTICE:
1. You only need to return the completed test() function, and do not return other information.
2. The test() function should contain at least three test cases.
3. The test() function should be able to test the correctness of the function, which means the function in assert must be consistent with the original function.
4. If you refer to a function that does not appear in FUNCTION TO TEST in test(), it is regarded as a generation failure.
5. Try to cover every line of code and every branch as much as possible while ensuring the correctness of the assert.
OUTPUT FORMAT:
def test():
    assert ...
INPUT EXAMPLE:
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
OUTPUT EXAMPLE:  
def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
    
INPUT EXAMPLE:
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

OUTPUT EXAMPLE:
def test():   
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
FUNCTION TO TEST:
'''
REFINED_COV_ASSERT_PROMPT = '''
MISSION:
You are a Python unit test generator, please generate the test() function for the following function. Just return the test function, no need to output any other natural language information.
REQUIREMENT:
10 assert test statements must be generated.
NOTICE:
1. You only need to return the completed test() function, and do not return other information.
2. The test() function should be able to test the correctness of the function, which means the function in assert must be consistent with the original function.
3. If you refer to a function that does not appear in FUNCTION TO TEST in test(), it is regarded as a generation failure.
4. Try to cover every line of code and every branch as much as possible while ensuring the correctness of the assert.
OUTPUT FORMAT:
def test():
    assert ...
INPUT EXAMPLE:
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
OUTPUT EXAMPLE:  
def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
    
INPUT EXAMPLE:
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

OUTPUT EXAMPLE:
def test():   
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
FUNCTION TO TEST:
'''
def generate_humaneval(num: int, llm: str, save_path: str, prompt_type: str):

    file_path='./data/HumanEval/'+str(num)+'/script_'+str(num)+'.py'
    print('file_path:', file_path)
    code_content = get_function_source_code(file_path)
       
    if prompt_type == 'baseline':
        prompt = PROMPT + code_content
    elif prompt_type == 'few_shot':
        prompt = FEW_SHOT_PROMPT + code_content
    elif prompt_type == 'refined':
        prompt = REFINED_PROMPT + code_content
    elif prompt_type == 'refined_cov':
        prompt = REFINED_COV_PROMPT + code_content
    elif prompt_type == 'refined_cov_assert':
        prompt = REFINED_COV_ASSERT_PROMPT + code_content
    #print('code prompt:', prompt)
    #print(code_content)
    test_code = call_prompt_on_model_gpt35(prompt=prompt, code_model=llm)
    #print('test_code:', test_code)
    code_func_name_iter = extract_function_name(code_content)
    for code_func_name in code_func_name_iter:
        code_func_name = code_func_name.group()[4:-1]
        test_code = "from code_" + str(num) + " import " + code_func_name + '\n' + test_code
        
    #print(test_code)
    return test_code, code_content
    #print(test_code)
    
if __name__ == "__main__":
    def run(
        dataset: str = typer.Option("HumanEval", help="The dataset to use"),
        num_start: int = typer.Option(0, help="The starting number of the dataset"),
        num_end: int = typer.Option(1, help="The ending number of the dataset"),
        llm: str = typer.Option("gpt-3.5-turbo-0125", help="The language model to use"),
        save_path: str = typer.Option("./result", help="The path to save the generated files"),
        log_file: str = typer.Option("./log/generate_"+time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())+".log", help="Log file"),
        prompt_type: str = typer.Option("baseline", help="The type of prompt to use:baseline, few_shot, refined, refined_cov, refined_cov_assert"),
    ):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
            level=logging.INFO,
            handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        )
        
        logger.info(f"Start generate test cases for {dataset} from {num_start} to {num_end} using {llm} with {prompt_type} prompt type and save to {save_path}")
        if os.path.exists(save_path) == False:
            os.mkdir(save_path)
        if os.path.exists(save_path + '/generate') == False:
            os.mkdir(save_path + '/generate')
        if os.path.exists(save_path + '/generate/' + dataset) == False:
            os.mkdir(save_path + '/generate/' + dataset)
        save_path = save_path + '/generate/' + dataset
        #time_str = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        if llm != 'pynguin':
            if os.path.exists(save_path + '/' + prompt_type) == False:
                os.mkdir(save_path + '/' + prompt_type)
            if os.path.exists(save_path + '/' + prompt_type + '/' + llm) == False:
                os.mkdir(save_path + '/' + prompt_type + '/' + llm)
            test_path = save_path + '/' + prompt_type + '/' + llm
        
        else:
            if os.path.exists(save_path + '/' + llm) == False:
                os.mkdir(save_path + '/' + llm)
            test_path = save_path + '/' + llm
        logger.info(f"llm:{llm}")
        if dataset == "HumanEval":
            if 0 <= num_start <= 163 and 0 <= num_end <= 163 and num_start <= num_end:
                with tqdm(total=num_end-num_start+1) as pbar:
                    for num in range(num_start, num_end+1):
                        #t_start = time.time()
                        logger.info(f"HumanEval_num:{num}")
                        if os.path.exists(test_path +'/test_code_' + str(num) + '.py'):
                            pbar.update(1)
                            continue
                        if llm != 'pynguin':
                            test_code, code = generate_humaneval(num, llm, save_path, prompt_type)
                            
                            save_file(test_path +'/test_code_' + str(num) + '.py', test_code)
                            save_file(test_path +'/code_' + str(num) + '.py', code)
                           
                        else:
                            logger.info(f"pynguin execution for num:{num}")
                            file_path='./data/HumanEval/'+str(num)+'/script_'+str(num)+'.py'
                            code = get_function_source_code(file_path)
                            save_file(test_path +'/code_' + str(num) + '.py', code)
                            cmd = 'pynguin --project-path ' + test_path + ' --output-path ' + test_path + ' --module-name code_' + str(num)
                            logger.info(f"cmd:{cmd} ")
                            os.system(cmd)
                            
                            
                        #t_end = time.time()
                        #logger.info(f"HumanEval_num time:{round(t_end - t_start , 2)}s")
                        pbar.update(1)
                    
                write_coveragerc(test_path)
                coverage_calculate(test_path)
            else:
                logger.error("num_start or num_end is out of range, or num_start > num_end")
                return
#  coverage run  --context=CONTEXT --branch  -m pytest
    typer.run(run)    