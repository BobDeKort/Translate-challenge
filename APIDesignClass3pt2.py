# This library has to be imported so that we can use this to make requests
import httplib2
# Included so that we don't have to add ASCII to add spaces
import urllib
# This converts
import json

'''
Challenges:
1. Create a Python wrapper function for Translate:
    print translate_text) -> translate_text

2. Extended your wrapper function with target language:
    print translate(text, language='XX') -> text in XX language

3. Extended your wrapper function to translate multiple strings:
    print translate([text1, text2, ...], language='XX')
    -> [text1 in XX language, text 2 in XX language, ...]

4. Add Twilio SMS functionality to text the translation to you!
'''

# Key has to be included in the URL so that we can get permission to be granted
# GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
# TRANSLATE_URL = '''https://www.googleapis.com/language/translate/v2?
#                    key=AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk&target=de&q='''
#
# # This is the text that will be translated
# text = "Hello World"
#
# ''' The text cannot be translated if there's space on the text.
#     Usually, we have to use %20. But this is not user friendly. But
#     by using urlib.quote_plus(text) this will allow the computer to
#     understand the spaces without using ASCII on the UI.
# '''
# text_encoded = urllib.quote_plus(text)
#
# ''' url concatenates both the googleapis url and the text that is encoded
#     that does not have to accept ASCII spaces.'''
# url = TRANSLATE_URL + text_encoded
#
# ''' Http is a class that is part of the httplib2 method. '''
# http = httplib2.Http()
# ''' We then send two arguments on the request method. "GET" is a syntax
#     understood by http.'''
# response, body = http.request(url, "GET")
#
# print(response)
# print(body)


def translate(text, language):

        outputArray = []

        ''' Key has to be included in the URL so that we can get permission to
            be granted '''
        GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
        TRANSLATE_URL = 'https://www.googleapis.com/language/translate/v2?key=' + GOOGLE_API_KEY + '&source=en&target=' + language + '&q='

        for inputArrays in text:
            ''' The text cannot be translated if there's space on the text.
                Usually, we have to use %20. But this is not user friendly. But
                by using urlib.quote_plus(text) this will allow the computer to
                understand the spaces without using ASCII on the UI.
            '''
            text_encoded = urllib.quote_plus(inputArrays)

            ''' url concatenates both the googleapis url and the text that is encoded
                that does not have to accept ASCII spaces.'''
            url = TRANSLATE_URL + text_encoded

            ''' Http is a class that is part of the httplib2 method. '''
            http = httplib2.Http()
            ''' We then send two arguments on the request method. "GET" is a command
                understood by http.'''

            response, body = http.request(url, "GET")

            parsed_body = json.loads(body)
            translatedText2 = parsed_body['data']['translations'][0]['translatedText']

            outputArray.append(translatedText2)

        return outputArray

test = translate(["Hello who is this", "This is not human"], 'es')
print(test[0])
print(test[1])
