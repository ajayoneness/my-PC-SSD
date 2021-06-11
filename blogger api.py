from googleapiclient.discovery import build




Key="AIzaSyA0G4gqRzucY9glzW4fdNc1FEK6eima1ag"
id = "2301448740362257948"

blog = build('blogger', 'v3', developerKey=Key)
resp = blog.blogs().get(blogId=id).execute()
print(resp)


