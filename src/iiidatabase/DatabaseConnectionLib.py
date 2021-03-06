'''
Created on 1 Feb, 2015

@author: Vu Trong Hoa
'''
from __future__ import print_function


import pymysql



DB_HOST = "127.0.0.1"
DB_USER_NAME = "root"
DB_PASSWORD = "123456"
DB_NAME = "iii_news_db"
class IIIDatbaseConnection:
    def init_database_cont(self):
        self.db_connection = pymysql.connect(host=DB_HOST, passwd=DB_PASSWORD,
                                        user=DB_USER_NAME, db=DB_NAME)
        
    
    def close_database_cont (self):
        if (self.db_connection is not None):
            self.db_connection.close()
            
    def cursor(self):
        return self.db_connection.cursor();
    
    def commit(self):
        self.db_connection.commit()
        
    # method to insert new Categories
    def insert_category(self, cate_id, cate_name):
        cursor = self.cursor()
        sql = "INSERT INTO categories (category_id, category_name) VALUES (%s, %s)";
        result = cursor.execute(sql, (cate_id, cate_name))
        self.db_connection.commit();
        cursor.close()
        return result
    
    # method to update category
    def update_category(self, cate_id, cate_name):
        cursor = self.cursor()
        sql = "UPDATE categories SET category_name = %s WHERE category_id = %s";
        result = cursor.execute(sql, (cate_name, cate_id))
        self.db_connection.commit()
        cursor.close()
        return result
    
    # method to delete category
    def delete_category(self, cate_id):
        cursor = self.cursor()
        sql = "DELETE FROM categories WHERE category_id = %s";
        result = cursor.execute(sql, (cate_id))
        self.db_connection.commit()
        cursor.close()
        return result
    
    # method to insert new source
    def insert_source (self,source_id, source_name, source_url):
        cursor = self.cursor()
        sql = "INSERT INTO sources (source_id, name, url) VALUES (%s, %s, %s)"
        result = cursor.execute(sql, (source_id, source_name, source_url))
        self.db_connection.commit()
        cursor.close()
        return result
    # method to update source name
    def update_source_name (self, source_id, source_name):
        cursor = self.cursor()
        sql = "UPDATE sources SET source_name = %s WHERE source_id = %s";
        result = cursor.execute(sql, (source_name, source_id))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update source url
    def update_source_url (self, source_id, url):
        cursor = self.cursor()
        sql = "UPDATE sources SET url = %s WHERE source_id = %s";
        result = cursor.execute(sql, (url, source_id))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update source source reputation
    def update_source_reputation (self, source_id, reputation):
        cursor = self.cursor()
        sql = "UPDATE sources SET reputation = %s WHERE source_id = %s";
        result = cursor.execute(sql, (reputation, source_id))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to delete source
    def delete_source(self, source_id):
        cursor = self.cursor()
        sql = "DELETE FROM sources WHERE source_id = %s";
        result = cursor.execute(sql, (source_id))
        self.db_connection.commit()
        cursor.close()
        return result
        
    # method to insert new article 
    def insert_article (self, url, title, facebook_id, source_id, category_id, comment_count,
                        share_count, like_count, is_top_story, is_on_homepage):
        cursor = self.cursor()
        sql = "INSERT INTO articles (url, title, facebook_id, source_id, category_id, comment_count, share_count, like_count,is_top_story_on_their_site, is_on_home_page) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        result = cursor.execute(sql, (url, title, facebook_id, source_id, category_id, comment_count,
                        share_count, like_count, is_top_story, is_on_homepage))
        self.db_connection.commit()
        cursor.close()
        return result
    
    # method to update count
    def update_article_count(self, url, comment_count, share_count, like_count):
        cursor = self.cursor()
        sql = "UPDATE articles SET comment_count = %s, share_count = %s, like_count = %s where url = %s"
        result = cursor.execute(sql, (comment_count, share_count, like_count, url))
        self.db_connection.commit()
        cursor.close()
        return result
        
    # method to update share_count
    def update_article_share(self, url, share_count):
        cursor = self.cursor()
        sql = "UPDATE articles SET share_count = %s where url = %s"
        result = cursor.execute(sql, (share_count, url))
        self.db_connection.commit()
        cursor.close()
        return result
            
    # method to update share_count
    def update_article_comment(self, url, comment_count):
        cursor = self.cursor()
        sql = "UPDATE articles SET comment_count = %s where url = %s"
        result = cursor.execute(sql, (comment_count, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    # method to update like count
    def update_article_like(self, url, like_count):
        cursor = self.cursor()
        sql = "UPDATE articles SET like_count = %s where url = %s"
        result = cursor.execute(sql, (like_count, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    # method to update title
    def update_article_title(self, url, title):
        cursor = self.cursor()
        sql = "UPDATE articles SET title = %s where url = %s"
        result = cursor.execute(sql, (title, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    # method to update facebook id
    def update_article_fbid(self, url, facebook_id):
        cursor = self.cursor()
        sql = "UPDATE articles SET facebook_id = %s where url = %s"
        result = cursor.execute(sql, (facebook_id, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update source
    def update_article_source(self, url, source_id):
        cursor = self.cursor()
        sql = "UPDATE articles SET source_id = %s where url = %s"
        result = cursor.execute(sql, (source_id, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update category
    def update_article_category(self, url, category_id):
        cursor = self.cursor()
        sql = "UPDATE articles SET category_id = %s where url = %s"
        result = cursor.execute(sql, (category_id, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update onsite and homepage
    def update_article_ontop_homepage (self, url, is_topsite, is_on_hompage):
        cursor = self.cursor()
        sql = "UPDATE articles SET is_top_story_on_their_site = %s, is_on_home_page = %s where url = %s"
        result = cursor.execute(sql, (is_topsite, is_on_hompage, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update onsite and homepage
    def update_article_ontopsite (self, url, is_topsite):
        cursor = self.cursor()
        sql = "UPDATE articles SET is_top_story_on_their_site = %s where url = %s"
        result = cursor.execute(sql, (is_topsite, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update on site and home page
    def update_article_onhomepage (self, url, is_on_hompage):
        cursor = self.cursor()
        sql = "UPDATE articles SET is_on_home_page = %s where url = %s"
        result = cursor.execute(sql, (is_on_hompage, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update on site and home page
    def update_article_hotpoint (self, url, hotpoint):
        cursor = self.cursor()
        sql = "UPDATE articles SET hot_point = %s where url = %s"
        result = cursor.execute(sql, (hotpoint, url))
        self.db_connection.commit()
        cursor.close()
        return result
    
    #method to update
    