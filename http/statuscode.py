'''All status codes have been provided for use internally or by applications
an underscore has been added to the end of keyword properties
statuses with a leading underscore are not used
if you're using all of these then you're a better coder than me'''

from enum import Enum

class StatusCode(Enum):
    """All status codes have been provided for continuity. Status codes who's name clashes with keywords have an underscore appended. statuses with leading underscores are not defined by an rfc or have been removed and should be used with causion, if you need one of these statuses then you'll probably know it. generic unrecognised errors are also provided for convinience"""
    
    unrecognised = "xxx"
    
    #1xx - information
    unrecognised_information = "1xx"
    continue_ = 100
    switching_protocols = 101
    processing = 102

    #2xx - success
    unrecognised_success = "2xx"
    ok = 200
    created = 201
    accepted = 202
    non_authorative_infomation = 203
    no_content = 204
    reset_content = 205
    partial_content = 206
    multi_status = 207 #RFC 4918 webDav
    already_reported = 208 #RFC 5842 webDav
    im_used = 226 #RFC 3229

    #3xx - redirection
    unrecognised_redirection = "3xx"
    multiple_choices = 300
    moved_permanently = 301
    found = 302
    see_other = 303
    not_modified = 304
    use_proxy = 305
    _switch_proxy = 306 #deprecated
    temporary_redirect = 307
    permanent_redirect = 308

    #4xx - client errors
    unrecognised_client_error = "4xx"
    bad_request = 400
    unauthorised = 401
    payment_required = 402
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    not_acceptable = 406
    proxy_authentication_required = 407
    request_timeout = 408
    conflict = 409
    gone = 410
    length_required = 411
    precondition_failed = 412
    request_entity_too_large = 413
    request_uri_too_large = 414
    unsupported_media_type = 415
    requested_range_not_satisfiable = 416
    expectation_failed = 417
    _im_a_teapot = 418 #RFC 2324 april fools
    _authentication_timeout = 419 #unknown
    _method_failure = 420 #deprecated spring framework error
    _enhance_your_calm = 420 #twitter api
    _unprocessed_entity = 422 #RFC 4918 webDav
    locked = 423 #RFC 4918 webDav
    _failed_dependency = 424 #Internet Draft
    unordered_collection = 425 #RFC 2817
    upgrade_required = 426 #RFC 2817
    precondition_required = 428 #RFC 6585
    too_many_requests = 429 #RFC 6585
    request_header_fields_too_large = 431 #RFC 6585
    _login_timeout = 440 #Microsoft
    _no_response = 444 #Nginx
    _retry_with = 449 #Microsoft
    _blocked_by_windows_perental_controls = 450 #Micosoft
    _unavailable_for_legal_reasons = 451 #Internet Draft
    _redirect = 451 #Microsoft
    _request_header_too_large = 494 #Nginx
    _cert_error = 495 #Nginx
    _no_cert = 496 #Nginx
    _http_to_https = 497 #Nginx
    _client_closed_request = 499 #Nginx

    #5xx Server Error
    unrecognised_server_error = "5xx"
    internal_server_error = 500
    not_implemented = 501
    bad_gateway = 502
    service_unavailable = 503
    gateway_timeout = 504
    http_version_not_supported = 505
    variant_also_negotiates = 506 #RFC 2295
    insufficent_storage = 507 #RFC 4918
    loop_detected = 508 #RFC 5842
    _bandwidth_limit_exceeded = 509 #Apache
    not_extended = 510 #RFC 2774
    network_authentication_required = 511 #RFC 6585
    _origin_error = 520 #cloudflare
    _web_server_is_down = 521 #cloudflare
    _connection_timed_out = 522 #cloudflare
    _proxy_declined_request = 523 #cloudflare
    _a_timeout_occurred = 524 #cloudflare
    _network_read_timeout_error = 598 #unknown
    _network_connect_timeout_error = 599 #unknown