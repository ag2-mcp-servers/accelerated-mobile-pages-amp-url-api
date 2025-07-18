# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T00:36:05+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class AmpUrl(BaseModel):
    ampUrl: Optional[str] = Field(
        None, description="The AMP URL pointing to the publisher's web server."
    )
    cdnAmpUrl: Optional[str] = Field(
        None,
        description='The [AMP Cache URL](/amp/cache/overview#amp-cache-url-format) pointing to the cached document in the Google AMP Cache.',
    )
    originalUrl: Optional[str] = Field(None, description='The original non-AMP URL.')


class ErrorCode(Enum):
    ERROR_CODE_UNSPECIFIED = 'ERROR_CODE_UNSPECIFIED'
    INPUT_URL_NOT_FOUND = 'INPUT_URL_NOT_FOUND'
    NO_AMP_URL = 'NO_AMP_URL'
    APPLICATION_ERROR = 'APPLICATION_ERROR'
    URL_IS_VALID_AMP = 'URL_IS_VALID_AMP'
    URL_IS_INVALID_AMP = 'URL_IS_INVALID_AMP'


class AmpUrlError(BaseModel):
    errorCode: Optional[ErrorCode] = Field(
        None, description='The error code of an API call.'
    )
    errorMessage: Optional[str] = Field(
        None, description='An optional descriptive error message.'
    )
    originalUrl: Optional[str] = Field(None, description='The original non-AMP URL.')


class LookupStrategy(Enum):
    FETCH_LIVE_DOC = 'FETCH_LIVE_DOC'
    IN_INDEX_DOC = 'IN_INDEX_DOC'


class BatchGetAmpUrlsRequest(BaseModel):
    lookupStrategy: Optional[LookupStrategy] = Field(
        None, description='The lookup_strategy being requested.'
    )
    urls: Optional[List[str]] = Field(
        None,
        description='List of URLs to look up for the paired AMP URLs. The URLs are case-sensitive. Up to 50 URLs per lookup (see [Usage Limits](/amp/cache/reference/limits)).',
    )


class BatchGetAmpUrlsResponse(BaseModel):
    ampUrls: Optional[List[AmpUrl]] = Field(
        None,
        description='For each URL in BatchAmpUrlsRequest, the URL response. The response might not be in the same order as URLs in the batch request. If BatchAmpUrlsRequest contains duplicate URLs, AmpUrl is generated only once.',
    )
    urlErrors: Optional[List[AmpUrlError]] = Field(
        None, description='The errors for requested URLs that have no AMP URL.'
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'
