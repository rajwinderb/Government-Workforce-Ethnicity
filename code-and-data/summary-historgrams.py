import pandas as pd
import matplotlib.pyplot as plt


# create civil service plot
def plot_civil_data():
    # import data
    data = pd.read_csv('summary-data/civil-service-workforce-summary.csv')

    # create plot
    plt.bar(data['Ethnicity'], data['Change in percentage'])
    plt.ylabel('Change in Percentage')
    plt.xlabel('Ethnicity')
    plt.title('Change in percentage of Ethnicity in the Civil Service Workforce between 2015 & 2019')

    plt.show()


# create fire and rescue plot
def plot_fire_and_rescue_data():
    # import data
    data = pd.read_csv('summary-data/fire-and-rescue-workforce-summary.csv')

    # create plot
    plt.bar(data['Ethnicity'], data['Change in percentage'])
    plt.ylabel('Change in Percentage')
    plt.xlabel('Ethnicity')
    plt.title('Change in percentage of Ethnicity in the Fire and Rescue Workforce between 2015 & 2019')

    plt.show()


# create prison officer plot
def plot_prison_officer_data():
    # import data
    data = pd.read_csv('summary-data/prison_officer_workforce_summary.csv')

    # create plot
    plt.bar(data['Ethnicity'], data['Change in percentage'])
    plt.ylabel('Change in Percentage')
    plt.xlabel('Ethnicity')
    plt.title('Change in percentage of Ethnicity in the Prison Officer Workforce between 2015 & 2019')

    plt.show()


# create social workers plot
def plot_social_workers_data():
    # import data
    data = pd.read_csv('summary-data/social-workers-for-children-and-families-summary.csv')

    # create plot
    plt.bar(data['Ethnicity'], data['Change in percentage'])
    plt.ylabel('Change in Percentage')
    plt.xlabel('Ethnicity')
    plt.title('Change in percentage of Ethnicity in the Social Workers Workforce between 2016-17 & 2017-18')

    plt.show()

plot_civil_data()
plot_prison_officer_data()
plot_fire_and_rescue_data()
plot_social_workers_data()