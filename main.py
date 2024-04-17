import tweepy
import requests

api_key = "ZjDnwwqdKu3ih3hle7D4Tmjok"
api_secret = "L6MztbSl1YL73CcFR93slcOc5Rezs0hcxRZPwtrKMFqKIvIqi8"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAADl5tQEAAAAAFGGqjmD%2BkILJTvXWf5dJthYxx40%3DtMuQLpNRQonjGRbF0KPTDPFPH5ZYxBWjYhtkdamyHwzdMTRuRP"
access_token = "1780624937616560130-zRs9DVBzlKbLMyJJcjSAHTmV6ILdc7"
access_token_secret = "10USkn9eo6sFK9weBnrRfMj42KSBxSUErnkAkXtsTDJIO"


def frame_to_time(frame_number):
    hours = frame_number // 3600
    frame_number %= 3600
    minutes = frame_number // 60
    seconds = frame_number % 60
    time_str = "[{:02d}:{:02d}:{:02d}]".format(hours, minutes, seconds)
    return time_str


# api=tweepy.API(auth,wait_on_rate_limit=True)
# media_id=api.media_upload(filename='images.jpeg')


def twitConnection():
    client = tweepy.Client(
        bearer_token,
        api_key,
        api_secret,
        access_token,
        access_token_secret,
        wait_on_rate_limit=True,
    )

    return client


def twitConnection1():
    auth = tweepy.OAuth1UserHandler(
        api_key, api_secret, access_token, access_token_secret
    )
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def get_image(i):
    repo_owner = "Vishwaa-Arumugam"
    repo_name = "temp"
    file_path = f"extracted_frames/frame_{i}.jpg"
    print(file_path)

    api_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    )

    response = requests.get(api_url)

    if response.status_code == 200:
        file_info = response.json()
        download_url = file_info["download_url"]

        file_response = requests.get(download_url)

        if file_response.status_code == 200:
            with open("downloaded_image.jpg", "wb") as f:
                f.write(file_response.content)
            print("Image downloaded successfully.")
        else:
            print("Failed to download image.")
    else:
        print("Failed to fetch file metadata.")


if __name__ == "__main__":

    client = twitConnection()

    client1 = twitConnection1()

    with open("data.txt", "r") as file:
        # mymedia=r'C:\Users\vijay\OneDrive - SSN Trust\Desktop\SSN\sem 6\tweepy folder\images.jpeg'
        data = file.read()
        i = int(data)

    media = client1.media_upload(filename=get_image(i))
    media_id = media.media_id

    msg = frame_to_time(i)

    response = client.create_tweet(text=msg, media_ids=[media_id])

    with open("data.txt", "w") as file:
        file.write(i + 1)
