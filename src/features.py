# src\features.py
import re
from urllib.parse import urlparse

ip_regex = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")

def has_ip(netloc: str) -> int:
    return int(bool(ip_regex.search(netloc)))

def count_digits(s: str) -> int:
    return sum(c.isdigit() for c in s)

def extract_tokens(s: str):
    parts = re.split(r"[^a-zA-Z0-9]+", s)
    return [p.lower() for p in parts if p]

def url_features(url: str):
    parsed = urlparse(url if "://" in url else "http://" + url)
    netloc = parsed.netloc or parsed.path
    path = parsed.path or ""
    query = parsed.query or ""
    tokens = extract_tokens(netloc) + extract_tokens(path) + extract_tokens(query)

    feats = {
        "url_len": len(url),
        "host_len": len(netloc),
        "path_len": len(path),
        "count_dots": netloc.count(".") + path.count("."),
        "count_hyphen": url.count("-"),
        "count_at": url.count("@"),
        "count_qm": url.count("?"),
        "count_digits": count_digits(url),
        "has_ip": has_ip(netloc),
        "suspicious_tokens": sum(1 for t in tokens if t in ("login","signin","secure","verify","confirm","account")),
    }
    return feats
