import facebook

# Set your access token and Page ID
access_token = 'YOUR_ACCESS_TOKEN'
page_id = 'YOUR_PAGE_ID'

def post_to_facebook(message):
    graph = facebook.GraphAPI(access_token)
    graph.put_object(page_id, "feed", message=message)
    print("Post successfully posted to Facebook!")

def main():
    message = input("Enter your Facebook post message: ")
    post_to_facebook(message)

if __name__ == "__main__":
    main()
