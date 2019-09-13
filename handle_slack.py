#!/usr/bin/env python3
from collections import deque
from slackeventsapi import SlackEventAdapter
from trans import norify
import os
import re
import slack

# イベントAPI用の設定
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(
    slack_signing_secret,
    endpoint="/slack/events/"
)

# Slackクライアント用の設定
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
cl = slack.WebClient(slack_bot_token)

# ポートの設定
port = os.environ["PORT"]

# 最大メッセージ長(超過したらエラーメッセージを返す)
msg_len_limit = 1000

# イベント履歴(同一メッセージがトリガーしたイベントは無視するようにする)
# 区別にはイベントIDがあれば十分なのでそれだけ覚えておく
event_hist = deque(maxlen=100)


# メンションが飛んできたときだけ対応する
@slack_events_adapter.on("app_mention")
def app_mention(event_data):
    # イベントIDを取得
    event_id = event_data.get("event_id")

    # すでに処理したイベントだったとき
    if event_id in event_hist:
        print("[INFO] Ignoring duplicates")
        return

    event_hist.append(event_id)

    event = event_data["event"]

    # 編集された場合もイベントが飛んでくるので無視する
    if "edited" in event:
        print("[INFO] Ignoring the edited")
        return

    # 自分や他のボットに反応するとうるさいので無視する
    if "bot_id" in event:
        print("[INFO] Ignoring a message of bots (including myself)")
        return

    msg_recv = event["text"]
    msg_send = ""
    if len(msg_recv) > msg_len_limit:
        print("[INFO] The message received is too long")
        print("[INFO] Replacing the message with a error message")
        msg_send = norify("メッセージ長すぎ(1000文字まで)")
        msg_send = ":no_entry: " + msg_send + " :no_entry:"
    else:
        print(f"[INFO] Message received: {msg_recv}")

        # メンションを削除
        msg_san = re.sub(r"<@.+?>\s*", "", msg_recv)

        msg_send = norify(msg_san)
        print(f"[INFO] Message to send: {msg_send}")

    chan = event["channel"]
    status = cl.chat_postMessage(
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
