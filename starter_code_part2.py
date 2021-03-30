# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 02:44:03 2021

@author: proo
"""

# Import Library

import psycopg2
from psycopg2 import Error

# Complete the function to create connection


def getConnection():
    
    # Write Your Code Here
    connection = psycopg2.connect(
        host='localhost', user='postgres', password='tiamz', database='postgres')
    return connection



def closeConnection(connection):
    
    connection.close()
    print("Connection is Closed")


def getCustomer(customer_id):
    
    try:
        connection = getConnection()  # Create a connection using the connection function
        
        #  Create a cursor object from the connection
        cursor = connection.cursor()


        query = "SELECT * FROM CUSTOMER WHERE customer_id = %s"
 
        cursor.execute(query, (customer_id,))
    
        
        records = cursor.fetchall()

        print("Printing Records")
        
        for row in records:
            print('Customer ID', row[0])
            
            print('Store ID', row[1])
            
            print('First Name', row[2])
            
            print('Last Name', row[3])
            
            print('Email', row[4])
            
            print('Address ID', row[5])
            
            print('Active Status', row[6])
            
            print('Create Date', row[7])
            
            print('Last Update', row[8])
            
            print('Active', row[9], '\n')

        closeConnection(connection)  # Closes the connection
    except Error as e:
        print("Error: Reading Record")


# Using the getCustomer function, print out the customer information for customer_id = 34
getCustomer(34)
