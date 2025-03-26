import hashlib

def sign(line: bytes) -> str:
    # Remove trailing newline if present
    line = line.rstrip(b'\n')
    # SHA-1 digest, hex representation, first 20 characters
    return hashlib.sha1(line).hexdigest()[:20]

def scan(paths, signature):
    matching_paths = []
    for path in paths:
        with open(path, 'rb') as f:
            for line in f:
                if sign(line) == signature:
                    matching_paths.append(path)
                    break
    return matching_paths