from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import AnonymousUser, RequestInfo
from api.models import TokenV2, TokenV1


# tutorial: for protection against:
#                           1:) repetitive chained requests => error = block_attacks(request, False, False)
#                                                              return error
#                           2:) repetitive chained requests & repetitive unauthorized requests(only if your route needs
#                               logIn or authorization) => error = block_attacks(request, True, False)
#                                                          return error
#                           3:) repetitive chained requests & repetitive unauthorized requests with using token for
#                               verification(usually in APIs) => error = block_attacks(request, True, False)
#                                                                return error
def block_attacks(request, authorization_sensitive, token_based):
    h = 5  # danger interval between requests
    n = 10  # maximum number of repetitive fast requests
    unauthorized_tolerance = 5  # maximum number of repetitive unauthorized requests

    ip, browser, time_stamp = gather_request_info(request)
    anonymous_user = find_or_make_anonymous_user(ip, time_stamp)

    # block the spammer
    if anonymous_user.fastRequestChain >= n:
        return HttpResponse('you got caught! \nidiot spammer')

    # block the unauthorized
    if authorization_sensitive and anonymous_user.repeatedUnauthorized >= unauthorized_tolerance:
        return HttpResponse('you got caught! \nidiot unauthorized jerk')

    # save request info
    request_info = make_and_save_request_info(anonymous_user, browser, time_stamp)

    # handle invasion probability(in other words: watch out :D )
    handle_dangerous_ip(anonymous_user, authorization_sensitive, h, request, time_stamp, token_based)


def handle_dangerous_ip(anonymous_user, authorization_sensitive, h, request, time_stamp, token_based):
    # fast requests
    request_time_difference = int(time_stamp - anonymous_user.lastRequestTimeStamp)
    if request_time_difference < h:
        anonymous_user.fastRequestChain += 1
    else:
        anonymous_user.fastRequestChain = 0
    anonymous_user.lastRequestTimeStamp = time_stamp
    # unauthorized requests
    if authorization_sensitive and not token_based:
        # unauthorized not token based
        if not request.user.is_authenticated:
            anonymous_user.repeatedUnauthorized += 1
        else:
            anonymous_user.repeatedUnauthorized = 0
    elif authorization_sensitive and token_based:
        # unauthorized token based
        v1 = True
        v2 = True
        token_hash = request.GET.get('key')
        if not token_hash:
            anonymous_user.repeatedUnauthorized += 1
        else:
            try:
                token = TokenV1.objects.get(key=token_hash)
            except TokenV1.DoesNotExist:
                v1 = False
            try:
                token = TokenV2.objects.get(key=token_hash)
            except TokenV2.DoesNotExist:
                v2 = False
            if not v1 and not v2:
                anonymous_user.repeatedUnauthorized += 1
            else:
                anonymous_user.repeatedUnauthorized = 0

    anonymous_user.save(update_fields=['fastRequestChain', 'lastRequestTimeStamp', 'repeatedUnauthorized'])


def gather_request_info(request):
    time_stamp = timezone.now().timestamp()
    browser = request.META.get('HTTP_USER_AGENT')
    ip = request.META.get('REMOTE_ADDR')
    return ip, browser, time_stamp


def find_or_make_anonymous_user(ip, time_stamp):
    try:
        # print('existing anonymous user')
        anonymous_user = AnonymousUser.objects.get(pk=ip)
    except AnonymousUser.DoesNotExist:
        # print('a new anonymous user')
        anonymous_user = AnonymousUser(ip=ip, lastRequestTimeStamp=time_stamp)
        anonymous_user.save()
    return anonymous_user


def make_and_save_request_info(anonymous_user, browser, time_stamp):
    request_info = RequestInfo(anonymousUser=anonymous_user, browser=browser, timeStamp=time_stamp)
    request_info.save()
    return request_info
