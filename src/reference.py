from flask import session
from sqlalchemy.sql import text
#import app
#from db import db


def add_book(title, author, year, publisher, url, db):
    sql = text(
        '''INSERT INTO books (title, author, b_year, publisher, b_url)
        VALUES (:title, :author, :year, :publisher, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "url": url
    })
    db.session.commit()


def get_books(db):
    sql = text(
        '''SELECT book_id, title, author, b_year, publisher, b_url FROM books''')
    result = db.session.execute(sql)
    books = result.fetchall()
    return books


def delete_book(book_id, db):
    sql = text(
        '''DELETE FROM books WHERE book_id=:id''')
    db.session.execute(sql, {"id": book_id})
    db.session.commit()
    return


def add_article(title, author, year, journal, url, db):
    sql = text(
        '''INSERT INTO articles (title, author, a_year, journal, a_url)
        VALUES (:title, :author, :year, :journal, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "journal": journal,
        "url": url
    })
    db.session.commit()


def get_articles(db):
    sql = text(
        '''SELECT article_id, title, author, a_year, journal, a_url FROM articles''')
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles


def delete_article(article_id, db):
    sql = text(
        '''DELETE FROM articles WHERE article_id=:id''')
    db.session.execute(sql, {"id": article_id})
    db.session.commit()
    return


def add_inproceeding(title, author, year, url, db):
    sql = text(
        '''INSERT INTO inproceedings (title, author, i_year, i_url)
        VALUES (:title, :author, :year, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "url": url
    })
    db.session.commit()


def get_inproceedings(db):
    sql = text(
        '''SELECT inproceeding_id, title, author, i_year, i_url FROM inproceedings''')
    result = db.session.execute(sql)
    inproceedings = result.fetchall()
    return inproceedings


def delete_inproceeding(inproceeding_id, db):
    sql = text(
        '''DELETE FROM inproceedings WHERE inproceeding_id=:id''')
    db.session.execute(sql, {"id": inproceeding_id})
    db.session.commit()
    return


def initialize_test_database(db):
    schemafile = open("delschema.sql", "r")
    sql = text(schemafile.read())
    schemafile.close()
    db.session.execute(sql)
    schemafile2 = open("schema.sql", "r")
    sql = text(schemafile2.read())
    schemafile2.close()
    db.session.execute(sql)
    db.session.commit()