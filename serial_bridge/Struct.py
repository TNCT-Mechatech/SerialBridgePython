#encoding=utf-8
# File: Struct
# Discription: struct class(struct_name,msg_id(int),List<Pair<variable_name,variable_type>>) 
# Date: 2020/12/7
# Author: testusuke
# GitHub: https://github.com/testusuke

# This class includes struct_name,msg_id(Int),variable_list<variable<variable_name,variable_type>>
# struct_name[string]
# msg_id[Int]
# variable_list[List]
# variable_name[String]
# variable_type[String]
class Struct:
    def __init__(self,struct_name,msg_id):
        self.struct_name = str(struct_name)
        self.msg_id = int(msg_id)
        # list head index
        self.head_index = 0
        self.variable_list = []
    
    ## Setter
    def add_variable(self,variable_name,variable_type):
        #self.variable_list[self.head_index] = (str(variable_name),str(variable_type))
        self.variable_list.append((str(variable_name),str(variable_type)))
        self.head_index += 1
    
    ## Getter
    # get list of variable(name,type)
    def get_variable_list(self):
        return self.variable_list
    
    # get struct name
    def get_struct_name(self):
        return self.struct_name
    
    # get message id
    def get_msg_id(self):
        return self.msg_id
    
    # print struct data
    def print_struct(self):
        print("struct_name: " + self.struct_name + " message_id: " + str(self.msg_id))
        # show list
        for a, b in self.variable_list:
            print("variable_name: " + a + " variable_type: " + b)