import pickle
from datetime import datetime
import logging

#klaidu gaudymas -- Igor

logging.basicConfig(
    log_name="logger.log", 
    encoding="UTF-8", 
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
)
logging.info("Program has started")

class Task:
    def __init__(self, name: str, description: str, deadline: datetime, start_time=datetime.now(), status='in progress'):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.status = status
        self.deadline = deadline

    def __str__(self) -> str:
        return(f'{self.name}, {self.status}')


class Entries:
    def __init__(self):
        self.task_list = []
        logging.info("Main GUI created")

    def add_task(self, task):
        self.task_list.append(task)
        logging.info(f"Task created: {Task.__str__()}")

    def delete_task(self, task_name):
        try:
            for task in self.task_list:
                if task.name == task_name:
                    self.task_list.remove(task)
                    logging.info(f"Task deleted: {self.task_list(task)}")
        except:
            print(f"Selected task doesn't exist")
            logging.info(f"Couldn't delete task, task not found")

    def save_to_pickle(self, filename):
        with open (filename, 'wb') as file:
            pickle.dump(self.task_list, file)
        logging.info(f"Data saved to file: {filename}")
            
    def load_from_pickle(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.task_list = pickle.load(file)
            logging.info(f"Data loaded from file: {filename}")
        except:
            self.task_list = []
            logging.info(f"File not found, creating empty file")

    def change_status(self, task_name, new_status):
        for task in self.task_list:
            if task.name == task_name:
                logging.info(f"Tasks {task} status changed from {task.status} to {new_status}")
                task.status = new_status

    def change_deadline(self, task_name, new_deadline):
        for task in self.task_list:
            if task.name == task_name:
                logging.info(f"Task {task} deadline changed from {task.deadline} to {new_deadline}")
                task.deadline == new_deadline
        
                
# Del deadline, tai reikia padaryti kad ispradziu gautumeme is vartotojo data (pvz. "1900-01-01, 11:15"),
# kuri uzsiraso kaip "str" i kintamaja "input_date", ir toliau atliekam veisma (tikriausiai ideti i add_task metoda):
# deadline = datetime.strftime(input_date, "%Y/%m/%d, %H:%M")
