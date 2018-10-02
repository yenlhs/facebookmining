import os 
import json 
import facebook 
import requests 
 
if __name__ == '__main__': 
  token = os.environ.get('ACCESS_TOKEN') 
 
  graph = facebook.GraphAPI(token) 
  posts = graph.get_connections('me', 'posts') 
 
  while True:  # keep paginating 
    try: 
      with open('my_posts.json', 'a') as f: 
        for post in posts['data']: 
          f.write(json.dumps(post)+"\n") 
        # get next page 
        posts = requests.get(posts['paging']['next']).json() 
    except KeyError: 
      # no more pages, break the loop 
      break 