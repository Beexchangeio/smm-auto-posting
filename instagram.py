from instabot import Bot

# Create an instance of the InstaBot class
bot = Bot()
bot.login(username='your_username', password='your_password')
def post_to_instagram(caption, image_path):
    bot.upload_photo(image_path, caption=caption)
    print("Post successfully uploaded to Instagram!")
def main():
    caption = input("Enter your Instagram post caption: ")
    image_path = input("Enter the path to your image: ")
    post_to_instagram(caption, image_path)

if __name__ == "__main__":
    main()
