from .tasks import longtime_add , process_new 
from .sqlite_client import SqliteClient


num_of_process = 8

sqlite_c = SqliteClient()


total_record = int(sqlite_c.read_data('select count(*) as count from json_test_table')[0]['count'])

num_of_record = total_record/num_of_process


i = 0
for d in range(0, num_of_process):
   process_new.delay(num_of_process, num_of_record)

