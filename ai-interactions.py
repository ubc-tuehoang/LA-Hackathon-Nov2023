import json
from bardapi import Bard
from datetime import datetime
import time

def _bardai(json_data):
    ##current_time_with_milliseconds = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
    ##json_data["key1"] = current_time_with_milliseconds
    
    queryString = json_data["prime1"]
    ##Secure-1PSID
    token = ''
    bard = Bard(token=token)
    
    #queryString = "PRIME WITH **Core courses for business*** COMM 101 - Business Fundamentals: grade above 90 then move on to COMM 291; grade between 85 and 90 student can move to COMM 291A; grade between 70 and 85 student can move to COMM 291B, else repeat COMM 101* COMM 291 - Application of Statistics in Business: grade above 90 then move on to COMM 292; grade between 85 and 90 student can move to COMM 292A; grade between 70 and 85 student can move to COMM 292B, else repeat COMM 291* COMM 291A - Application of Statistics in Business* COMM 291B - Application of Statistics in Business* COMM 292 - Management and Organizational Behaviour: grade above 70 then move on to ECON 101 or MATH 104; else repeat COMM 291* COMM 292A - Application of Statistics in Business * COMM 292B - Application of Statistics in Business * ECON 101 - Principles of Microeconomics * MATH 104 - Differential Calculus with Applications to Commerce and Social Sciences * OVERALL average of COMM 101, COMM 291 and COMM 292 between 75 and 90, the student can only take MINOR of ECON * OVERALL average of COMM 101, COMM 291 and COMM 292 above 90, the student can move to a quantitative MAJOR in sauder such as Accounting, Finance, BTM, Supply chain and logistics" 

    out = bard.get_answer(queryString)['content']
    json_data["content1"] = out
    ##json_data["prime1"] = ""

    return json_data

def _openai(json_data):
    current_time_with_milliseconds = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
    json_data["key2"] = current_time_with_milliseconds

    return json_data

if __name__ == "__main__":
    bard_json_data = {
        "prime1": "value1",
        "content1": "value2",
        "key3": ["item1", "item2", "item3"]
    }
    openai_json_data = {
        "prime1": "value1",
        "content1": "value2",
        "key3": ["item1", "item2", "item3"]
    }

for i in range(2):
    print(f"\nIteration {i + 1}:")
    # Call function A with JSON data and retrieve the result

    bard_json_data["prime1"] = "PRIME WITH **Core courses for business*** COMM 101 - Business Fundamentals: grade above 90 then move on to COMM 291; grade between 85 and 90 student can move to COMM 291A; grade between 70 and 85 student can move to COMM 291B, else repeat COMM 101* COMM 291 - Application of Statistics in Business: grade above 90 then move on to COMM 292; grade between 85 and 90 student can move to COMM 292A; grade between 70 and 85 student can move to COMM 292B, else repeat COMM 291* COMM 291A - Application of Statistics in Business* COMM 291B - Application of Statistics in Business* COMM 292 - Management and Organizational Behaviour: grade above 70 then move on to ECON 101 or MATH 104; else repeat COMM 291* COMM 292A - Application of Statistics in Business * COMM 292B - Application of Statistics in Business * ECON 101 - Principles of Microeconomics * MATH 104 - Differential Calculus with Applications to Commerce and Social Sciences * OVERALL average of COMM 101, COMM 291 and COMM 292 between 75 and 90, the student can only take MINOR of ECON * OVERALL average of COMM 101, COMM 291 and COMM 292 above 90, the student can move to a quantitative MAJOR in sauder such as Accounting, Finance, BTM, Supply chain and logistics"
    result_from_BardAI = _bardai(bard_json_data)
    print(f"Result from BardAI[{i+1}]:")
    print(json.dumps(result_from_BardAI, indent=2))

    ##example_json_data.update(result_from_BardAI)
    openai_json_data["prime1"] = result_from_BardAI["content1"]
    time.sleep(2)

    # Call OpenAI with JSON data and retrieve the result
    result_from_OpenAI = _openai(openai_json_data)
    print(f"Result from OpenAI[{i+1}]:")
    print(json.dumps(result_from_OpenAI, indent=2))

    example_json_data.update(result_from_OpenAI)
