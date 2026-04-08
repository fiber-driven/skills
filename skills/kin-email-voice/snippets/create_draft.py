from __future__ import annotations

import base64
import os
import sys
from email.mime.text import MIMEText
from typing import Optional

sys.path.insert(0, os.path.expanduser("~/.claude/skills/lod-google-workspace"))
from snippets.client import get_gmail_service  # noqa: E402


def create_draft(
    to: str,
    subject: str,
    body: str,
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
    in_reply_to: Optional[str] = None,
    thread_id: Optional[str] = None,
) -> str:
    """Create a Gmail draft for kin@lightson.co.

    Returns the draft ID. The draft appears in Gmail's Drafts folder
    at https://mail.google.com/mail/u/1/#drafts

    Args:
        to: Recipient email(s), comma-separated for multiple.
        subject: Email subject line.
        body: Plain text body.
        cc: CC recipients, comma-separated.
        bcc: BCC recipients, comma-separated.
        in_reply_to: Message-ID header for threading replies.
        thread_id: Gmail thread ID to attach the draft to an existing thread.
    """
    gmail = get_gmail_service("kin@lightson.co")

    msg = MIMEText(body)
    msg["to"] = to
    msg["subject"] = subject
    if cc:
        msg["cc"] = cc
    if bcc:
        msg["bcc"] = bcc
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
        msg["References"] = in_reply_to

    encoded = base64.urlsafe_b64encode(msg.as_bytes()).decode("utf-8")

    draft_body = {"message": {"raw": encoded}}
    if thread_id:
        draft_body["message"]["threadId"] = thread_id

    draft = gmail.users().drafts().create(userId="me", body=draft_body).execute()
    return draft["id"]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a Gmail draft")
    parser.add_argument("--to", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--cc", default=None)
    parser.add_argument("--bcc", default=None)
    parser.add_argument("--thread-id", default=None)
    args = parser.parse_args()

    draft_id = create_draft(
        to=args.to,
        subject=args.subject,
        body=args.body,
        cc=args.cc,
        bcc=args.bcc,
        thread_id=args.thread_id,
    )
    print(f"Draft created: {draft_id}")
    print("View at: https://mail.google.com/mail/u/1/#drafts")
