import csv
import requests

def fetch_and_print_posts():
    # Send GET request to fetch posts
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Print status code
    print("Status Code:", response.status_code)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        posts = response.json()

        # Print titles of all posts
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Send GET request to fetch posts
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        posts = response.json()

        # Define CSV file path
        csv_file = 'posts.csv'

        # Write fetched data into a CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()