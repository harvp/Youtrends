#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import operator
import cassandra
from cassandra.cluster import Cluster


def engagement(session, idnum):
    idval = str(idnum)
    query = 'SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics WHERE id = ' + idval
    rows = session.execute(query)
    for user_row in rows:
        comments = user_row.commentcount
        views = user_row.viewcount
        likes = user_row.likecount
        dislikes = user_row.dislikecount
        score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)
    return score


# pass the session connection to the server,
# an empty list, and an int X for the number of records
# to be in the list. returns the top X records
def toplist(session, arr, number):
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')
    for user_row in rows:
        comments = user_row.commentcount
        views = user_row.viewcount
        likes = user_row.likecount
        dislikes = user_row.dislikecount
        score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)
        if count < number:
            arr.append([user_row.id, score])
            count += 1
            if lowest < score:
                lowest = score
            arr.sort(key=operator.itemgetter(1))
        elif lowest < score:
            del arr[0]
            lowest = score
            arr.append([user_row.id, score])
            arr.sort(key=operator.itemgetter(1))


cluster = Cluster()
cqlSession = cluster.connect('yvideos')
myarr = []
toplist(cqlSession, myarr, 10)
print(myarr)
value = engagement(cqlSession, 42)
print(value)
