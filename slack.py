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

msg_len_limit = 1000


# メンションが飛んできたときだけ対応する
@slack_events_adapter.on("app_mention")
def app_mention(event_data):
    event = event_data["event"]

    # 編集された場合もイベントが飛んでくるので無視する
    if "edited" in event:
        print("[INFO] Ignoring the edited")
        return

    # 他のボットに反応するとうるさいので無視する
    if "bot_id" in event:
        print("[INFO] Ignoring a message of bots (including myself)")
        return

    msg_recv = event["text"]
    if len(msg_recv) > msg_len_limit:
        print("[INFO] The message received is too long")
        print("[INFO] Replacing the message with a error message")
        msg_recv = "メッセージが長すぎます(1000文字まで)"
    else:
        print(f"[INFO] Message received: {msg_recv}")

    # メンションを削除
    msg_san = re.sub("<.*>", "", msg_recv)

    msg_send = norify(msg_san)
    print(f"[INFO] Message to send: {msg_send}")

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
