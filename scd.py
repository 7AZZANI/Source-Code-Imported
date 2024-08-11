import requests
import sys

def download_source(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Get the content (source code) of the page
        source_code = response.text
        
        # Generate a filename based on the URL
        filename = url.split('//')[1].split('/')[0] + '.html'
        
        # Save the source code to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(source_code)
        
        print(f"Source code downloaded successfully. Saved as {filename}")
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    download_source(url)