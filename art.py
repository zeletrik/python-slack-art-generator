from pyfiglet import Figlet
import argparse
import clipboard

parser = argparse.ArgumentParser(description='Help for Slack Art Generator!')
parser.add_argument("--text", default=1, type=str, required=True, help="The text to make Slack art")
parser.add_argument("--emoji", default=2, type=str, required=True, help="The emoji to create the art")
args = parser.parse_args()


text = args.text
emoji = args.emoji

custom_fig = Figlet(font='banner')
asciiArt = custom_fig.renderText(text)

print("Default Ascii art:")
print(asciiArt)

slackArt = ":empty:\n" + asciiArt.replace(" ", ":empty:").replace("#", ":"+emoji+":")

print("Slack art: ")
print(slackArt)

clipboard.copy(slackArt)
print("Slack art copied to clipboard")
