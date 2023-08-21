import os
import yaml
import subprocess
import argparse
import logging
from tqdm import tqdm
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_dir = './log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

from datetime import datetime

now = datetime.now() # 获取当前日期时间
minute_time = now.strftime("%Y%m%d")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default=None, help="Path to the task config file")
    args = parser.parse_args()
    tasks = yaml.safe_load(open(args.task)) if args.task is not None else {}
    # 创建文件处理器
    task_file_name = args.task
    if "/" in task_file_name:
        task_file_name = task_file_name.split("/")[-1]
    file_handler = logging.FileHandler(f'{log_dir}/task_{task_file_name}_{minute_time}.log')
    file_handler.setLevel(logging.INFO)
    # 创建日志格式化器
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s- %(message)s')
    file_handler.setFormatter(formatter)
    # 添加处理器到 logger
    logger.addHandler(file_handler)
    #load task config
    logger.info(f"Here are {len(tasks)} tasks to process....")
    for i,task in enumerate(tqdm(tasks)):
        cmd = ['python',task['script']]
        cmd += task['args']
        logger.info(f"Task[{i+1}/{len(tasks)}] "+str(cmd))
        subprocess.call(cmd)
    logger.info("All task completed....")

if __name__ == "__main__":
    main()
    