from django.http import JsonResponse

def send_json(request):

    data = [{'sec_key': '0T7/GhwID0jlZB9ydthwsy+3lGgRs3eEF+2VHiagi20CEgfOdWswSVuwa3RGoVxwhqq1bNXEhcmVS8NWGzyOi6aCA=|cc2950870408245f1b1b89dd8634bb4fe28bc30be5c1cbd46964d49d75c70bdc', 'ResultText': 'Enroll User', 'JSONVersion': '1.0.0', 'ResultCode': '0810', 'PartnerParams':{
    'user_id': '1', 'user_type': '1', 'job_id': '1'
    }},
            {'timestamp': '2018-03-13T16:15:04.834319', 'SmileJobID': '0000001000', 'IsMachineResult': 'true', 'ConfidenceValue': '96', 'IsFinalResult': 'true'}]


    return JsonResponse(data, safe=False)
