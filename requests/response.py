from typing import Any
from os import fstat

from requests import HTTPResponseCode
from requests import PROTOCOL


class Response:
    def __init__(self, file) -> None:
        self.file = file
        self.status = HTTPResponseCode.OK
        self.headers = []
        self.body = None
        self.file_body = None

    def set_status(self, status: Any) -> None:
        self.status = status

    def add_header(self, name: str, value: Any) -> None:
        self.headers.append(
            {'name': name, 'value': value}
        )

    def set_body(self, body: str) -> None:
        self.body = body.encode()
        self.add_header('Content-Length', len(self.body))

    def set_file_body(self, file) -> None:
        self.file_body = file
        size = fstat(file)
        self.add_header('Content-Length', size)

    def _get_status_line(self) -> str:
        return f'{PROTOCOL} {self.status.code} {self.status.message}'

    def send(self) -> None:
        headers = self._get_response_headers()
        self.file.write(headers)

        if self.body:
            self.file.write(self.body)

        elif self.file_body:
            self._write_file_body()

    def _get_response_headers(self) -> ...:
        status_line = self._get_status_line()
        headers = [status_line]
        for header in self.headers:
            headers.append(f'{header["name"]}: {header["value"]}')

        header_string = '\r\n'.join(headers)
        header_string += '\r\n\r\n'
        return header_string.encode()

    def _write_file_body(self) -> None:
        while True:
            data = self.file_body.read(1024)
            if not data:
                break

            self.file.write(data)
