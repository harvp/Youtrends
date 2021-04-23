#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import operator
import sys
import getopt
import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'secure-connect-teaminferno.zip'
}
auth_provider = PlainTextAuthProvider('PKulaMpxCDcyZsxHoLeorxdE',
                                      'R1KL7l1u,awPgafa0-G3Xjt5QAjk,gTtz.qgmQSrsstUIdQnOoq_jgI,77nPA9upDOOYj2+ZefBMXudz+dFfF7IYPMGo56gz7xD337Nrcaufv3KKh,kzaS,0_xuCflNI')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
cqlsession = cluster.connect('yvideos')

def topvideonames(number, session):

    arr = []
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')
    nameresults = session.execute('SELECT id, title FROM localized')
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
    for records in nameresults:
        for item in arr:
            if item[0] == records.id:
                item[0] = records.title
    return arr


result = topvideonames(10, cqlsession)
exit(result)