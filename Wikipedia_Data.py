import requests
from bs4 import BeautifulSoup

def get_wikipedia_page_content(page_title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": page_title,
        "format": "json",
        "prop": "text",
        "redirects": 1,  # Ensure that redirects are followed
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if the response contains 'parse' key
        if 'parse' in data:
            html_content = data['parse']['text']['*']
            return html_content
        else:
            print(f"Page not found or redirect issue for '{page_title}'")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

def extract_summary(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    first_paragraph = soup.find('p')
    if first_paragraph:
        return first_paragraph.get_text()
    return "No summary available."

def extract_references(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    references = []
    for ref in soup.find_all("span", class_="reference-text"):
        references.append(ref.get_text())
    return references

def write_to_file(page_title, summary, references):
    file_name = f"{page_title}_info.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Summary:\n")
        file.write(summary + "\n\n")
        file.write("References:\n")
        for i, ref in enumerate(references, start=1):
            file.write(f"Reference {i}: {ref}\n")

page_title = "Artificial Intelligence"
html_content = get_wikipedia_page_content(page_title)

if html_content:
    summary = extract_summary(html_content)
    references = extract_references(html_content)

    print("Summary:")
    print(summary)
    print("\nReferences:")
    for i, ref in enumerate(references, start=1):
        print(f"Reference {i}: {ref}")

    write_to_file(page_title, summary, references)
    print(f"\nData written to {page_title}_info.txt")
else:
    print("Failed to get page content.")
