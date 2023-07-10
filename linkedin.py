from linkedin import linkedin

# Set your LinkedIn API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
def post_to_linkedin(title, text):
    app = linkedin.LinkedInApplication(token=access_token)
    app.submit_share(title=title, comment=text)
    print("Post successfully shared on LinkedIn!")
def main():
    title = input("Enter your LinkedIn post title: ")
    text = input("Enter your LinkedIn post text: ")
    post_to_linkedin(title, text)

if __name__ == "__main__":
    main()
