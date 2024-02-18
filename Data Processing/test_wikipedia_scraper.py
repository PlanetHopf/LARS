import unittest
import os
from Wikipedia_Data import get_wikipedia_page_content, extract_summary, extract_references

class TestWikipediaScraper(unittest.TestCase):

    def setUp(self):
        # Setup code, if necessary
        pass

    def test_file_creation(self):
        page_title = "Artificial Intelligence"
        html_content = get_wikipedia_page_content(page_title)
        if html_content:
            summary = extract_summary(html_content)
            references = extract_references(html_content)

            # Writing to a text file
            with open("test_wikipedia_page_content.txt", "w", encoding="utf-8") as file:
                file.write("Summary:\n")
                file.write(summary + "\n\n")
                file.write("References:\n")
                for i, ref in enumerate(references, start=1):
                    file.write(f"Reference {i}: {ref}\n")

            self.assertTrue(os.path.exists("test_wikipedia_page_content.txt"))

    def test_file_content(self):
        with open("test_wikipedia_page_content.txt", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("Summary:", content)
            self.assertIn("References:", content)

    def tearDown(self):
        # Remove the file after the test
        if os.path.exists("test_wikipedia_page_content.txt"):
            os.remove("test_wikipedia_page_content.txt")

if __name__ == '__main__':
    unittest.main()
