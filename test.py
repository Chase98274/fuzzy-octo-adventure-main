from facebook_scraper import get_posts

for post in get_posts('2920544088167018', pages=10):
    print(post)