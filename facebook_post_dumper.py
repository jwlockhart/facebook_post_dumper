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

#the fields you would like to save for each post, in your desired order. 
#other fields exist, but some are complex objects, like 'comments' which is a bit like posts inside posts.
fields = ['id', 'created_time', 'type', 'message', 'story', 'link', 'description']

def process_page(page):
  # convert a page of results into posts
  
  #dummy df to ensure we have the right column names even if the data is missing
  dummy = pd.DataFrame(columns = fields)

  posts = pd.DataFrame(page['data'])
  posts = posts.append(dummy)

  # if we run out of posts
  if len(posts.index) > 0:
    #select and order the data we want out of the posts, dropping the other columns
    return posts[fields]
  else:
    return posts


def get_all_posts(page_id):
  # fetch all posts (up to max_posts) from this page
  
  all_posts = pd.DataFrame()
  
  #authorize facebook, initialize graphAPI:  
  graph = facebook.GraphAPI(access_token = token)#, version = '2.2')
  print "Connected to facebook. Starting download of posts from %s..." % page_id
  
  #facebook restricts this call to ~250 results and paginates.
  page = graph.get_connections(id = page_id, connection_name = 'posts', limit = 250)
  last_posts = process_page(page)
  all_posts = all_posts.append(last_posts)
  
  print "%s posts downloaded so far..." % (len(all_posts.index))
  
  #keep paging through results until there are none
  while len(last_posts.index) > 0 and len(all_posts.index) < max_posts:
    #fetch the next page of results from facebook
    page = requests.get(page['paging']['next']).json()
    last_posts = process_page(page)
    
    #combine the posts we just pulled with the ones from earlier
    all_posts = all_posts.append(last_posts)
    
    print "%s posts downloaded so far..." % (len(all_posts.index))
  
  #write the csv - uft-8 encoding is needed to match the data from fb
  all_posts.to_csv(page_id +'.csv', encoding = 'utf-8')
  
  print "Done!"


if __name__ == '__main__':
  get_all_posts(pid) 
  
  
