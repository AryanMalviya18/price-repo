# from flask import Flask, request, jsonify
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
# import json

# app = Flask(__name__)

# # Your web scraping functions (e.g., get_price, get_image, etc.) here...
# # Function to extract Product Title


# def get_title(soup):

#     try:
#         # Outer Tag Object
#         title = soup.find("span", attrs={"id": 'productTitle'})

#         # Inner NavigatableString Object
#         title_value = title.text

#         # Title as a string value
#         title_string = title_value.strip()

#     except AttributeError:
#         title_string = ""

#     return title_string


# # Function to extract Product Price
# def get_price(soup):
#     try:
#         # Locate the outermost <span> element with class "a-price"
#         price_element = soup.find("span", class_="a-price")

#         # Extract the price from within the <span> element
#         price = price_element.find(
#             "span", class_="a-price-whole").get_text(strip=True)
#     except AttributeError:
#         price = "Price not found"
#     return price


# # Function to extract Product Rating
# def get_rating(soup):

#     try:
#         rating = soup.find(
#             "i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

#     except AttributeError:
#         try:
#             rating = soup.find(
#                 "span", attrs={'class': 'a-icon-alt'}).string.strip()
#         except:
#             rating = ""

#     return rating

# # Function to extract Number of User Reviews


# def get_review_count(soup):
#     try:
#         review_count = soup.find(
#             "span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

#     except AttributeError:
#         review_count = ""

#     return review_count


# # Function to extract Product Image
# def get_image(soup):
#     try:
#         image = soup.find("div", {'id': 'imgTagWrapperId'}).find("img")
#         img_link = image['src']
#     except AttributeError:
#         img_link = "Image not available"
#     return img_link


# @app.route('/')
# def index():
#     return "Welcome to the Amazon Product API"


# @app.route('/search/<query>')
# def search_amazon_product(query):
#     # Add your web scraping logic here based on the provided query
#     # Perform the scraping, create a JSON response, and return it
#         # The webpage URL
#     URL = "https://www.amazon.in/s?k=samsung+galaxy+s23+ultra&crid=18C6G5YYE27LD&sprefix=samsung+gala%2Caps%2C334&ref=nb_sb_ss_ts-doa-p_1_12"
#         # add your user agent
#     # HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", 'referer': URL}
#     HEADERS = json.dumps({
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#     'referer': URL
# })
#     # HTTP Request
#     webpage = requests.get(URL, headers=HEADERS)

#     # //Soup Object containing all data
#     soup = BeautifulSoup(webpage.content, "html.parser")

#     # Fetch links as List of Tag Objects
#     links = soup.find_all('a', attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

#     # Store the links
#     links_list = []

#     # Loop for extracting links from Tag Objects
#     for link in links:
#         links_list.append(link.get('href'))
#     links_list = [item for item in links_list if item.startswith('/')]

#     d = {"title": [], "price": [], "rating": [], "reviews": [], "image": []}

#     # Loop for extracting product details from each link
#     for link in links_list:
#         new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

#         new_soup = BeautifulSoup(new_webpage.content, "html.parser")

#         # Function calls to display all necessary product information
#         d['title'].append(get_title(new_soup))
#         d['price'].append(get_price(new_soup))
#         d['rating'].append(get_rating(new_soup))
#         d['reviews'].append(get_review_count(new_soup))
#         d['image'].append(get_image(new_soup))

#     amazon_df = pd.DataFrame.from_dict(d)
#     amazon_df['title'].replace('', np.nan, inplace=True)
#     amazon_df = amazon_df.dropna(subset=['title'])
#     amazon_df.to_csv("amazon_data.csv", header=True, index=False)
#     # Example:
#     amazon_url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
#     # Your scraping code here...

#     try:
#         response = requests.get(amazon_url, headers={"User-Agent": HEADERS})
#         response.raise_for_status()  # Check for request errors

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract product details based on your scraping functions
#         title = get_title(soup)
#         price = get_price(soup)
#         rating = get_rating(soup)
#         reviews = get_review_count(soup)
#         image = get_image(soup)

#         # Create a JSON response with the scraped data
#         response_data = {
#             'title': title,
#             'price': price,
#             'rating': rating,
#             'reviews': reviews,
#             'image': image
#             }

#     except Exception as e:
#         # Handle exceptions (e.g., request errors, parsing errors)
#         response_data = {
#         'error': str(e)
#     }

#     return jsonify(response_data)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3030)


from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

app = Flask(__name__)

# Your web scraping functions here...
# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})

        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price 
def get_price(soup):
    try:
        # Locate the outermost <span> element with class "a-price"
        price_element = soup.find("span", class_="a-price")

        # Extract the price from within the <span> element
        price = price_element.find("span", class_="a-price-whole").get_text(strip=True)
    except AttributeError:
        price = "Price not found"
    return price




# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count



# Function to extract Product Image
def get_image(soup):
    try:
        image = soup.find("div", {'id': 'imgTagWrapperId'}).find("img")
        img_link = image['src']
    except AttributeError:
        img_link = "Image not available"
    return img_link


@app.route('/')
def index():
    return "Welcome to the Amazon Product API"

@app.route('/search/<query>')
def search_amazon_product(query):
    try:
        # Create the Amazon search URL based on the user's query
        amazon_url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"

        # Set the User-Agent header
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        # Send a request to Amazon
        response = requests.get(amazon_url, headers=headers)
        response.raise_for_status()  # Check for request errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product details using your web scraping functions
        title = get_title(soup)
        price = get_price(soup)
        rating = get_rating(soup)
        reviews = get_review_count(soup)
        image = get_image(soup)

        # Create a JSON response
        response_data = {
            'title': title,
            'price': price,
            'rating': rating,
            'reviews': reviews,
            'image': image
        }

    except Exception as e:
        # Handle exceptions (e.g., request errors, parsing errors)
        response_data = {
            'error': str(e)
        }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)
