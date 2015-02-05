'''
Created on 4 Feb, 2015

@author: Vu Trong Hoa
'''
from pymysql.err import MySQLError

#from DatabaseConnectionLib import IIIDatbaseConnection
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection

try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()
    #start query everything here
    #print(db_connect.insert_category('category3', 'Category3'))   
    #print(db_connect.insert_source('cnn_usa', 'CNN', 'http://cnn.com'))
    #print(db_connect.insert_article('http://this_is_first_bbc_url', 'this is funny article', 
    #                             '43252', 'bbc_uk', 'entertainment', 10, 10, 10, True, False))
    
    #print(db_connect.update_article_like('http://this_is_first_bbc_url', 100))
    print(db_connect.update_article_hotpoint('http://this_is_first_bbc_url', 0.5))
    #db_connect.delete_category('category2')
    #
    db_connect.close_database_cont()
except MySQLError as e:
    print('Something went wrong: {}'.format(e))