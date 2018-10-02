import os 
import json 
from argparse import ArgumentParser 
import facebook 
import requests 
 
def get_parser(): 
  parser = ArgumentParser() 
  parser.add_argument('--page') 
  parser.add_argument('--n', default=100, type=int) 
  return parser 
 
if __name__ == '__main__': 
  parser = get_parser() 
  args = parser.parse_args() 
 
  token = os.environ.get('ACCESS_TOKEN') 
  page_id = os.environ.get('FB_PAGE_ID')
 
  graph = facebook.GraphAPI(token) 
  all_fields = [ 
    'id', 
    'message', 
    'created_time', 
    'shares', 
    'likes.summary(true)', 
    #'comments{id,message,created_time,comments}' 
    'comments.summary(true)'
  ] 
  all_fields = ','.join(all_fields) 
  posts = graph.get_connections(page_id, 
                                'posts', 
                                fields=all_fields) 
 
  downloaded = 0 
  while True:  # keep paginating 
    if downloaded >= args.n: 
      break 
    try: 
      fname = "posts_{}.json".format(args.page) 
      with open(fname, 'a') as f: 
        for post in posts['data']: 
          downloaded += 1 
          f.write(json.dumps(post)+"\n") 
        # get next page 
        posts = requests.get(posts['paging']['next']).json() 
    except KeyError: 
      # no more pages, break the loop 
      break 