import datetime

from loguru import logger

from IPNet import ipnet_train, ipnet_test
from Utils import check_dir, save_model
from Loader import load
from Setting import base_path

def train(name):
    check_dir(base_path+"output/csv/")
    check_dir(base_path+"output/log/")
    check_dir(base_path+"output/pt/")
    check_dir(base_path+"output/board/")
    dataset_name = name
    log_file = logger.add(f"{base_path}output/log/IPNet-{dataset_name}-{str(datetime.date.today())}.log")
    df_split = load(name = dataset_name)
    model = ipnet_train(df_split, dataset_name=dataset_name)
    logger.remove(log_file)
    
def test(name):
    check_dir(base_path+"output/csv/")
    check_dir(base_path+"output/log/")
    check_dir(base_path+"output/pt/")
    check_dir(base_path+"output/board/")
    dataset_name = name
    log_file = logger.add(f"{base_path}output/log/IPNet-{dataset_name}-{str(datetime.date.today())}.log")
    df_split = load(name = dataset_name)
    ipnet_test(df_split, dataset_name=dataset_name)
    logger.remove(log_file)

if __name__ == '__main__':
    # run("DAVIS")
    # run("KIBA")
    train("BindingDB_Kd")
    test("BindingDB_Kd")
    print("done")