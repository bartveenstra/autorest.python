﻿# --------------------------------------------------------------------------
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
import json
import isodate
from async_generator import yield_, async_generator
from azure.core.exceptions import DecodeError
from datetime import date, datetime, timedelta
from base64 import b64encode
from bodyarray.aio import AutoRestSwaggerBATArrayService
from bodyarray.models import Product
from bodyarray._rest import array
import msrest

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATArrayService(base_url="http://localhost:3000") as client:
        await yield_(client)


@pytest.fixture
def datetimes():
    datetime1 = isodate.parse_datetime("2000-12-01T00:00:01Z")
    datetime2 = isodate.parse_datetime("1980-01-02T00:11:35Z")
    datetime3 = isodate.parse_datetime("1492-10-12T10:15:01Z")
    return [datetime1, datetime2, datetime3]

@pytest.fixture
def products():
    prod1 = Product(integer=1, string="2")
    prod2 = Product(integer=3, string="4")
    prod3 = Product(integer=5, string="6")
    return [prod1.serialize(), prod2.serialize(), prod3.serialize()]

@pytest.fixture
def listdict():
    return [{"1": "one", "2": "two", "3": "three"},
            {"4": "four", "5": "five", "6": "six"},
            {"7": "seven", "8": "eight", "9": "nine"}]

@pytest.fixture
def make_request(client, base_make_request):
    async def _make_request(request):
        return await base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    async def _make_request(request):
        return await base_make_request_json_response(client, request)
    return _make_request

@pytest.mark.asyncio
async def test_empty(make_request, make_request_json_response):
    request = array.build_get_empty_request()

    assert [] ==  await make_request_json_response(request)

    request = array.build_get_null_request()
    response = await make_request(request)
    assert response.text == ''

    request = array.build_put_empty_request(json=[])
    await make_request(request)

@pytest.mark.asyncio
async def test_boolean_tfft(make_request, make_request_json_response):
    request = array.build_get_boolean_tfft_request()
    assert [True, False, False, True]  == await make_request_json_response(request)
    request = array.build_put_boolean_tfft_request(json=[True, False, False, True])
    await make_request(request)

@pytest.mark.asyncio
async def test_integer_valid(make_request, make_request_json_response):
    request = array.build_get_integer_valid_request()
    assert [1, -1, 3, 300] ==  await make_request_json_response(request)
    request = array.build_put_integer_valid_request(json=[1, -1, 3, 300])
    await make_request(request)

@pytest.mark.asyncio
async def test_long_valid(make_request, make_request_json_response):
    request = array.build_get_long_valid_request()
    assert [1, -1, 3, 300] == await make_request_json_response(request)
    request = array.build_put_long_valid_request(json=[1, -1, 3, 300])
    await make_request(request)

@pytest.mark.asyncio
async def test_float_valid(make_request, make_request_json_response):
    request = array.build_get_float_valid_request()
    assert [0, -0.01, -1.2e20] ==  await make_request_json_response(request)
    request = array.build_put_float_valid_request(json=[0, -0.01, -1.2e20])
    await make_request(request)

@pytest.mark.asyncio
async def test_double_valid(make_request, make_request_json_response):
    request = array.build_get_double_valid_request()
    assert [0, -0.01, -1.2e20] == await make_request_json_response(request)
    request = array.build_put_double_valid_request(json=[0, -0.01, -1.2e20])
    await make_request(request)

@pytest.mark.asyncio
async def test_string_valid(make_request, make_request_json_response):
    request = array.build_get_string_valid_request()
    assert ["foo1", "foo2", "foo3"] ==  await make_request_json_response(request)
    request = array.build_put_string_valid_request(json=["foo1", "foo2", "foo3"])
    await make_request(request)

@pytest.mark.asyncio
async def test_get_string_with_null(make_request_json_response):
    request = array.build_get_string_with_null_request()
    assert ["foo", None, "foo2"] ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_string_with_invalid(make_request_json_response):
    request = array.build_get_string_with_invalid_request()

    # response differs from convenience layer
    # this is bc in convenence layer we tell the demsrest_serializer to deserialize it fully as a list of string
    assert ["foo", 123, "foo2"] ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_uuid_valid(make_request, make_request_json_response):
    request = array.build_get_uuid_valid_request()
    assert ["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "d1399005-30f7-40d6-8da6-dd7c89ad34db",
                        "f42f6aa1-a5bc-4ddf-907e-5f915de43205"] == await make_request_json_response(request)
    request = array.build_put_uuid_valid_request(json=["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "d1399005-30f7-40d6-8da6-dd7c89ad34db",
                        "f42f6aa1-a5bc-4ddf-907e-5f915de43205"])
    await make_request(request)

@pytest.mark.asyncio
async def test_get_uuid_invalid_chars(make_request, make_request_json_response):
    #Handles invalid characters without error because of no guid class
    request = array.build_get_uuid_invalid_chars_request()
    assert ["6dcc7237-45fe-45c4-8a6b-3a8a3f625652", "foo"] == await make_request_json_response(request)

@pytest.mark.asyncio
async def test_date_valid(make_request, make_request_json_response):
    def datetime_handler(x):
        if isinstance(x, datetime.date):
            return x.isoformat()
        raise TypeError("Unknown type")
    date1 = isodate.parse_date("2000-12-01")
    date2 = isodate.parse_date("1980-01-02")
    date3 = isodate.parse_date("1492-10-12")

    request = array.build_get_date_valid_request()
    assert await make_request_json_response(request), [date1, date2 ==  date3]
    request = array.build_put_date_valid_request(json=[str(date1), str(date2), str(date3)])  # dates are not json serializable
    await make_request(request)

@pytest.mark.asyncio
async def test_date_time_valid(make_request, make_request_json_response, datetimes, msrest_serializer):
    request = array.build_get_date_time_valid_request()

    assert await make_request_json_response(request), [datetimes[0], datetimes[1] ==  datetimes[2]]
    request = array.build_put_date_time_valid_request(json=[msrest_serializer.serialize_iso(datetime) for datetime in datetimes])
    await make_request(request)

@pytest.mark.asyncio
async def test_date_time_rfc1123_valid(make_request, make_request_json_response, datetimes, msrest_serializer):
    request = array.build_get_date_time_rfc1123_valid_request()
    assert await make_request_json_response(request), [datetimes[0], datetimes[1] ==  datetimes[2]]
    request = array.build_put_date_time_rfc1123_valid_request(json=[msrest_serializer.serialize_rfc(datetime) for datetime in datetimes])
    await make_request(request)

@pytest.mark.asyncio
async def test_duration_valid(make_request, make_request_json_response):
    duration1 = timedelta(days=123, hours=22, minutes=14, seconds=12, milliseconds=11)
    duration2 = timedelta(days=5, hours=1)

    request = array.build_get_duration_valid_request()
    assert await make_request_json_response(request), [duration1 ==  duration2]
    request = array.build_put_duration_valid_request(json=[isodate.duration_isoformat(duration1), isodate.duration_isoformat(duration2)])
    await make_request(request)

@pytest.mark.asyncio
async def test_byte_valid(make_request, make_request_json_response):
    bytes1 = bytearray([0x0FF, 0x0FF, 0x0FF, 0x0FA])
    bytes2 = bytearray([0x01, 0x02, 0x03])
    bytes3 = bytearray([0x025, 0x029, 0x043])

    request = array.build_get_byte_valid_request()
    assert await make_request_json_response(request), [bytes1, bytes2 ==  bytes3]
    request = array.build_put_byte_valid_request(json=[b64encode(b).decode() for b in [bytes1, bytes2, bytes3]])
    await make_request(request)

@pytest.mark.asyncio
async def test_get_byte_invalid_null(make_request_json_response):
    request = array.build_get_byte_invalid_null_request()
    assert await make_request_json_response(request), [bytearray([0x0AB, 0x0AC, 0x0AD]) ==  None]

@pytest.mark.asyncio
async def test_get_complex_null(make_request):
    request = array.build_get_complex_null_request()
    assert (await make_request(request)).text == ''

@pytest.mark.asyncio
async def test_get_complex_empty(make_request_json_response):
    request = array.build_get_complex_empty_request()
    assert [] == await make_request_json_response(request)

@pytest.mark.asyncio
async def test_complex_valid(make_request, make_request_json_response, products):
    request = array.build_get_complex_valid_request()
    assert products ==  await make_request_json_response(request)
    request = array.build_put_complex_valid_request(json=products)
    await make_request(request)

@pytest.mark.asyncio
async def test_get_array_valid(make_request, make_request_json_response):
    listlist = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    request = array.build_get_array_valid_request()
    assert listlist ==  await make_request_json_response(request)
    request = array.build_put_array_valid_request(json=listlist)
    await make_request(request)


@pytest.mark.asyncio
async def test_dictionary_valid(make_request, make_request_json_response, listdict):
    request = array.build_get_dictionary_valid_request()
    assert listdict ==  await make_request_json_response(request)
    request = array.build_put_dictionary_valid_request(json=listdict)
    await make_request(request)

@pytest.mark.asyncio
async def test_get_complex_item_null(make_request_json_response, products):
    products_null = [products[0], None, products[2]]
    request = array.build_get_complex_item_null_request()
    assert products_null == await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_complex_item_empty(make_request_json_response, products):
    products_empty = [products[0], Product().serialize(), products[2]]

    request = array.build_get_complex_item_empty_request()
    assert products_empty ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_array_null(make_request):
    request = array.build_get_array_null_request()
    assert (await make_request(request)).text == ''

@pytest.mark.asyncio
async def test_get_array_empty(make_request_json_response):
    request = array.build_get_array_empty_request()
    assert [] ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_array_item_null(make_request_json_response):
    listlist2 = [["1", "2", "3"], None, ["7", "8", "9"]]
    request = array.build_get_array_item_null_request()
    assert listlist2 ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_array_item_empty(make_request_json_response):
    listlist3 = [["1", "2", "3"], [], ["7", "8", "9"]]
    request = array.build_get_array_item_empty_request()
    assert listlist3 ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_dictionary_and_dictionary_item_null(make_request, make_request_json_response, listdict):

    request = array.build_get_dictionary_null_request()
    assert (await make_request(request)).text == ''

    listdict[1] = None
    request = array.build_get_dictionary_item_null_request()
    assert listdict == await make_request_json_response(request)

@pytest.mark.asyncio
async def test_get_dictionary_and_dictionary_item_empty(make_request_json_response, listdict):
    request = array.build_get_dictionary_empty_request()
    assert [] ==  await make_request_json_response(request)

    listdict[1] = {}
    request = array.build_get_dictionary_item_empty_request()
    assert listdict ==  await make_request_json_response(request)

@pytest.mark.asyncio
async def test_array_get_invalid(make_request_json_response):
    request = array.build_get_invalid_request()
    with pytest.raises(json.decoder.JSONDecodeError):
        await make_request_json_response(request)

@pytest.mark.asyncio
async def test_array_get_boolean_invalid_null(make_request_json_response):
    request = array.build_get_boolean_invalid_null_request()
    assert await make_request_json_response(request), [True, None ==  False]

@pytest.mark.asyncio
async def test_array_get_boolean_invalid_string(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_boolean_invalid_string_request()
    assert await make_request_json_response(request) == [True, "boolean", False]

@pytest.mark.asyncio
async def test_array_get_int_invalid_null(make_request_json_response):
    request = array.build_get_int_invalid_null_request()
    assert await make_request_json_response(request), [1, None ==  0]

@pytest.mark.asyncio
async def test_array_get_int_invalid_string(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_int_invalid_string_request()
    assert await make_request_json_response(request) == [1, "integer", 0]

@pytest.mark.asyncio
async def test_array_get_long_invalid_null(make_request_json_response):
    request = array.build_get_long_invalid_null_request()
    assert await make_request_json_response(request), [1, None ==  0]

@pytest.mark.asyncio
async def test_array_get_long_invalid_string(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_long_invalid_string_request()
    assert await make_request_json_response(request) == [1, "integer", 0]

@pytest.mark.asyncio
async def test_array_get_float_invalid_null(make_request_json_response):
    request = array.build_get_float_invalid_null_request()
    assert await make_request_json_response(request), [0.0, None ==  -1.2e20]

@pytest.mark.asyncio
async def test_array_get_float_invalid_string(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_float_invalid_string_request()
    assert await make_request_json_response(request) == [1, "number", 0]

@pytest.mark.asyncio
async def test_array_get_double_invalid_null(make_request_json_response):
    request = array.build_get_double_invalid_null_request()
    assert await make_request_json_response(request), [0.0, None ==  -1.2e20]

@pytest.mark.asyncio
async def test_array_get_double_invalid_string(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_double_invalid_string_request()
    assert await make_request_json_response(request) == [1, "number", 0]

@pytest.mark.asyncio
async def test_array_get_string_with_invalid(make_request_json_response):
    request = array.build_get_string_with_invalid_request()
    assert await make_request_json_response(request), ["foo", "123" ==  "foo2"]

@pytest.mark.asyncio
async def test_array_get_date_invalid_null(make_request_json_response):
    request = array.build_get_date_invalid_null_request()
    assert await make_request_json_response(request), [isodate.parse_date("2012-01-01"), None ==  isodate.parse_date("1776-07-04")]

@pytest.mark.asyncio
async def test_array_get_date_invalid_chars(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_date_invalid_chars_request()
    assert await make_request_json_response(request) == ["2011-03-22", "date"]

@pytest.mark.asyncio
async def test_array_get_date_time_invalid_null(make_request_json_response):
    request = array.build_get_date_time_invalid_null_request()
    assert await make_request_json_response(request), [isodate.parse_datetime("2000-12-01T00:00:01Z") ==  None]

@pytest.mark.asyncio
async def test_array_get_date_time_invalid_chars(make_request_json_response):
    # don't raise deserialization error bc we're not msrest deserializing
    request = array.build_get_date_time_invalid_chars_request()
    assert await make_request_json_response(request) == ['2000-12-01t00:00:01z', 'date-time']

@pytest.mark.asyncio
async def test_array_get_base64_url(make_request_json_response, msrest_deserializer):
    test_array = ['a string that gets encoded with base64url'.encode(),
                    'test string'.encode(),
                    'Lorem ipsum'.encode()]
    request = array.build_get_base64_url_request()
    response = await make_request_json_response(request)
    assert [msrest_deserializer.deserialize_base64(s) for s in await make_request_json_response(request)] == test_array

@pytest.mark.asyncio
async def test_array_enum_valid(make_request, make_request_json_response):
    request = array.build_get_enum_valid_request()
    response = await make_request_json_response(request)
    assert response == ['foo1', 'foo2', 'foo3']
    request = array.build_put_enum_valid_request(json=response)
    await make_request(request)

@pytest.mark.asyncio
async def test_array_string_enum_valid(make_request, make_request_json_response):
    request = array.build_get_string_enum_valid_request()
    response = await make_request_json_response(request)
    assert response == ['foo1', 'foo2', 'foo3']
    request = array.build_put_string_enum_valid_request(json=response)
    await make_request(request)