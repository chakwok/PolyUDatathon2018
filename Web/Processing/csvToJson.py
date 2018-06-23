import csv
import json


csvfile = open('summary_table_comments.csv', 'r')
jsonfile = open('summary_table_comments.json', 'w')

fieldnames = ("id", "comments_count", "created_at", "likes_count", "retweets_count", "s_text", "sid", "u_name_x", "uid_x", "Id", "result", "cid", "u_city", "u_name_y", "u_province", "uid_y")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')