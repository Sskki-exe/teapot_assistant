import random
import re

http_code_dict = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Content",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required"
}

def translate_to_text(http_code):
    print("    " + http_code_dict[http_code])

# 204 No Content

opinion_good = [
    200, # Ok
    202, # Accepted
]

opinion_bad = [
    406, # Not Acceptable
    417, # Expectation Failed
]

excuses = [
    408, # Request Timeout 
    418, # I'm a teapot
    426, # Upgrade Required
    429, # Too Many Requests
    501, # Not Implemented
]

missing = [
    404, # Missing
    410, # Gone
]

locations = [
    301, # Moved Permanently
    302, # Found
    404, # Missing
    410, # Gone
]

permission_denied = [
    401, # Unauthorised
    403, # Forbidden
    405, # Method Not Allowed
    406, # Not Acceptable
    407, # Proxy Authentication Required
    511, # Network Authentication Required
]

request_denied = [
    400, # Bad request
    402, # Payment Required
    421, # Misdirected Request
]

def generate_response(input_text):
    # lower case, strip punctuation and split into words
    unigrams = re.sub(r"[^\w\s]", "", input_text.lower()).split()
    bigrams = [f"{unigrams[i]} {unigrams[i+1]}" for i in range(len(unigrams) - 1)]
    trigrams = [f"{unigrams[i]} {unigrams[i+1]} {unigrams[i+2]}" for i in range(len(unigrams) - 2)]

    input_text = unigrams + bigrams + trigrams
    print(input_text)
    if any(a in input_text for a in ["remember"]):
        print("remember")
        return 507 # Insufficient Storage
    if any(a in input_text for a in ["which", "choose", "select", "option"]):
        print("multiple choices")
        return 300 # multiple choices
    if any(a in input_text for a in ["dad joke"]):
        print("dad joke")
        return random.choice(missing)
    if any(a in input_text for a in ["mom joke","mama joke","fat"]):
        print("mom joke")
        return 413 # Payload too large
    if any(a in input_text for a in ["youtube","spotify","maps","gps",
                                     "google","chat gpt"]):
        print("services")
        return 503 # Service Unavailable
    if any(a in input_text for a in ["cia","fbi",
                                     "area 52","aliens","conspiracy",
                                     "drug","drugs","meth","weed",
                                     "marijuana","lsd","cocaine"]):
        print("legal reasons")
        return 451 # Unavailable For Legal Reasons
    if any(a in input_text for a in ["length","dick joke","sex joke","long enough"]):
        print("length")
        return 411 # Length Required
    if any(a in input_text for a in ["war","battle","conflict","combat","invasion","military"]):
        print("conflict")
        return 409 # conflict    
    if any(a in input_text for a in ["loop", "again", "forever", "repeat"]):
        print("loop")
        return 508 # Loop Detected
    if any(a in input_text for a in ["where", "location", "place",
                                     "situated", "address"]):
        print("locations")
        return random.choice(locations)
    if any(a in input_text for a in ["ok","okay","sure","fine","alright","cool","yes"]):
        print("ok")
        return 200 # OK
    if any(a in input_text for a in ["morning","mornings","early","sunrise"]):
        print("too early")
        return 425 # too early
    if any(a in input_text for a in ["hello","hi","greetings",
                                     "day","night","afternoon",
                                     "bye","goodbye","see you",
                                     "whats up","yo","howdy",
                                     "hows it going","evening"]):
        print("greetings")
        return 200 # Ok
    if any(a in input_text for a in ["look","see","listen","hear"
                                     "taste","smell","watch","touch"]):
        print("senses")
        return 422 # Unprocessable Content
    if any(a in input_text for a in ["music","movie","movies",
                                     "song","songs","playlist"]):
        print("media")
        return 415 # Unsupported Media Type
    if any(a in input_text for a in ["can you", "please", "command", "request", "do this","order","execute"]):
        print("request")
        return random.choice(request_denied)
    if any(a in input_text for a in ["can i","may i","allowed to",
                                     "legal","illegal","law","permission","able to"]):
        print("permission")
        if random.choice([True, False]):
            return random.choice(opinion_good)
        return random.choice(permission_denied)
    if any(a in input_text for a in ["opinion","think","reckon","believe","stance"]):
        print("opinion")
        if random.choice([True, False]):
            return random.choice(opinion_good)
        return random.choice(opinion_bad)
    if any(a in input_text for a in ["you","yourself", "your name"]):
        print("teapot")
        return 418 # I'm a teapot
    print("excuse")
    return random.choice(excuses)

prev_output = ""

while True:    
    input_text = input("ask the teapot: ")
    http_code = generate_response(input_text)

    if prev_output == http_code and prev_output != 508: # loop exception
        http_code = 208 # Already Reported
    # handle "how about" after permission denied
    prev_output = http_code

    translate_to_text(http_code)