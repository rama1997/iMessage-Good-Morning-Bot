import requests
import requests.auth
import random
import glob
import os
from iMessage import send_message, send_picture
from config import (
    REDDIT_USER,
    REDDIT_PASS,
    REDDIT_API_ID,
    REDDIT_API_SECRET,
    SUBREDDITS,
    DOG_PIC_MESSAGE,
)


def call_reddit_api(subreddit):
    """Calls Reddit API and returns a recent hot image/gif from a given subreddit

    Args:
        subreddit (str): This is the given suberddit to search for a dog picture

    Returns:
        json: Returns the data associated with the GET request of Reddit
    """

    # Step 1. Getting Authentication Info
    client_auth = requests.auth.HTTPBasicAuth(REDDIT_API_ID, REDDIT_API_SECRET)
    post_data = {
        "grant_type": "password",
        "username": REDDIT_USER,
        "password": REDDIT_PASS,
    }
    headers = {"User-Agent": "Test"}

    # Step 2. Getting Token Access Id
    TOKEN_ACCESS_ENDPOINT = "https://www.reddit.com/api/v1/access_token"
    response = requests.post(
        TOKEN_ACCESS_ENDPOINT, data=post_data, headers=headers, auth=client_auth
    )
    if response.status_code == 200:
        token_id = response.json()["access_token"]

    # Step 3. Use Reddit's REST API to perform operations
    OAUTH_ENDPOINT = "https://oauth.reddit.com"
    params_get = {
        "limit": 15,
    }
    headers_get = {"User-Agent": "Test", "Authorization": "Bearer " + token_id}
    # Get recent hot posts from subreddit
    response = requests.get(
        OAUTH_ENDPOINT + "/r/{}/hot/".format(subreddit),
        headers=headers_get,
        params=params_get,
    )
    return response.json()


def valid_content_format(post) -> bool:
    """Given a Reddit post, determine if the post's content is in a valid format (a single image)

    Args:
        post (): A reddit post containing content
    """

    from_youtube = True if post["data"]["domain"] == "youtu.be" else False
    stickied_post = True if post["data"]["stickied"] == True else False
    is_video = True if post["data"]["is_video"] == True else False
    is_gallery = True if "is_gallery" in post["data"].keys() else False

    is_valid = (
        True
        if not stickied_post and not is_gallery and not from_youtube and not is_video
        else False
    )
    return True if is_valid else False


def download_image_content(image_url):
    """Given an image url, download the content of the image

    Args:
        image_url (str): URL link to image
    """

    # Open the url image, set stream to True, this will return the stream content.
    response = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if response.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        response.raw.decode_content = True

        # Get file extension of image
        extension = ".jpeg"
        for ext in ("mp4", "png", "gif", "jpeg", "jpg"):
            if ext in image_url:
                extension = "." + ext

        # Create output file
        file_name = "dog_picture" + extension

        # Remove former dog file, need for Applescript
        for old_file in glob.glob("dog_picture*"):
            os.unlink(old_file)

        # Open a local file with wb ( write binary ) permission.
        with open(file_name, "wb") as f:
            f.write(response.content)


def send_dog_pic(recipient_number):
    """Obtains a dog picture from reddit and sends it to the given number

    Args:
        recipient_number (str): Phone number of desired recipient
    """

    subreddit = random.choice(SUBREDDITS)
    subreddit_data = call_reddit_api(subreddit)
    posts = subreddit_data["data"]["children"]

    # Returns url for a post's content only if it is a single image
    for post in posts:
        if valid_content_format(post):
            title = post["data"]["title"]
            url = post["data"]["url"]
            download_image_content(url)
            break

    if title and url:
        send_message(
            recipient_number=recipient_number,
            message=DOG_PIC_MESSAGE.format(TITLE=title, URL=url).replace("'", ""),
        )
        # send_picture(recipient_number=recipient_number)
