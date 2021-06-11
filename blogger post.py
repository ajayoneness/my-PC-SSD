from goco import Goco

GoogleApi = Goco("path\\to\\client_secret.json", "path\\to\\credentials.storage")

MyBlog = GoogleApi.connect(scope='Blogger', service_name='blogger', version='v3')

Posts = MyBlog.posts().list(blogId='desired-blog-id').execute()

print(Posts)