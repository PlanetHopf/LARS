import unittest
from Wikipedia_Data import extract_summary

class TestExtractSummary(unittest.TestCase):

    def test_extract_summary_with_summary(self):
        # Test case 1: Ensure the function works with a valid HTML content containing a summary
        html_content_with_summary = '<div><p>This is a summary.</p></div>'
        expected_summary = 'This is a summary.'
        self.assertEqual(extract_summary(html_content_with_summary), expected_summary)

    def test_extract_summary_without_summary(self):
        # Test case 2: Ensure the function returns the default message when no summary is found
        html_content_without_summary = '<div><div><span>Some text</span></div></div>'
        expected_default_message = 'No summary available.'
        self.assertEqual(extract_summary(html_content_without_summary), expected_default_message)

    def test_extract_summary_empty_html(self):
        # Test case 3: Ensure the function returns the default message when HTML content is empty
        empty_html_content = ''
        expected_default_message = 'No summary available.'
        self.assertEqual(extract_summary(empty_html_content), expected_default_message)

if __name__ == '__main__':
    unittest.main()
