def age_in_months(listofdics):
    print([create_dic(dic) for dic in listofdics if dic["age"] <= 20])

def create_dic(dic):
    dic["age_in_months"] = dic["age"] * 12
    return dic

age_in_months([{"name":"a", "age" : 5}, {"name":"b", "age" : 21}])

def age_in_monthsv2(listofdics):
    #for dic in listofdics:
        #print(**dic)
    print([dict(**dic, age_in_months=dic["age"]*12) for dic in listofdics if dic["age"] <= 20])

age_in_monthsv2([{"name":"a", "age" : 5}, {"name":"b", "age" : 21}])
