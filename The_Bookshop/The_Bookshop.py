#!/bin/python3

import math
import os
import random
import re
import sys

def makebook(isbn,title,authors,genre,year,qtystck,saleprice):
    """constructor - creates a book"""
    return [isbn,title,authors,genre,year,qtystck,saleprice]

def bookshop():
    """constructor- creates a new bookshop"""
    return ("bookshop",[])

def books(bookshop):
    """accessor - returns the books of a bookshop"""
    return bookshop[1]

def add_book(book,bookshop):
    """constructor - adds a book to the bookshop"""
    return bookshop[1].append(book)


# Include the following accessor functions (from PROBLEM1) below.
#

def get_isbn(book):
    isbn = book[0]
    return isbn 

def get_title(book):
    title = book[1]
    return title

def get_authors(book):
    authors = book[2]
    return authors

def get_genre(book):
    genre = book[3]
    return genre

def get_year(book):
    year = book[4]
    return year
  
def get_qty(book):
    qty = book[5]
    return qty

def get_saleprice(book):
    saleprice = book[6]
    return saleprice



#
# Complete the 'books_to_reorder' function below.
#
# The function is expected to return a LIST OF TUPLES.
# The function accepts following parameters:
#  1. BOOKSHOP_ADT bookshop
#  2. INTEGER reorder
#

def books_to_reorder(bookshop, reorder):
    # Write your code here
      # Write your code here
    list = []
    for book in books(bookshop):
        if get_qty(book) <= reorder:
            list.append((get_isbn(book),get_title(book)))
    return list
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    uwi_bookshop=bookshop()
    
    book_count = int(input().strip())
    
    for _ in range(book_count):
        book = input().split(',')
        isbn = book[0]
        title = book[1]
        no_of_authors = int(book[2])
        authors = []
        for i in range(no_of_authors):
            authors += [book[3+i]]
        genre = book[3+no_of_authors]
        year = int(book[4+no_of_authors])
        qtystck = int(book[5+no_of_authors])
        saleprice = float(book[6+no_of_authors])
        b1= makebook(isbn,title,authors,genre,year,qtystck,saleprice)
        add_book(b1,uwi_bookshop)

    reorder = int(input().strip())

    bks = books_to_reorder(uwi_bookshop, reorder)
    str1 = '['
    if len(bks) > 0:
        str1 += '('
        for i in range(2):
            str1 += bks[0][i]
            if i == 0:
                str1 += ', '
        str1 += ')'
    for bk in bks[1:]:
        str1 += ', ('
        for i in range(2):
            str1 += bk[i]
            if i == 0:
                str1 += ', '
        str1 += ')'
    str1 += ']'
    fptr.write(str1 + '\n')

    fptr.close()
