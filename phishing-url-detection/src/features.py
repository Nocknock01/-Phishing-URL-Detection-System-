# src/features.py




def suspicious_token_count(tokens) -> int:
return sum(1 for t in tokens if t in SUSPICIOUS_TOKENS)




def url_features(url: str):
"""Return a feature vector (dict) for a single URL."""
try:
parsed = urlparse(url)
except Exception:
parsed = urlparse('http://' + url)


netloc = parsed.netloc or parsed.path # in case url missing scheme
path = parsed.path or ''
query = parsed.query or ''


tokens = extract_tokens(netloc) + extract_tokens(path) + extract_tokens(query)


feats = {
'url_len': len(url),
'host_len': len(netloc),
'path_len': len(path),
'count_dots': netloc.count('.') + path.count('.'),
'count_hyphen': url.count('-'),
'count_at': url.count('@'),
'count_qm': url.count('?'),
'count_digits': count_digits(url),
'count_special': count_special(url),
'has_ip': has_ip(netloc),
'suspicious_tokens': suspicious_token_count(tokens),
}


# You can add more handcrafted features here
return feats




if __name__ == '__main__':
# quick test
test_urls = [
'http://example.com/login',
'http://192.168.0.1/confirm',
'https://secure-paypal.example.com/verify?user=1'
]
for u in test_urls:
print(u, url_features(u))