from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts


def make_post(content):
    wp = Client(f'https://newspyy.wordpress.com/xmlrpc.php','newspyy','@J@y12345')
    post = WordPressPost()
    post.title = content['title']
    post.content = content['body']
    post.terms_names = {
        'post_tag': ['AutoBlogger', 'BotPosted'],
        'category': ['News', 'Update']
    }
    filename = '1.jpg'
    data = {
        'name': '1.jpg',
        'type': 'image/jpeg'
    }

    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())
        response = wp.call(media.UploadFile(data))
    attachment_id = response['id']

    post.thumbnail = attachment_id
    post.post_status = 'publish'
    post.id = wp.call(posts.NewPost(post))
    print("Sucessfully Posted To Our Blog !")
