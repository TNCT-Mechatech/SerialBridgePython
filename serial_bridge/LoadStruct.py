#encoding=utf-8
# File: LoadStruct
# Discription: you are able to get struct class(struct_name,msg_id(int),List<Pair<variable_name,variable_type>>) 
# Date: 2020/12/6
# Author: testusuke
# GitHub: https://github.com/testusuke

import Struct as st
import os
import traceback
import yaml
#from strictyaml import load, Map, Str, Int, Seq, YAMLError

class LoadStruct:
    def __init__(self,path):
        print("info: init LoadStruct")
        self.path = path
        # load struct
        self.load_struct()
        
    def load_struct(self):
        print("info: loading file:" + self.path)
        # check exist file
        if not os.path.exists(self.path):
            try:
                raise ValueError("Error: fine not exist")
            except ValueError as e:
                traceback.print_exc()
        # check file type
        root, ext = os.path.splitext(self.path)
        if not ext == '.yml' or ext == '.yaml':
            try:
                raise ValueError("Error: file is not yaml file")
            except ValueError as e:
                traceback.print_exc()
        # get info
        try:
            with open(self.path) as file:
                obj = yaml.safe_load(file)
                print(obj)
                # detect struct_name key
                for key in obj.keys():
                    if key == 'msg_id':
                        self.msg_id = obj[key]
                    else:
                        self.struct_name = key
                # create instance
                self.struct = st.Struct(self.struct_name,self.msg_id)
                # add variables
                for key in obj[self.struct_name].keys():
                    variable_name = key
                    variable_type = obj[self.struct_name][key]
                    # add
                    self.struct.add_variable(variable_name,variable_type)
        except Exception as e:
            traceback.print_exc()

    def get_struct(self):
        return self.struct