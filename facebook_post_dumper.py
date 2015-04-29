#!/usr/share/bin/python

# script by Jeff Lockhart
# downloaded from https://github.com/jwlockhart/facebook_post_dumper
# modeled after this tweet dumping script: https://gist.github.com/yanofsky/5436496
# see the README.md file for instructions

import facebook
import requests
import pandas as pd

#Facebook access token
token = ""

#the ID of the facebook page, group, or person you want to download posts from
pid = ""

#without an upper bound, this script may download way more than you want
max_posts = 3000



def process_page(page):
  # convert a page of results into posts
  posts = pd.DataFrame(page['data'])
  return posts[['id', 'created_time', 'type', 'message', 'story', 'link', 'description']]

def get_all_posts(page_id):
  all_posts = pd.DataFrame()
  
  #authorize facebook, initialize graphAPI:  
  graph = facebook.GraphAPI(access_token = token)#, version = '2.2')
  print "Connected to facebook. Starting download of posts from %s..." % page_id
  
  #facebook restricts this call to 250 results and paginates.
  page = graph.get_connections(id = page_id, connection_name = 'posts', limit = 250)
  last_posts = process_page(page)
  all_posts = all_posts.append(last_posts)
  
  print "%s posts downloaded so far..." % (len(all_posts.index))
  
  #keep paging through results until there are none
  while len(last_posts.index) > 0 and len(all_posts.index) < max_posts:
    page = requests.get(page['paging']['next']).json()
    last_posts = process_page(page)
    all_posts = all_posts.append(last_posts)
    
    print "%s posts downloaded so far..." % (len(all_posts.index))
  
  #write the csv
  all_posts.to_csv(page_id +'.csv', encoding = 'utf-8')
  
  print "Done!"



if __name__ == '__main__':
  get_all_posts(pid) #the garbage there is the page ID
  
  
