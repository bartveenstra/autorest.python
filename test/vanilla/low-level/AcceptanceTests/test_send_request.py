# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import io
import json

from azure.core.rest import HttpRequest

from os.path import dirname, pardir, join, realpath
import pytest

cwd = dirname(realpath(__file__))


class TestSendRequest(object):

    def test_send_request_with_body_get_model_deserialize(self):
        from bodycomplexlowlevel import AutoRestComplexTestService

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        request = HttpRequest("GET", "/complex/inheritance/valid",
        )

        response = client.send_request(request)
        response.raise_for_status()

        deserialized = response.json()
        assert 2 ==  deserialized['id']
        assert "Siameeee" ==  deserialized['name']
        assert -1 ==  deserialized['hates'][1]['id']
        assert "Tomato" == deserialized['hates'][1]['name']

    def test_send_request_with_stream_get_direct_json(self):
        from bodycomplexlowlevel import AutoRestComplexTestService

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        request = HttpRequest("GET", "/complex/inheritance/valid",
            headers={
                'Accept': 'application/json'
            },
        )

        with client.send_request(request, stream=True) as response:
            response.raise_for_status()
            data = ''.join([chunk for chunk in response.iter_text()])
        json_response = json.loads(data)
        assert 2 == json_response['id']
        assert "Siameeee" == json_response['name']
        assert - 1 == json_response['hates'][1]['id']
        assert "Tomato" == json_response['hates'][1]['name']

    def test_send_request_with_body_put_json_dumps(self):
        from bodycomplexlowlevel import AutoRestComplexTestService

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        siamese_body = {
            "id": 2,
            "name": "Siameeee",
            "color": "green",
            "hates":
                [
                    {
                        "id": 1,
                        "name": "Potato",
                        "food": "tomato"
                    },
                    {
                        "id": -1,
                        "name": "Tomato",
                        "food": "french fries"
                    }
                ],
            "breed": "persian"
        }

        request = HttpRequest("PUT", "/complex/inheritance/valid",
            json=siamese_body
        )
        assert request.headers['Content-Type'] == "application/json"
        response = client.send_request(request)
        response.raise_for_status()
        assert response.status_code == 200

    def test_send_request_get_stream(self):
        from bodyfilelowlevel import AutoRestSwaggerBATFileService

        client = AutoRestSwaggerBATFileService(base_url="http://localhost:3000", connection_data_block_size=1000)
        file_length = 0
        with io.BytesIO() as file_handle:

            request = HttpRequest("GET", "/files/stream/nonempty",
                headers={
                    'Accept': 'image/png, application/json'
                },
            )

            with client.send_request(request, stream=True) as response:
                response.raise_for_status()
                for data in response.iter_bytes():
                    file_length += len(data)
                    file_handle.write(data)

            assert file_length !=  0

            sample_file = realpath(
                join(cwd, pardir, pardir, pardir, pardir,
                    "node_modules", "@microsoft.azure", "autorest.testserver", "routes", "sample.png"))

            with open(sample_file, 'rb') as data:
                sample_data = hash(data.read())
            assert sample_data == hash(file_handle.getvalue())

    def test_send_request_put_stream(self):
        from bodyformdatalowlevel import AutoRestSwaggerBATFormDataService

        client = AutoRestSwaggerBATFormDataService(
            base_url="http://localhost:3000",
        )

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        with io.BytesIO(test_bytes) as stream_data:
            request = HttpRequest("PUT", '/formdata/stream/uploadfile',
                content=stream_data,
                headers={"Content-Type": "application/octet-stream"}
            )
            with client.send_request(request, stream=True) as response:
                response.raise_for_status()

    def test_send_request_full_url(self):
        from bodycomplexlowlevel import AutoRestComplexTestService

        client = AutoRestComplexTestService(base_url="http://fakeUrl")

        request = HttpRequest("GET", "http://localhost:3000/complex/inheritance/valid",
            headers={
                'Accept': 'application/json'
            },
        )

        response = client.send_request(request)
        response.raise_for_status()

        deserialized = response.json()
        assert 2 ==  deserialized['id']
        assert "Siameeee" ==  deserialized['name']
        assert -1 ==  deserialized['hates'][1]['id']
        assert "Tomato" ==  deserialized['hates'][1]['name']