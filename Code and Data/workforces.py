import csv


# READ ALL DATA
# Read Civil service data
def read_civil_data():
    # create a list for the data
    data = []
    # Open the spreadsheet to read it
    with open('civil-service-workforce-2019.csv', 'r') as Civil_Service_Workforce:
        spreadsheet = csv.DictReader(Civil_Service_Workforce)
        # Add each row of the spreadsheet to the data list
        for row in spreadsheet:
            data.append(row)
    # To return the list of data
    return data


# Read Fire and Rescue data
def read_fire_and_rescue_data():
    # create a list for the data
    data = []
    # Open the spreadsheet to read it
    with open('fire-and-rescue-service-workforce.csv', 'r') as Fire_and_Rescue_Workforce:
        spreadsheet = csv.DictReader(Fire_and_Rescue_Workforce)
        # Add each row of the spreadsheet to the data list
        for row in spreadsheet:
            data.append(row)
    # To return the list of data
    return data


# Read Prison Officer data
def read_prison_officer_data():
    # Create a list for the data
    data = []
    # open spreadsheet to read it
    with open('prison-officer-workforce-data.csv', 'r') as Prison_Officer_Workforce:
        spreadsheet = csv.DictReader(Prison_Officer_Workforce)
        # add each row of the spreadsheet into the data list
        for row in spreadsheet:
            data.append(row)
    # want to return the list of data
    return data


# Read Social Workers data
def read_social_workers_data():
    # Create a list for the data
    data = []
    # open spreadsheet to read it
    with open('social-workers-for-children-and-families.csv', 'r') as Social_Service_Workforce:
        spreadsheet = csv.DictReader(Social_Service_Workforce)
        # add each row of the spreadsheet into the data list
        for row in spreadsheet:
            data.append(row)
    # want to return the list of data
    return data


# SUMMARISE DATA FUNCTIONS
# Summarise civil service data
def civil_service_summary():
    # create a list of data
    data = read_civil_data()

    # 2015 data [total amount, percentage]
    all_2015 = []
    asian_2015 = []
    black_2015 = []
    chinese_2015 = []
    mixed_2015 = []
    white_2015 = []
    other_2015 = []

    # 2019 data [total amount, percentage]
    all_2019 = []
    asian_2019 = []
    black_2019 = []
    chinese_2019 = []
    mixed_2019 = []
    white_2019 = []
    other_2019 = []

    # add in the 2015 values for each ethnicity
    for row in data:
        if row['Year'] == '2015' and row['Grade/Rank/Area/Gender/Age'] == 'All grades':
            if row['Ethnicity'] == 'All Groups':
                all_2015.append(row['Number'])
                all_2015.append('100')
            elif row['Ethnicity'] == 'Asian':
                asian_2015.append(row['Number'])
                asian_2015.append(row['%'])
            elif row['Ethnicity'] == 'Black':
                black_2015.append(row['Number'])
                black_2015.append(row['%'])
            elif row['Ethnicity'] == 'Chinese':
                chinese_2015.append(row['Number'])
                chinese_2015.append(row['%'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2015.append(row['Number'])
                mixed_2015.append(row['%'])
            elif row['Ethnicity'] == 'White':
                white_2015.append(row['Number'])
                white_2015.append(row['%'])
            elif row['Ethnicity'] == 'Other':
                other_2015.append(row['Number'])
                other_2015.append(row['%'])

    # add in the 2019 values for each ethnicity
    for row in data:
        if row['Year'] == '2019' and row['Grade/Rank/Area/Gender/Age'] == 'All grades':
            if row['Ethnicity'] == 'All Groups':
                all_2019.append(row['Number'])
                all_2019.append('100')
            elif row['Ethnicity'] == 'Asian':
                asian_2019.append(row['Number'])
                asian_2019.append(row['%'])
            elif row['Ethnicity'] == 'Black':
                black_2019.append(row['Number'])
                black_2019.append(row['%'])
            elif row['Ethnicity'] == 'Chinese':
                chinese_2019.append(row['Number'])
                chinese_2019.append(row['%'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2019.append(row['Number'])
                mixed_2019.append(row['%'])
            elif row['Ethnicity'] == 'White':
                white_2019.append(row['Number'])
                white_2019.append(row['%'])
            elif row['Ethnicity'] == 'Other':
                other_2019.append(row['Number'])
                other_2019.append(row['%'])
    # Create dictionary for what we want
    output = []

    # Add All ethnicity data
    all_change = round(float(all_2019[1]) - float(all_2015[1]), 1)
    all = {'Ethnicity': 'All groups', '2015 total': all_2015[0], '2015 percentage (%)': all_2015[1],
           '2019 total': all_2019[0],
           '2019 percentage (%)': all_2019[1], 'Change in percentage': all_change}
    output.append(all)

    # Add Asian data
    asian_change = round(float(asian_2019[1]) - float(asian_2015[1]), 1)
    asian = {'Ethnicity': 'Asian', '2015 total': asian_2015[0], '2015 percentage (%)': asian_2015[1],
             '2019 total': asian_2019[0], '2019 percentage (%)': asian_2019[1], 'Change in percentage': asian_change}
    output.append(asian)

    # Add Black data
    black_change = round(float(black_2019[1]) - float(black_2015[1]), 1)
    black = {'Ethnicity': 'Black', '2015 total': black_2015[0], '2015 percentage (%)': black_2015[1],
             '2019 total': black_2019[0], '2019 percentage (%)': black_2019[1], 'Change in percentage': black_change}
    output.append(black)

    # Add Chinese data
    chinese_change = round(float(chinese_2019[1]) - float(chinese_2015[1]), 1)
    chinese = {'Ethnicity': 'Chinese', '2015 total': chinese_2015[0], '2015 percentage (%)': chinese_2015[1],
               '2019 total': chinese_2019[0], '2019 percentage (%)': chinese_2019[1],
               'Change in percentage': chinese_change}
    output.append(chinese)

    # Add Mixed data
    mixed_change = round(float(mixed_2019[1]) - float(mixed_2015[1]), 1)
    mixed = {'Ethnicity': 'Mixed', '2015 total': mixed_2015[0], '2015 percentage (%)': mixed_2015[1],
             '2019 total': mixed_2019[0], '2019 percentage (%)': mixed_2019[1], 'Change in percentage': mixed_change}
    output.append(mixed)

    # Add White data
    white_change = round(float(white_2019[1]) - float(white_2015[1]), 1)
    white = {'Ethnicity': 'White', '2015 total': white_2015[0], '2015 percentage (%)': white_2015[1],
             '2019 total': white_2019[0], '2019 percentage (%)': white_2019[1], 'Change in percentage': white_change}
    output.append(white)

    # Add Other data
    other_change = round(float(other_2019[1]) - float(other_2015[1]), 1)
    other = {'Ethnicity': 'Other', '2015 total': other_2015[0], '2015 percentage (%)': other_2015[1],
             '2019 total': other_2019[0], '2019 percentage (%)': other_2019[1], 'Change in percentage': other_change}
    output.append(other)

    for i in range(len(output)):
        print(output[i])

    field_names = ['Ethnicity', '2015 total', '2015 percentage (%)', '2019 total', '2019 percentage (%)',
                   'Change in percentage']
    with open('civil-service-workforce-summary.csv', 'w+') as Civil_Service_Workforce:
        spreadsheet = csv.DictWriter(Civil_Service_Workforce, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(output)


# Summarise Fire and Rescue data
def fire_and_rescue_summary():
    # create a list of data
    data = read_fire_and_rescue_data()

    # 2015 data [total amount, percentage]
    all_2015 = []
    asian_2015 = []
    black_2015 = []
    mixed_2015 = []
    white_2015 = []
    other_2015 = []

    # 2019 data [total amount, percentage]
    all_2019 = []
    asian_2019 = []
    black_2019 = []
    mixed_2019 = []
    white_2019 = []
    other_2019 = []

    # add in the 2015 values for each ethnicity
    for row in data:
        if row['Time'] == '2015' and row['Type of Role'] == 'All Staff':
            if row['Ethnicity'] == 'All':
                all_2015.append(row['Total number of this ethnic group in this year in this role in this area'])
                all_2015.append('100')
            elif row['Ethnicity'] == 'Asian':
                asian_2015.append(row['Total number of this ethnic group in this year in this role in this area'])
                asian_2015.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'Black':
                black_2015.append(row['Total number of this ethnic group in this year in this role in this area'])
                black_2015.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2015.append(row['Total number of this ethnic group in this year in this role in this area'])
                mixed_2015.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'White ':
                white_2015.append(row['Total number of this ethnic group in this year in this role in this area'])
                white_2015.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'Other inc Chinese':
                other_2015.append(row['Total number of this ethnic group in this year in this role in this area'])
                other_2015.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])

    # add in the 2019 values for each ethnicity
    for row in data:
        if row['Time'] == '2019' and row['Type of Role'] == 'All Staff':
            if row['Ethnicity'] == 'All':
                all_2019.append(row['Total number of this ethnic group in this year in this role in this area'])
                all_2019.append('100')
            elif row['Ethnicity'] == 'Asian':
                asian_2019.append(row['Total number of this ethnic group in this year in this role in this area'])
                asian_2019.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'Black':
                black_2019.append(row['Total number of this ethnic group in this year in this role in this area'])
                black_2019.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2019.append(row['Total number of this ethnic group in this year in this role in this area'])
                mixed_2019.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'White ':
                white_2019.append(row['Total number of this ethnic group in this year in this role in this area'])
                white_2019.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
            elif row['Ethnicity'] == 'Other inc Chinese':
                other_2019.append(row['Total number of this ethnic group in this year in this role in this area'])
                other_2019.append(row[
                                      'Percentage of this ethnic group in this year in this role in this area (excluding where ethnicity is not known)'])
    # Create dictionary for what we want
    output = []

    # Add All ethnicity data
    all_change = round(float(all_2019[1]) - float(all_2015[1]), 1)
    all = {'Ethnicity': 'All groups', '2015 total': all_2015[0], '2015 percentage (%)': all_2015[1],
           '2019 total': all_2019[0],
           '2019 percentage (%)': all_2019[1], 'Change in percentage': all_change}
    output.append(all)

    # Add Asian data
    asian_change = round(float(asian_2019[1]) - float(asian_2015[1]), 1)
    asian = {'Ethnicity': 'Asian', '2015 total': asian_2015[0], '2015 percentage (%)': asian_2015[1],
             '2019 total': asian_2019[0], '2019 percentage (%)': asian_2019[1], 'Change in percentage': asian_change}
    output.append(asian)

    # Add Black data
    black_change = round(float(black_2019[1]) - float(black_2015[1]), 1)
    black = {'Ethnicity': 'Black', '2015 total': black_2015[0], '2015 percentage (%)': black_2015[1],
             '2019 total': black_2019[0], '2019 percentage (%)': black_2019[1], 'Change in percentage': black_change}
    output.append(black)

    # Add Mixed data
    mixed_change = round(float(mixed_2019[1]) - float(mixed_2015[1]), 1)
    mixed = {'Ethnicity': 'Mixed', '2015 total': mixed_2015[0], '2015 percentage (%)': mixed_2015[1],
             '2019 total': mixed_2019[0], '2019 percentage (%)': mixed_2019[1], 'Change in percentage': mixed_change}
    output.append(mixed)

    # Add White data
    white_change = round(float(white_2019[1]) - float(white_2015[1]), 1)
    white = {'Ethnicity': 'White', '2015 total': white_2015[0], '2015 percentage (%)': white_2015[1],
             '2019 total': white_2019[0], '2019 percentage (%)': white_2019[1], 'Change in percentage': white_change}
    output.append(white)

    # Add Other data
    other_change = round(float(other_2019[1]) - float(other_2015[1]), 1)
    other = {'Ethnicity': 'Other inc Chinese', '2015 total': other_2015[0], '2015 percentage (%)': other_2015[1],
             '2019 total': other_2019[0], '2019 percentage (%)': other_2019[1], 'Change in percentage': other_change}
    output.append(other)

    for i in range(len(output)):
        print(output[i])

    field_names = ['Ethnicity', '2015 total', '2015 percentage (%)', '2019 total', '2019 percentage (%)',
                   'Change in percentage']
    with open('fire-and-rescue-workforce-summary.csv', 'w+') as Fire_and_Rescue_Workforce:
        spreadsheet = csv.DictWriter(Fire_and_Rescue_Workforce, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(output)


# Summarise Prison Officer data
def prison_officer_summary():
    # create a list of data
    data = read_prison_officer_data()
    # 2015 data [total amount, percentage]
    asian_2015 = []
    black_2015 = []
    mixed_2015 = []
    white_2015 = []
    other_2015 = []
    # 2019 data [total amount, percentage
    asian_2019 = []
    black_2019 = []
    mixed_2019 = []
    white_2019 = []
    other_2019 = []
    # add in the 2015 values for each ethnicity
    for row in data:
        if row['Time'] == '31/03/2015':
            if row['Ethnicity'] == 'Asian':
                asian_2015.append(row['Numerator'])
                asian_2015.append(row['Value'])
            elif row['Ethnicity'] == 'Black':
                black_2015.append(row['Numerator'])
                black_2015.append(row['Value'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2015.append(row['Numerator'])
                mixed_2015.append(row['Value'])
            elif row['Ethnicity'] == 'White':
                white_2015.append(row['Numerator'])
                white_2015.append(row['Value'])
            elif row['Ethnicity'] == 'Other':
                other_2015.append(row['Numerator'])
                other_2015.append(row['Value'])
    # add in the 2019 values for each ethnicity
    for row in data:
        if row['Time'] == '31/03/2019':
            if row['Ethnicity'] == 'Asian':
                asian_2019.append(row['Numerator'])
                asian_2019.append(row['Value'])
            elif row['Ethnicity'] == 'Black':
                black_2019.append(row['Numerator'])
                black_2019.append(row['Value'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2019.append(row['Numerator'])
                mixed_2019.append(row['Value'])
            elif row['Ethnicity'] == 'White':
                white_2019.append(row['Numerator'])
                white_2019.append(row['Value'])
            elif row['Ethnicity'] == 'Other':
                other_2019.append(row['Numerator'])
                other_2019.append(row['Value'])
    # Create dictionary for what we want
    output = []
    # Add Asian data
    asian_change = round(float(asian_2019[1]) - float(asian_2015[1]), 1)
    asian = {'Ethnicity': 'Asian', '2015 total': asian_2015[0], '2015 percentage(%)': asian_2015[1],
             '2019 total': asian_2019[0],
             '2019 percentage(%)': asian_2019[1], 'Change in percentage': asian_change}
    output.append(asian)
    # Add Black data
    black_change = round(float(black_2019[1]) - float(black_2015[1]), 1)
    black = {'Ethnicity': 'Black', '2015 total': black_2015[0], '2015 percentage(%)': black_2015[1],
             '2019 total': black_2019[0],
             '2019 percentage(%)': black_2019[1], 'Change in percentage': black_change}
    output.append(black)
    # Add mixed data
    mixed_change = round(float(mixed_2019[1]) - float(mixed_2015[1]), 1)
    mixed = {'Ethnicity': 'Mixed', '2015 total': mixed_2015[0], '2015 percentage(%)': mixed_2015[1],
             '2019 total': mixed_2019[0],
             '2019 percentage(%)': mixed_2019[1], 'Change in percentage': mixed_change}
    output.append(mixed)
    # Add white data
    white_change = round(float(white_2019[1]) - float(white_2015[1]), 1)
    white = {'Ethnicity': 'White', '2015 total': white_2015[0], '2015 percentage(%)': white_2015[1],
             '2019 total': white_2019[0],
             '2019 percentage(%)': white_2019[1], 'Change in percentage': white_change}
    output.append(white)
    # other data
    other_change = round(float(other_2019[1]) - float(other_2015[1]), 1)
    other = {'Ethnicity': 'Other', '2015 total': other_2015[0], '2015 percentage(%)': other_2015[1],
             '2019 total': other_2019[0],
             '2019 percentage(%)': other_2019[1], 'Change in percentage': other_change}
    output.append(other)

    for i in range(len(output)):
        print(output[i])

    field_names = ['Ethnicity', '2015 total', '2015 percentage(%)', '2019 total', '2019 percentage(%)',
                   'Change in percentage']
    with open('prison_officer_workforce_summary.csv', 'w+') as Prison_Officer_Workforce:
        spreadsheet = csv.DictWriter(Prison_Officer_Workforce, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(output)


def social_workers_summary():
    # create a list of data
    data = read_social_workers_data()

    # 2017-18 data [total amount, percentage]
    all_2017_2018 = []
    asian_2017_2018 = []
    black_2017_2018 = []
    mixed_2017_2018 = []
    white_2017_2018 = []
    other_2017_2018 = []

    # 2016-17 data [total amount, percentage
    all_2016_2017 = []
    asian_2016_2017 = []
    black_2016_2017 = []
    mixed_2016_2017 = []
    white_2016_2017 = []
    other_2016_2017 = []

    # add in the 2017-18 values for each ethnicity
    for row in data:
        if row['Year'] == '2017-18':
            if row['Ethnicity'] == 'All':
                all_2017_2018.append(row['Headcount'])
                all_2017_2018.append('100')
            elif row['Ethnicity'] == 'Asian':
                asian_2017_2018.append(row['Headcount'])
                asian_2017_2018.append(row['Percentage'])
            elif row['Ethnicity'] == 'Black':
                black_2017_2018.append(row['Headcount'])
                black_2017_2018.append(row['Percentage'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2017_2018.append(row['Headcount'])
                mixed_2017_2018.append(row['Percentage'])
            elif row['Ethnicity'] == 'White':
                white_2017_2018.append(row['Headcount'])
                white_2017_2018.append(row['Percentage'])
            elif row['Ethnicity'] == 'Chinese and other':
                other_2017_2018.append(row['Headcount'])
                other_2017_2018.append(row['Percentage'])

    # add in the 2016-17 values for each ethnicity
    for row in data:
        if row['Year'] == '2016-17':
            if row['Ethnicity'] == 'All':
                all_2016_2017.append(row['Headcount'])
                all_2016_2017.append('100')
            elif row['Ethnicity'] == 'Asian':
                asian_2016_2017.append(row['Headcount'])
                asian_2016_2017.append(row['Percentage'])
            elif row['Ethnicity'] == 'Black':
                black_2016_2017.append(row['Headcount'])
                black_2016_2017.append(row['Percentage'])
            elif row['Ethnicity'] == 'Mixed':
                mixed_2016_2017.append(row['Headcount'])
                mixed_2016_2017.append(row['Percentage'])
            elif row['Ethnicity'] == 'White':
                white_2016_2017.append(row['Headcount'])
                white_2016_2017.append(row['Percentage'])
            elif row['Ethnicity'] == 'Chinese and other':
                other_2016_2017.append(row['Headcount'])
                other_2016_2017.append(row['Percentage'])

    # Create dictionary for what we want
    output = []

    # Add Asian data
    asian_change = round(float(asian_2017_2018[1]) - float(asian_2016_2017[1]), 1)
    asian = {'Ethnicity': 'Asian', '2016-17 total': asian_2016_2017[0],
             '2016-17 percentage(%)': asian_2016_2017[1], '2017-18 total': asian_2017_2018[0],
             '2017-18 percentage(%)': asian_2017_2018[1],
             'Change in percentage': asian_change}
    output.append(asian)

    # Add Black data
    black_change = round(float(black_2017_2018[1]) - float(black_2016_2017[1]), 1)
    black = {'Ethnicity': 'Black', '2016-17 total': black_2016_2017[0],
             '2016-17 percentage(%)': black_2016_2017[1], '2017-18 total': black_2017_2018[0],
             '2017-18 percentage(%)': black_2017_2018[1],
             'Change in percentage': black_change}
    output.append(black)

    # Add mixed data
    mixed_change = round(float(mixed_2017_2018[1]) - float(mixed_2016_2017[1]), 1)
    mixed = {'Ethnicity': 'Mixed', '2016-17 total': mixed_2016_2017[0],
             '2016-17 percentage(%)': mixed_2016_2017[1], '2017-18 total': mixed_2017_2018[0],
             '2017-18 percentage(%)': mixed_2017_2018[1],
             'Change in percentage': mixed_change}
    output.append(mixed)

    # Add white data
    white_change = round(float(white_2017_2018[1]) - float(white_2016_2017[1]), 1)
    white = {'Ethnicity': 'White', '2016-17 total': white_2016_2017[0],
             '2016-17 percentage(%)': white_2016_2017[1], '2017-18 total': white_2017_2018[0],
             '2017-18 percentage(%)': white_2017_2018[1],
             'Change in percentage': white_change}
    output.append(white)

    # other data
    other_change = round(float(other_2017_2018[1]) - float(other_2016_2017[1]), 1)
    other = {'Ethnicity': 'Chinese and other', '2016-17 total': other_2016_2017[0],
             '2016-17 percentage(%)': other_2016_2017[1], '2017-18 total': other_2017_2018[0],
             '2017-18 percentage(%)': other_2017_2018[1],
             'Change in percentage': other_change}
    output.append(other)

    for i in range(len(output)):
        print(output[i])

    field_names = ['Ethnicity', '2017-18 total', '2017-18 percentage(%)', '2016-17 total', '2016-17 percentage(%)',
                   'Change in percentage']
    with open('social-workers-for-children-and-families-summary.csv', 'w+') as Social_Service_Workforce:
        spreadsheet = csv.DictWriter(Social_Service_Workforce, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(output)


def choose_workforce():
    print('Which workforce would you like the summary of? (Civil Service / Fire and Rescue / Prison Officer / Social '
          'Workers)')
    workforce = input('Please enter as shown above: ')

    if workforce == 'Civil Service':
        civil_service_summary()
        print('A csv has been created')
    elif workforce == 'Fire and Rescue':
        fire_and_rescue_summary()
        print('A csv has been created')
    elif workforce == 'Prison Officer':
        prison_officer_summary()
        print('A csv has been created')
    elif workforce == 'Social Workers':
        social_workers_summary()
        print('A csv has been created')
    else:
        print('Please enter workforce as shown.')


choose_workforce()
