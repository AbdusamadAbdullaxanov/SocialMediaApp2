from django.test import TestCase
from youtube_search import YoutubeSearch

# Create your tests here.

a = YoutubeSearch("lamar", max_results=1)
print(a.to_dict())
# id
# title
# views
# likes
