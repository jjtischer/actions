#!/usr/bin/python
from src.actions.actions import ActionsLib

if __name__=="__main__":

    al = ActionsLib()
    al.addAction('{"action":"jump","time":200}')
    al.addAction('{"action":"run","time":75}')
    al.addAction('{"action":"jump","time":100}')
    print(al.getStats())