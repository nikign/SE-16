from GoogleSearch.googlesearch import main_search_web
from GoogleSearch.googlesearch import main_search_email

from GoogleSearch.DB_Search import main_searchDB_web
from GoogleSearch.DB_Search import main_searchDB_email

#Query = "CONFLICT (content): Merge conflict in README.md.Automatic merge failed: fix conflicts and then commit the result."
path = "/Users/BARNES_3/Documents/niki/SE-16/git_helper/"


def get_web_results(search_phrase):
    result = main_search_web(search_phrase)
    #print result
    return result

def get_email_result(error_message):
    res = main_searchDB_email(error_message,path)
    # res = main_search_email(error_message)
    print 'outside !!!!!!!!!!!!!!!!!!!!!!!!!'
    # res = 'q', 'a', 'l'
    return res

#print get_email_result(Query)


