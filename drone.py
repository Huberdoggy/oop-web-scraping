import signal
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup


class Drone:
    def __init__(self) -> None:
        pass

    def _sigHandler():
        raise Exception

    def _getPageMarkup(self, url: str, handlers: list):
        try:
            html = urlopen(url)
            bs = BeautifulSoup(html, "lxml")
            return bs.title
        except Exception as e:
            if type(e) in handlers:
                print(f"[!] An error occured:\n\n{e}")
            return None


class Scout(Drone):
    def __init__(self) -> None:
        self.prefix = "https://www."
        self.base_domain = input(
            "Enter the base domain name to scrape => "
        ).strip()  # Explicit override
        self.handlers = [HTTPError, AttributeError]
        # Usage of 'signal' module is temp workaround for infinite hanging on printing
        # body when not caught by other handlers in my list
        signal.signal(
            signal.SIGALRM, self._sigHandler
        )  # Register with handler function to raise Exception
        signal.alarm(10)
        try:
            self.page_data = self._getPageMarkup(
                self.prefix + self.base_domain, self.handlers
            )
            signal.alarm(0)  # Reset alarm on success
        except Exception:
            self.page_data = None
