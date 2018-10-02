import os 
import facebook 
import json 
 
if __name__ == '__main__': 
  token = os.environ.get('ACCESS_TOKEN') 
 
  graph = facebook.GraphAPI(token) 
  user = graph.get_object("me") 
  friends = graph.get_connections(user["id"], "friends") 
  print(json.dumps(friends, indent=4)) 