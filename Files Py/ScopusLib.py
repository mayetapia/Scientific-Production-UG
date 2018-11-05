# -*- encoding: utf-8 -*-


import pandas as pd
import requests
import json


API_KEY = '' # set here the API KEY

########## Retrieve documents related to a given affiliation id
def get_docs_affil(AFFIL_ID):
  url = ("http://api.elsevier.com/content/search/scopus?query=AF-ID("
        + AFFIL_ID + ')')
  resp = requests.get(url,
                   headers={'Accept':'application/json',
                           'X-ELS-APIKey': API_KEY})
  results = json.loads(resp.text.encode('utf-8'))
  r = pd.DataFrame(results["search-results"]["entry"])
  return r

########## Retrieve information of affiliations
def get_info_affil(AFFIL_ID):
  #for use af = get_info_affil('60072042')
  url = ("http://api.elsevier.com/content/affiliation/affiliation_id/"
        + AFFIL_ID)
  resp = requests.get(url,
                   headers={'Accept':'application/json',
                           'X-ELS-APIKey': API_KEY})
  results = json.loads(resp.text.encode('utf-8'))
  r = pd.DataFrame(results["affiliation-retrieval-response"])
  return r

########## Retrieve metadata of papers
def get_info_paper(PAPER_ID):
  #To use: p = get_info_paper('85005950245')
  url = ("http://api.elsevier.com/content/abstract/scopus_id/"
      + PAPER_ID)
  resp = requests.get(url,
                  headers={'Accept':'application/json',
                             'X-ELS-APIKey': API_KEY})
  results = json.loads(resp.text.encode('utf-8'))
  r = pd.DataFrame(results)
  return r

########## Retrieve metadata of authors
def get_info_author(AF_ID):
  #To use: a = get_info_author('26432947200') 
  url = ("http://api.elsevier.com/content/author/author_id/"
          + AF_ID)
  resp = requests.get(url,
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': API_KEY})
  results = json.loads(resp.text.encode('utf-8'))
  r = pd.DataFrame(results['author-retrieval-response'])
  return r

#####################################################
#Instructions to use ScopusLib functions
# update the variable API_KEY, set at the top of this file
#$ import ScopusLib as s
#$ ug = s.get_docs_affil('60072042')   # Retrieve information about affiliation



 