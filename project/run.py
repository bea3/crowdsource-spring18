import csv
import boto
from boto.mturk.connection import MTurkConnection

HOST_URL_SANDBOX = 'mechanicalturk.sandbox.amazonaws.com'
HOST_URL = 'mechanicalturk.amazonaws.com'

def read_csv():
    comments = []
    with open('./jhuapl.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()

        for row in reader:
            comment = dict()
            comment["employer"] = row[0]
            comment["link"] = row[1]
            comment["job_title"] = row[2]
            comment["date"] = row[3]
            comment["city"] = row[4]
            comment["state"] = row[5]
            comment["current_job"] = row[6]
            comment["length_employement"] = row[7]
            comment["employment_status"] = row[8]
            comment["overall_satisfcation"] = row[9]
            comment["career_opportunities"] = row[10]
            comment["compensation"] = row[11]
            comment["senior_leadership"] = row[12]
            comment["worklife_balance"] = row[13]
            comment["culture"] = row[14]
            comment["business_outlook"] = row[15]
            comment["recommended"] = row[16]
            comment["ceo_approval"] = row[17]
            comment["pros"] = row[18]
            comment["cons"] = row[19]
            comment["advice_to_sr_mgmt"] = row[20]
            comment["headline"] = row[21]
            comment["employer_response"] = row[22]
            comments.append(comment)
    return comments


def create_mturk_client():
    f = open("aws_credentials.txt", "r")
    credentials = f.readlines()
    access_key = credentials[0].split('=')[-1].replace('\n','')
    secret_access_key = credentials[1].split('=')[-1]
    client = MTurkConnection(aws_access_key_id=access_key,
                             aws_secret_access_key=secret_access_key,
                             host=HOST_URL)
    return client


def create_mturk_hit(client):
    account_balance = client.get_account_balance()[0]
    print "You have a balance of: {}".format(account_balance)


if __name__ == '__main__':
    client = create_mturk_client()
    reviews = read_csv()
    create_mturk_hit(client)
