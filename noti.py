from slacker import Slacker
import constant

slack = Slacker(constant.slackToken)

# Send a message to #general channel
slack.chat.post_message('#stocktrade', 'Hello fellow slackers!')