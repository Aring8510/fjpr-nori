import os
import re
from trans import norify
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient

slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(
    slack_signing_secret,
    endpoint="/slack/events/"
)

slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
sc = SlackClient(slack_bot_token)

port = os.environ["PORT"]

# メンションが飛んできたときだけ対応する
@slack_events_adapter.on("app_mention")
def app_mention(event_data):
    event = event_data["event"]

    # 編集された場合もイベントが飛んでくるので無視する
    if "edited" in event:
        print("[INFO] Ignore the edited...")
        return

    # 他のボットに反応するとうるさいので無視する
    if "bot_id" in event:
        print("[INFO] Ignore a message of bots (including myself) ...")
        return

    msg_recv = event["text"]
    print(f"Message received: {msg_recv}")

    msg_send = norify(re.sub("<.*> ", "", msg_recv))
    print(f"Message to send: {msg_send}")

    chan = event["channel"]
    status = sc.api_call(
        "chat.postMessage",
        channel=chan,
        text=msg_send,
        as_user=True
    )
    ok = status.get("ok")
    if not ok:
        print("[INFO] Failed to send the message")
        print(status)
    else:
        print("[INFO] The message has sent successfully")


# Start the server on specified port
slack_events_adapter.start(host='0.0.0.0', port=port)
