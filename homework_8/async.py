import asyncio
import requests


class AsyncFetcher:
    """
    A class to fetch data asynchronously with a delay before making a request.

    Methods
    -------
    say_hello:
        Prints a message, waits for 3 seconds, and then makes an HTTP request to Google.
    """

    async def say_hello(self):
        """
        Simulate an asynchronous action by waiting 3 seconds before making a request to Google.

        This function waits for 3 seconds, then sends an HTTP GET request to 'https://google.com'.
        It prints the response status code once the request is completed.
        """
        print("wait 3 sec before request to google")
        await asyncio.sleep(3)  # Wait for 3 seconds
        print("send request to google")
        google = requests.get("https://google.com")  # Make the HTTP request to Google
        status = google.status_code  # Get the status code from the response
        print(f"status {status}")  # Print the status code


async def main():
    """
    The main entry point of the program. Creates an instance of AsyncFetcher and calls the
    `say_hello` method asynchronously.
    """
    greeter = AsyncFetcher()  # Create an instance of AsyncFetcher
    await greeter.say_hello()  # Await the async method say_hello


# Run the main function asynchronously
asyncio.run(main())
