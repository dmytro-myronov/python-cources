import requests
import unittest
from unittest.mock import patch, Mock


class WebService:
    """
    A simple web service class that fetches data from a given URL.
    """

    def get_data(self, url: str) -> dict:
        """
        Performs a GET request to the specified URL and returns the JSON response.
        If the request fails, it returns an error dictionary.

        :param url: The URL to fetch data from.
        :return: A dictionary containing the response data or an error message.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}"}


class TestWebService(unittest.TestCase):
    """
    Unit tests for the WebService class using unittest and mock.
    """

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        """
        Tests if the get_data method correctly returns data on a successful request.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("http://example.com")
        self.assertEqual(result, {"data": "test"})

    @patch('requests.get')
    def test_get_data_not_found(self, mock_get):
        """
        Tests if the get_data method correctly handles a 404 error.
        """
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": "Not Found"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("http://example.com")
        self.assertEqual(result, {"error": "HTTP 404"})

    @patch('requests.get')
    def test_get_data_server_error(self, mock_get):
        """
        Tests if the get_data method correctly handles a 500 server error.
        """
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"error": "Server Error"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("http://example.com")
        self.assertEqual(result, {"error": "HTTP 500"})


if __name__ == '__main__':
    unittest.main()
