import webbrowser, sys

webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))

if len(sys.argv) > 1:
	socials = sys.argv[1:]
	for social in socials:
		webbrowser.get(using='chrome').open(social + '.com')