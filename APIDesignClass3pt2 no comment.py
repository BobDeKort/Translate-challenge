import httplib2
import urllib
import json

def translate(text, language):

        outputArray = []
        GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
        TRANSLATE_URL = 'https://www.googleapis.com/language/translate/v2?key=' + GOOGLE_API_KEY + '&source=en&target=' + language + '&q='

        for inputArrays in text:
            text_encoded = urllib.quote_plus(inputArrays)
            url = TRANSLATE_URL + text_encoded

            http = httplib2.Http()
            response, body = http.request(url, "GET")

            parsed_body = json.loads(body)
            translatedText2 = parsed_body['data']['translations'][0]['translatedText']

            outputArray.append(translatedText2)

        return outputArray

test = translate(["Hello who is this", "This is not human"], 'es')
print(test[0])
print(test[1])
