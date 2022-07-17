# CNT 4713 Net-Centric Computing Project

This project contains a web application to host a static and live feed.

You can visit the project website <a href="https://dropcube-cnt-4713-project.herokuapp.com/" target="_blank" rel="noopener noreferrer">here</a>

Note: The sample website is currently whitelisted. You may sill register, but accounts that are not whitelisted will be logged out and returned home.

## Implementation
- Python/Flask
- Auth0

## Requirements

To run the application, make sure you have `python3` and `pip` installed.

All dependencies/requirements are in the requirements.txt file.

To install the dependencies:

Locate and cd to the project directory.

```
cd <project directory>
```

Type the following command to install all the requirements.

```
pip3 install -r requirements.txt
```

## Live Feed

The live feed uses OpenCV to get the users webcam stream.

In order to ge live feed working, a user must run webcam.py locally.

After running webcam.py locally, the user can use Ngrok to forward their stream to an address generated by Ngrok.

Since we are using Ngrok's free tier, we must update the `img src=URL/video_feed`  to the url address generated by Ngrok followed by a '/video_feed' endpoint.