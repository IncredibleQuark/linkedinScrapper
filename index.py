from linkedin_api import Linkedin
import csv


# Authenticate using any Linkedin account credentials
api = Linkedin('your@email.com', 'yourpassword')

with open('list.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    resultsArray = []
    results = []
    for name, surname in spamreader:

        credentials = name + ' ' + surname
        print('Processing ' + credentials)
        results = api.search({'keywords': credentials}, 200)

        resultOne = results[0]['publicIdentifier']
        print(results[1]['publicIdentifier'])
        resultsArray.append(resultOne)

    with open('results.csv', "w", newline='') as resultfile:
        spamwriter = csv.writer(resultfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for result in resultsArray:
            print(result, "ress")
            spamwriter.writerow([credentials] + ['https://www.linkedin.com/in/' + result])
    resultfile.close()


csvfile.close()
