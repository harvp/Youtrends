#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import operator
import cassandra
from cassandra.cluster import Cluster


def videoengagement(idnum):

    cluster = Cluster()
    session = cluster.connect('yvideos')
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


def channelengagement(cname):

    cluster = Cluster()
    session = cluster.connect('yvideos')
    query1 = 'SELECT id, channeltitle FROM snippets'
    rows = session.execute(query1)
    vidnumbers = []
    for result in rows:
        if result.channeltitle == cname:
            vidnumbers.append(result.id)
    score = 0
    for idnum in vidnumbers:
        idval = str(idnum)
        score += videoengagement(idval)
    return score


# pass the session connection to the server,
# an empty list, and an int X for the number of records
# to be in the list. returns the top X records
def topvideos(number):
    cluster = Cluster()
    session = cluster.connect('yvideos')
    arr = []
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
    return arr


# pass the session connection to the server,
# an empty list, and an int X for the number of records
# to be in the list. returns the top X records
def topchannels(number):

    cluster = Cluster()
    session = cluster.connect('yvideos')
    arr = []
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT channeltitle FROM snippets')
    for user_row in rows:
        score = channelengagement(user_row.channeltitle)
        if count < number:
            arr.append([user_row.channeltitle, score])
            count += 1
            if lowest < score:
                lowest = score
            arr.sort(key=operator.itemgetter(1))
        elif lowest < score:
            del arr[0]
            lowest = score
            arr.append([user_row.channeltitle, score])
            arr.sort(key=operator.itemgetter(1))
    return arr


myarr = topvideos(10)
print(myarr)
value = videoengagement(42)
holder = channelengagement("Sapnap")
print(value)
newarr = topchannels(10)
print(newarr)
print(holder)
