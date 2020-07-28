

key = "AIzaSyD-35A5jFeuAMvyxESuZZxJJbHl2GkDvBQ"


from google_images_search import GoogleImagesSearch
import requests

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyD-35A5jFeuAMvyxESuZZxJJbHl2GkDvBQ', '008046156900458172849:slbk4b8_ww0')

# define search params:
_search_params = {
    'q': 'Chuck Schumer',
    'num': 10,
    'safe': 'off',
    'fileType': 'jpg',
    'imgType': 'photo',
    'imgSize': 'MEDIUM',
    'imgDominantColor': 'black'
}

# this will only search for images:
image = gis.search(search_params=_search_params)

print(image)


# # this will search and download:
gis.search(search_params=_search_params, path_to_dir='/static/images')

# # this will search, download and resize:
# gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# # search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
#     image.download('/path/')
#     image.resize(500, 500)



# import requests
# key = "3DqvUGwMNpqwZ7oiHy6tGJpNM1B2Ih94"
# # endpoint = "https://api.giphy.com/v1/gifs/search?api_key={key}&q=frog&limit=25&offset=0&rating=g&lang=en"
# # results = requests.get(endpoint).json()

# def getImageUrlFrom(query):
#     endpoint = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=g&lang=en"
#     results = requests.get(endpoint).json()
#     return results["data"][0]["images"]["original"]['url']