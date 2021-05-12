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
from mediatypes.aio import MediaTypesClient
from mediatypes._rest import *
from async_generator import yield_, async_generator

import pytest

@pytest.fixture
@async_generator
async def client():
    async with MediaTypesClient() as client:
        await yield_(client)

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    async def _make_request(request):
        return await base_make_request_json_response(client, request)
    return _make_request

@pytest.mark.asyncio
async def test_pdf(make_request_json_response):
    request = build_analyze_body_request(content=b"PDF", content_type="application/pdf")
    assert await make_request_json_response(request) == "Nice job with PDF"

@pytest.mark.asyncio
async def test_json(make_request_json_response):
    request = build_analyze_body_request(json={"source":"foo"})
    assert await make_request_json_response(request) == "Nice job with JSON"

@pytest.mark.asyncio
async def test_content_type_with_encoding(make_request_json_response):
    request = build_content_type_with_encoding_request(content="hello", content_type='text/plain; encoding=UTF-8')
    assert await make_request_json_response(request) == "Nice job sending content type with encoding"