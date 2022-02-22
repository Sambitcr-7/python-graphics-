import instaloader

ig = instaloader.Instaloader()
dp = input("Enter Insta Username :")

ig.download_proflie(dp, profile_pic_only = True)