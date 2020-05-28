# -*- coding: utf-8 -*-

import sqlite3
from scrapy import log

class DB(object):
    '''
    变量定义：
    db_name：数据库名称
    connect：数据库的连接
    cursor：数据库游标
    last_changes：上一次数据修改计数器的值
    '''

    db_name = 'sqlite3.db'
    connect = None
    cursor = None
    last_changes = 0

    def __init__(self, db_name):
        '''
        对数据库的基本数据进行初始化
        1、建立数据库连接
        2、获取数据库游标
        3、初始化修改计数器
        '''
        try:
            if db_name != None:
                self.db_name = db_name
            self.connect = sqlite3.connect(self.db_name)
            # 链接数据库
            self.cursor = self.connect.cursor()
            # 取得数据库游标
            self.last_changes = self.connect.total_changes
            # 初始化数据修改计数器
            #print('数据库初始化成功')
            log.msg('数据库初始化成功', level=log.DEBUG)
        except Exception as e:
            #print('数据库初始化失败', e)
            log.msg('数据库初始化失败', level=log.DEBUG)
            log.msg(e, level=log.DEBUG)

    def create_table(self, table_name, fields = {}):
        '''
        创建table的方法
        传入参数：
        table_name：表名称
        fields：字段名称和字段类型的字典
        返回值：
        create_sql：组合后的建表语句
        语句转换：fields = {'id':'int PRIMARY KEY', 'name':'varchar(100)'}
        转换结果 args = "id int PRIMARY KEY, name varchar(100)"
        '''
        # 建表语句可以修改为：CREATE TABLE IF NOT EXISTS 表名 (字段1名 字段1类型, 字段2名 字段2类型);. 可以不使用查表的方式判断表是否已经建立
        # 详细语句如下：
        if self.check_table(table_name)[0][0] == 0:

            create_sql = u'CREATE TABLE %s(%s);'
            # 基本见表语句

            number = 0
            # 列数量计数器
            args = ''
            # 用于保存将字典形式的参数转化为字符串格式的结果
            for k, v in fields.items():
                # 获取参数的键值对，拼接成字符串
                #print(k, v, number, len(fields))
                if number >= len(fields) - 1:
                    args += str(k) + ' ' + str(v)
                    break
                else:
                    args += str(k) + ' ' + str(v) + ','
                number += 1
            create_sql = create_sql % (table_name, args)
            # 将参数插入到建表语句中
            self.execute_sql(create_sql)
            # 执行sql
            self.commit_sql()
            # 提交执行结果，完成最终数据库的修改
            #print('表创建成功', table_name)
            log.msg('表创建成功'+table_name, level=log.DEBUG)
        else:
            #print('该表已存在,继续执行其他任务', table_name)
            log.msg('该表已存在,继续执行其他任务'+table_name, level=log.DEBUG)


    def check_table(self, table_name):
        '''
        查询表是否存在
        参数：
        table_name：表名称
        返回值：
        result：查询结果，当结果有记录时说明表已经存在
        '''
        check_sql = u"SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = '%s';" % table_name
        result = self.execute_sql(check_sql)
        # print '*'*10, result
        # 执行sql
        return result

    def execute_sql(self, sqlstring):
        '''
        执行数据库语句并返回操作结果
        参数：
        sqlstring：数据库语句
        返回值：
        result.fetchall()：查询得到的数据集
        change_num：修改记录数
        '''
        try:
            result = self.cursor.execute(sqlstring)
            # 执行sql语句，并取得结果
            if sqlstring.lower().startswith('select'):
                # 如果是查询语句，直接返回查询结果
                return result.fetchall()
            else:
                # 如果是非查询语句，返回变更的个数
                change_num = self.connect.total_changes - self.last_changes
                # 本次修改和上次修改的差值，大于0说明已经完成修改
                self.last_changes = self.connect.total_changes
                # 记录本次修改的数目
                if change_num == 0:
                    #print(sqlstring, '语句执行变更为 0')
                    log.msg('语句执行变更为 0', level=log.DEBUG)
                    
                else:
                    #print(sqlstring, '语句执行变更为', change_num)
                    log.msg('语句执行变更为 '+str(change_num), level=log.DEBUG)
                return change_num
        except Exception as e:
            #print('数据库执行sql语句失败', e, sqlstring)
            log.msg('数据库执行sql语句失败', level=log.DEBUG)
            log.msg(e, level=log.DEBUG)
            log.msg(sqlstring, level=log.DEBUG)

    def commit_sql(self):
        '''
        提交数据库修改结果，对于查询没有影响，对于增删改操作则完成对数据库的最终执行
        此函数用于手动提交修改结果，
        '''
        try:
            self.connect.commit()
            # 提交数据库修改
        except Exception as e:
            print('数据库修改提交失败', e)
            self.connect.rollback()
            # 修改执行出错时回滚操作到上一次提交成功的状态

    def close(self):
        '''
        关闭前提交一次数据库修改，防止修改过程丢失
        关闭游标和数据库连接
        '''
        try:
            self.commit_sql()
            # 关闭前提交一次修改，防止数据尚未提交则关闭
            self.cursor.close()
            # 关闭游标
            self.connect.close()
            # 关闭数据库连接
            print('数据库已经关闭')
        except Exception as e:
            print('数据库关闭失败', e)
        finally:
            self.cursor = None
            # 释放游标变量
            self.connect = None
            # 释放连接变量
