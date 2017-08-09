__author__ = 'root'
from tasks import process_new,add
from sqlite_client import SqliteClient
from EventCoder import EventCoder
from encode_with_petrarch import code_articles, code_articles_

#print add.delay(4,4).ready()


num_of_process = 8

sqlite_c = SqliteClient()

total_record = int(sqlite_c.read_data('select count(*) as count from json_test_table')[0]['count'])

num_of_record = total_record/num_of_process


i = 0
for d in range(0, num_of_process):
   process_new.delay(num_of_process, num_of_record)

# sql = 'select * from json_test_table limit {}, {}'.format(1, 2)
# sqlite_c = SqliteClient()
# data = sqlite_c.read_data(sql)
# #for d in data:
# #    process.delay(d)
# coder = EventCoder(petrGlobal={})
#
# result = list()
# for d in data:
#     result.append(code_articles_(d, coder.get_PETRGlobals()))
#
# print result