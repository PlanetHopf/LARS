import unittest
from Wikipedia_Data import extract_references

class TestExtractReferences(unittest.TestCase):

    def test_extract_references(self):
        # Test case 1: Ensure the function works with a valid HTML content
        html_content = '<div><span class="reference-text">Reference 1</span><span class="reference-text">Reference 2</span></div>'
        expected_references = ['Reference 1', 'Reference 2']
        self.assertEqual(extract_references(html_content), expected_references)

        # Test case 2: Ensure the function works with an empty HTML content
        empty_html_content = ''
        self.assertEqual(extract_references(empty_html_content), [])

        # Test case 3: Ensure the function works with HTML content containing no references
        html_without_references = '<div><p>Some text</p></div>'
        self.assertEqual(extract_references(html_without_references), [])

if __name__ == '__main__':
    unittest.main()

class TestExtractFunction(unittest.TestCase):
    def test_extract_references(self):
        html_content= []
        self.assertTrue(data['parse']['text']['*'])
