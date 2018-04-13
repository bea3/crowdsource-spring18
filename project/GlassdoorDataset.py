import csv

def read_csv():
    comments = []
    with open('./dataset/jhuapl.csv', 'r') as csvfile:
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


if __name__ == '__main__':
    reviews = read_csv()